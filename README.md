# Michel Pierce Tahya — Game Portfolio

Minimal game portfolio inspired by the direct, chronological presentation of [dukope.com](https://dukope.com).

## Preview

```sh
python3 -m http.server 4173
```

Open `http://localhost:4173`.

## Branches and deployment

- Develop on `dev`.
- Pull requests targeting `main` run site validation.
- Pushes and merges to `main` validate and deploy to GitHub Pages.
- The custom domain will be configured separately.

## Site structure

- `index.html` is the concise chronological game index.
- `games/*.html` contains the full case study for each finished game.
- `assets/` contains project media; images are displayed without cropping.
- `styles.css` contains the shared visual system for the index and case studies.
- `scripts/check_site.py` validates every HTML page and its local references.

## Career content

- [`content/CAREER_PROFILE.md`](content/CAREER_PROFILE.md) is the canonical factual record.
- [`content/games/`](content/games/) keeps each game’s roles, methods, playtest findings, and design responses in a separate source file.
- [`content/RESUME.md`](content/RESUME.md) contains the application-ready resume copy.
- [`content/COVER_LETTER.md`](content/COVER_LETTER.md) contains the tailored cover letter.

Update the career profile first when new projects, tools, roles, or experience are confirmed.
