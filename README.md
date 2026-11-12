# Idea Compass — Precomputed Vector Demo

Static GitHub Pages app for concentric-circle discovery of 70 Chinese knowledge concepts around **AI 教學系統**.

## Features

- Recursively recenter on any topic (deep dive beyond the first level)
- Near / cross-domain / distant rings, ranked by precomputed vector similarity
- Search all concepts, keep exploration history, select and combine concepts
- Offline rule/template-based Idea Mixer with copyable AI prompts
- No API keys, backend, login, cookies, or per-user LLM charges

## Deploy to GitHub Pages

1. Create a new **public** GitHub repository, e.g. `idea-compass-demo`.
2. Upload the **contents of this folder** to the root of the `main` branch (including `.github/workflows/pages.yml`, `.nojekyll` and `data/knowledge.json`).
3. In the repository open **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**.
4. Open **Actions** and verify the “Deploy Idea Compass to GitHub Pages” workflow succeeded.
5. Visit `https://YOUR-USERNAME.github.io/idea-compass-demo/` (or check Settings → Pages for the actual URL).

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Vector calculation

`data/knowledge.json` is committed and ready to use. It contains 70 curated domain concepts, 48D latent vectors and all pairwise precomputed similarity scores. To regenerate it:

```bash
pip install numpy scikit-learn
python scripts/build_vectors.py
```

**Important:** This uses *character n-gram TF-IDF + TruncatedSVD (48 dimensions)*, combining the full TF-IDF cosine score (55%) with a nonnegative SVD cosine score (45%). It is a reproducible **corpus-specific statistical vector demo**, **not a pretrained neural embedding model** and **not an OpenAI Embedding**. Distances reflect text similarity in the curated corpus and are not validated creativity scores. Visual rings show relative similarity ranks among the corpus, not a universal metric distance scale.

For a next version, replace the vector build script with an actual multilingual embedding model and keep the same `knowledge.json` data contract (`nodes` and `similarity`).

## Notes

Everything is client-side. The idea combinations are templates, not live LLM synthesis. If you host on a public repository, all concept descriptions and vectors are publicly accessible.
