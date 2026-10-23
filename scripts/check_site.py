"""Validate required portfolio files and local HTML references."""

from html.parser import HTMLParser
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROOT = (PROJECT_ROOT / os.environ.get("SITE_ROOT", ".")).resolve()
REQUIRED_FILES = ("index.html", "styles.css", "script.js")


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: set[str] = set()
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)

        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        attribute = "src" if tag in {"img", "script"} else "href" if tag in {"a", "link"} else None
        if attribute and values.get(attribute):
            self.references.add(values[attribute])


def local_path(reference: str, source_file: Path) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:", "data:")):
        return None

    path = unquote(parsed.path)
    base = ROOT if path.startswith("/") else source_file.parent
    target = (base / path.lstrip("/")).resolve()
    if ROOT not in target.parents and target != ROOT:
        raise ValueError(f"Reference escapes project root: {reference}")
    return target


def main() -> None:
    missing_required = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing_required:
        raise SystemExit(f"Missing required files: {', '.join(missing_required)}")

    html_files = sorted(ROOT.rglob("*.html"))
    if not html_files:
        raise SystemExit("No HTML files found")

    missing_references: list[str] = []
    reference_count = 0
    for html_file in html_files:
        parser = SiteParser()
        parser.feed(html_file.read_text(encoding="utf-8"))

        if parser.duplicate_ids:
            names = ", ".join(sorted(parser.duplicate_ids))
            raise SystemExit(f"Duplicate HTML ids in {html_file.relative_to(ROOT)}: {names}")

        reference_count += len(parser.references)
        for reference in sorted(parser.references):
            target = local_path(reference, html_file)
            if target is not None and not target.exists():
                missing_references.append(f"{html_file.relative_to(ROOT)} → {reference}")

    if missing_references:
        raise SystemExit(f"Missing local references: {', '.join(missing_references)}")

    print(f"Site validation passed: {len(html_files)} pages and {reference_count} references checked")


if __name__ == "__main__":
    main()
