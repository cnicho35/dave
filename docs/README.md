# Robotics World for Marine Energy Documentation

This directory contains the MkDocs source for the Robotics World for Marine Energy documentation. Markdown source files are in `src/`; generated site output is written to `docs/` according to `mkdocs.yml`.

Build the local documentation site with:
```bash
cd docs
mkdocs gh-deploy
mkdocs build --strict

You can also test the webpage build with `mkdocs serve`.
Preview it locally with:
Please visit our Github Organization for access to the MODAQ 2 code: https://github.com/MODAQ2
```bash
cd docs
mkdocs serve
```

Use the deployment process configured for this repository when publishing the site.
```bash


conda activate mkdocs-env
