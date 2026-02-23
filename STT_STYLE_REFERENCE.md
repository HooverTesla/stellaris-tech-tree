# STT Style Reference

## Purpose
This file captures the current Stellaris Tech Tree (STT) visual and UI style system so it can be reused as the base style for the larger site.

This is intended as the quick source-of-truth for future implementation work.

## Source-of-Truth Files
1. `stellaris-tech-tree/assets/css/tech-tree.css`
2. `stellaris-tech-tree/assets/html/body.html`
3. `stellaris-tech-tree/assets/js/header.js`
4. `stellaris-tech-tree/assets/js/tech-tree.js`
5. `stellaris-tech-tree/index.html`

## Boot and Composition Model
1. `index.html` loads vendor libs and `node-template`.
2. `load_page()` injects shared CSS/HTML/JS into version routes.
3. Shared shell lives in `assets/html/body.html`.
4. Header/tabs logic lives in `assets/js/header.js`.
5. Tree rendering/search behavior lives in `assets/js/tech-tree.js`.

## Design Tokens (Current Hard-Coded Values)
These are not CSS variables yet; they are currently literals spread across CSS/JS.

### Base and Header Colors
1. Page background: `#474747` (`tech-tree.css` line 11)
2. Header bar background: `#333` (`tech-tree.css` line 378)
3. Tab lowlight: `#303030` (`tech-tree.css` line 420)
4. Tab highlight: `#474747` (`tech-tree.css` line 423)
5. Header border accent: `#2F6458` (`header.js` line 105, `tech-tree.css` line 477)
6. Right button gradient top: `#2b574e` (`header.js` line 106)
7. Right button gradient bottom: `#0D1717` (`header.js` line 107)

### Research Domain Colors
1. Society: `#5ACA9C` (`tech-tree.css` lines 267, 483)
2. Engineering: `#E29C43` (`tech-tree.css` lines 279, 488)
3. Physics: `#4396E2` (`tech-tree.css` lines 291, 493)

### Tier Text Colors
1. Tier 0: `#9d9d9d`
2. Tier 1: `#ffffff`
3. Tier 2: `#1eff00`
4. Tier 3: `#45a9ff`
5. Tier 4: `#c380f1`
6. Tier 5: `#ff8000`
Source: `tech-tree.css` lines 526-547

### Tooltip and Meta Colors
1. Tooltip border: `#327866`
2. Tooltip background: `rgba(30,30,30,0.9)`
3. Tooltip header text: `#f59f17`
Source: `tech-tree.css` lines 22, 27, 262

## Typography
1. Primary UI/body font: `'Arimo', Verdana`
2. Legacy Treant paragraph fallback: Helvetica/Arial stack
3. Symbol glyph font: `'Symbola'` from `../fonts/Symbola.ttf`

Reference:
1. `tech-tree.css` lines 18, 26, 63, 228, 406, 448
2. `tech-tree.css` lines 47-52 (`@font-face`)
3. `index.html` line 19 (Google Fonts Arimo)

## Core Layout and Component Contracts

### Header and Tabs
1. Header container class: `.float-Holder`
2. Tab class: `.float-Element`
3. Active/inactive state: `.float-Highlight` and `.float-Lowlight`
4. Tab text/icon class: `.float-Contents`, `.float-Image`
5. Right utility buttons: `.float-RightElement`, `.float-RightContents`
6. Hidden utility/state class: `.float-NoDisplay`

Reference:
1. `body.html` lines 1-74
2. `tech-tree.css` lines 374-467
3. `header.js` lines 14-67

### Content Zones
1. Search zone: `#tech-tree-search`
2. Physics zone: `#tech-tree-physics`
3. Society zone: `#tech-tree-society`
4. Engineering zone: `#tech-tree-engineering`
5. Events zone: `#tech-tree-anomalies`

Reference: `body.html` lines 75-91

### Tech Card
1. Root class: `.tech` (275x66 card)
2. Icon slot: `.tech div.icon` (52x52)
3. Research variants: `.tech.society`, `.tech.engineering`, `.tech.physics`
4. Special variants: `.tech.dangerous`, `.tech.rare`
5. Status indicator: `.tech div.node-status` and `.active`

Reference: `tech-tree.css` lines 54-149, 266-301

### Texture Background Assets (Card Skins)
1. `assets/css/tech_bg_society.png`
2. `assets/css/tech_bg_engineering.png`
3. `assets/css/tech_bg_physics.png`
4. `assets/css/tech_bg_dangerous.png`
5. `assets/css/tech_bg_rare.png`

All currently present in repo.

## Behavior That Drives Visual State
1. Tab click toggles visible content container and tab highlight classes.
2. Search tab (`float-SearchTab`) shows only `#tech-tree-search`.
3. Right-side button decorative backgrounds are generated in JS gradients.
4. Node search dim/highlight behavior modifies opacity (`1`, `0.6`, `0.1`).

Reference:
1. `header.js` lines 14-67, 98-138
2. `tech-tree.js` lines 95-205

## Asset Buckets
1. Icons: `stellaris-tech-tree/assets/icons`
2. Tech/event images: `stellaris-tech-tree/assets/img`
3. CSS texture backgrounds: `stellaris-tech-tree/assets/css/*.png`
4. Vendor CSS/JS: `stellaris-tech-tree/assets/vendor`

## Version Selection/Boot Integration Notes
1. STT now supports alias-based route selection.
2. Default alias is `latest`.
3. Current mapping: `latest -> phoenix-4.0.10`.
4. Host can set `window.STT_VERSION` or `window.STELLARIS_TECH_TREE_VERSION`.

Reference: `index.html` lines 149-190

## Reuse Plan For Overarching Site
Use this order when lifting style into global site design:
1. Promote hard-coded colors and sizes into CSS variables in a shared theme file.
2. Keep STT class names as compatibility layer for existing scripts.
3. Build new sections using STT palettes, card borders, and textured backgrounds.
4. Add additional textures/images through new variables, not per-selector literals.
5. Keep research-domain colors unchanged unless a full recolor pass is approved.

## Missing Information / TODO Comments
1. TODO: Confirm final global font stack for non-STT pages (keep Arimo or upgrade).
2. TODO: Confirm icon/texture licensing constraints before broad reuse outside STT.
3. TODO: `assets/fonts/Symbola.ttf` is referenced but file is currently missing in STT path.
4. TODO: Define responsive breakpoints and mobile behavior for top tab bar overflow.
5. TODO: Decide whether analytics block in `body.html` lines 67-72 should remain in global shell.
6. TODO: Define preferred contrast/accessibility targets for future recolor work.
7. TODO: Define image mapping contract for `GFX_*` picture keys in search results UI.
8. TODO: Confirm if right-button JS-generated gradient style should become pure CSS tokens.
9. TODO: Decide if legacy fallback route list UI should stay, or always hard-load chosen route.

## Known Issues Worth Tracking
1. `tech-tree.css` line 362 contains a stray `]` in `.anomaly div.node-status` block.
2. Style tokens are duplicated between CSS and JS, which can drift over time.

