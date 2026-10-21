"""Validate required portfolio files and local HTML references."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ENTRY_POINT = ROOT / "index.html"
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


def local_path(reference: str) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:", "data:")):
        return None

    relative = Path(unquote(parsed.path).lstrip("/"))
    target = (ROOT / relative).resolve()
    if ROOT not in target.parents and target != ROOT:
        raise ValueError(f"Reference escapes project root: {reference}")
    return target


def main() -> None:
    missing_required = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing_required:
        raise SystemExit(f"Missing required files: {', '.join(missing_required)}")

    parser = SiteParser()
    parser.feed(ENTRY_POINT.read_text(encoding="utf-8"))

    if parser.duplicate_ids:
        raise SystemExit(f"Duplicate HTML ids: {', '.join(sorted(parser.duplicate_ids))}")

    missing_references = []
    for reference in sorted(parser.references):
        target = local_path(reference)
        if target is not None and not target.exists():
            missing_references.append(reference)

    if missing_references:
        raise SystemExit(f"Missing local references: {', '.join(missing_references)}")

    print(f"Site validation passed: {len(parser.references)} references checked")


if __name__ == "__main__":
    main()
