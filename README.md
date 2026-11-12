# Idea Compass v5 — GitHub Pages Demo

A zero-backend, no-API-key, static Traditional Chinese interactive knowledge exploration website.

## Run locally

Open `index.html` in a modern browser. All files are static; no build step is required.

## Publish on GitHub Pages

1. Upload `index.html`, `app.js`, and `data.js` to the **root** of the `kevcltsai/idea-compass-demo` repository (replace existing `index.html` if necessary).
2. In GitHub repository **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/(root)**, then **Save**.
3. Visit `https://kevcltsai.github.io/idea-compass-demo/` after Pages publishes.

Alternatively, if the repository already uses a GitHub Actions Pages deployment workflow, keep that workflow and commit these files to the published branch/directory.

## Features

- 10 curated demo topics
- 340 knowledge nodes total, 3 levels per topic (6 first-level, 24 second-level, 24 third-level)
- Editable demonstration radius, interactive SVG, knowledge-center navigation, breadcrumb history
- Cross-branch collection and N-to-1 rule-based synthesis with 3 solution archetypes
- Browser-local persistence, text export, responsive desktop/mobile layout

## Important limitations

- The displayed radial distances are **editorial demonstration values**, not actual embedding distances.
- Knowledge links are curated tree branches; this is not a live graph/vector search engine.
- Synthesis uses deterministic templates, **not** a live LLM. Different selected knowledge items feed into the displayed mechanisms, but the output is not independently validated research.
- No backend, API key, tracking, or paid hosting dependency is needed.

## Files

- `index.html`: layout and CSS
- `data.js`: topics and curated knowledge nodes
- `app.js`: exploration and synthesis logic
