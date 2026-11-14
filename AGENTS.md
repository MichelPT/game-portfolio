# AGENTS.md

## Project

Minimal static portfolio for Michel Pierce Tahya's software and games. Visual direction: clean, direct, and text-led, following Apple Human Interface Guidelines principles: system font, clear size and weight hierarchy, 17px body text, 44px tap targets, and light and dark mode.

## Stack

- Plain HTML, CSS, and minimal JavaScript
- No build step or dependencies
- Entry point: `index.html` for software; `games/index.html` for games

## Design rules

- Keep one chronological list of games as the core experience at `/games/`.
- Prefer strong typography, generous spacing, and restrained color.
- Avoid card grids, gradients, glass effects, stock imagery, and decorative UI.
- Make every line of copy useful. No marketing filler.
- Write copy in plain first person. Avoid rhetorical-question hooks, "not X but Y" constructions, em dashes, and inflated words.
- Keep layout responsive and keyboard accessible.
- Respect `prefers-reduced-motion`.

## Content rules

- Never invent game names, descriptions, release dates, store links, awards, or screenshots.
- Placeholder content must remain visibly generic until real details are supplied.
- Show released games before work in progress.
- First game links to its real App Store page once URL is supplied.

## Editing

- Concise game previews live directly in `games/index.html`.
- Full game case studies live in `games/*.html` and must link back to the chronological index.
- Keep detailed process writing and complete galleries on case-study pages, not the homepage.
- Global visual tokens live at top of `styles.css`.
- Verified career facts live in `content/CAREER_PROFILE.md`; treat it as the canonical source for resume, cover-letter, and portfolio claims.
- Detailed ownership, playtest evidence, and design responses for each game live in `content/games/*.md`; update the relevant game file before changing its public case study.
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
