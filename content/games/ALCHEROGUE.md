# Alcherogue

## Project facts

- **Date:** October 8, 2026
- **Type:** Solo project
- **Engine:** Unity 6
- **Language:** C#
- **Roles:** Game designer, programmer, illustrator, technical artist
- **Technical work:** Implemented the game, its illustrations, and a 2.5D visual approach
- **Methods:** Paper prototyping, playable browser prototyping, Python verification scripts, economy simulation, perceptual testing, MDA, game-feel analysis, comparative analysis

## Design

An alchemy-shop game about pouring by eye without numerical measurements. Liquid colour is derived from the mixture’s properties and acts as the player’s only instrument. Accelerating flow makes larger pours harder to control. Potion results use a quality ladder instead of binary success or failure.

Rent, stock, haggling, and auctions repeat the same decision at different scales: take the sure result or reach for something better. Pouring and haggling reuse the same hold-and-release input.

## Structural iteration

- Cut a quiz-roguelite direction after nine versions because questions became exhausted once their answers were known.
- Cut a deduction direction after a Python script proved every four-jar arrangement could be solved in exactly two pours with one fixed strategy.
- Economy scripts exposed excessive free stock, predictable ingredient shortages, and rent pressure that arrived too late.
- Required precision varied by 3.1× between recipes, while visible hue feedback varied by 4.8×.
- One recipe produced only 2.8° of visible hue change, making memory-based judgement unfair.
- A browser prototype was used to compare constant flow with accelerating flow.

## Paper playtest

- **Participants:** 15
- **Prototype:** Players selected a potion, poured it into a customer’s container, and judged the result by timing the pour with a stopwatch because the paper version had no liquid graphics.
- **Observed response:** Most participants were highly engaged by the core action.
- **Main questions:** Whether selling currency felt important, how different customer-container shapes changed difficulty and fairness, what assistance players needed, and what motivated them to continue.
- **Distinctive finding:** Container geometry was not cosmetic. Different shapes changed how difficult the same pouring task felt, creating a unique but important fairness problem.
- **Design response:** Add a shop where players can refill supplies or buy measuring aids; limit the range of customer-container shapes; add a stronger narrative that gives players a reason to continue through the progression.

## Process evidence

- `assets/alcherogue/process/paper-playtest.jpg`: observing a player complete the paper version of the core loop.
- `assets/alcherogue/process/prototype-materials.jpg`: handmade potion, recipe, container, day, and currency materials.
- `assets/alcherogue/process/design-process.jpg`: the paper interface beside a digital narrative flow during design work.

## Public positioning

This is the strongest evidence of end-to-end ownership, quantitative systems design, prototyping, playtesting, and the ability to turn observations into concrete design changes.
