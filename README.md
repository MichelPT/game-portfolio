# Michel Pierce Tahya — Software & Game Portfolio

Minimal software and game portfolio with a direct, chronological presentation.

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

- `index.html` is the software, iOS, mobile, AI, and interactive-work index.
- `games/index.html` is the concise chronological game index.
- `ios/index.html` redirects the former `/ios/` route to the homepage.
- `design-practice.html` presents prototyping, playtesting, and design communication evidence.
- `games/*.html` contains the game index and full case studies.
- `assets/` contains project media; images are displayed without cropping.
- `styles.css` contains the shared visual system for the index and case studies.
- `scripts/check_site.py` validates every HTML page and its local references.

## Career content

- [`content/CAREER_PROFILE.md`](content/CAREER_PROFILE.md) is the canonical factual record.
- [`content/games/`](content/games/) keeps each game’s roles, methods, playtest findings, and design responses in a separate source file.
- [`content/RESUME.md`](content/RESUME.md) contains the application-ready resume copy.
- [`content/COVER_LETTER.md`](content/COVER_LETTER.md) contains the tailored cover letter.

Update the career profile first when new projects, tools, roles, or experience are confirmed.
