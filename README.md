[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16945588.svg)](https://doi.org/10.5281/zenodo.16945588)

# Clogging paper code

This repository contains notebooks, data, and helper code to reproduce figures and analyses for the riverbed clogging paper.

## Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# Optional: strip notebook outputs from commits
nbstripout --install
```

## Notebooks
- `notebooks/Final_Version_With_Summary.ipynb`
- `notebooks/Publication_MetaAnalysis_charts.ipynb`

## Paths
Code reads and writes relative to the repository. See `src/paths.py`.
