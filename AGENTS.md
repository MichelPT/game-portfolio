# AGENTS.md

## Project

Minimal static portfolio for Michel Pierce Tahya's games. Visual direction: editorial, direct, and text-led. Inspired by the clarity of `dukope.com`, without copying its design or content.

## Stack

- Plain HTML, CSS, and minimal JavaScript
- No build step or dependencies
- Entry point: `index.html`

## Design rules

- Keep one chronological list of games as the core experience.
- Prefer strong typography, generous spacing, and restrained color.
- Avoid card grids, gradients, glass effects, stock imagery, and decorative UI.
- Make every line of copy useful. No marketing filler.
- Keep layout responsive and keyboard accessible.
- Respect `prefers-reduced-motion`.

## Content rules

- Never invent game names, descriptions, release dates, store links, awards, or screenshots.
- Placeholder content must remain visibly generic until real details are supplied.
- Show released games before work in progress.
- First game links to its real App Store page once URL is supplied.

## Editing

- Game entries live directly in `index.html`.
- Global visual tokens live at top of `styles.css`.
- Verified career facts live in `content/CAREER_PROFILE.md`; treat it as the canonical source for resume, cover-letter, and portfolio claims.
- Keep `content/RESUME.md` and `content/COVER_LETTER.md` consistent with the career profile.
- Never convert an unconfirmed detail into a public claim. Leave it under “Needs confirmation” until Michel verifies it.
- Keep JavaScript optional; site content must remain usable without it.
- Test desktop and narrow mobile widths after layout changes.

## Validation

Run a local static server from project root:

```sh
python3 -m http.server 4173
```

Then check `http://localhost:4173`.
