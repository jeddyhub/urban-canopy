# Denver Canopy Equity

**Question.** Given a fixed annual tree-planting budget, where should Denver
plant — and how much aggregate benefit does the city give up in order to
distribute canopy more equitably?

The city's Urban Forest Strategic Plan sets a minimum canopy target and names
equity as a goal, but a target is not an allocation. This project turns the
target into a decision problem, solves it under several competing definitions of
"fair," and quantifies the trade-off between them.

## Status

Scaffold only. Notebooks contain the plan and the model specification; the
implementation is the work.

## Setup

```bash
git clone <your-repo-url> && cd denver-canopy-equity

# Conda (recommended — handles the GDAL/GEOS/PROJ C libraries for you)
conda env create -f environment.yml
conda activate canopy

# Register the kernel so JupyterLab can see this environment
python -m ipykernel install --user --name canopy --display-name "Python (canopy)"

# Strip notebook outputs on commit, so diffs stay readable
nbstripout --install

jupyter lab
```

`environment.yml` installs this repo in editable mode (`pip: -e .`), which is
what lets a notebook run `from canopy.io import RAW` without any `sys.path`
manipulation.

### Census API key

Request one at https://api.census.gov/data/key_signup.html, then create a `.env`
file in the repo root:

```
CENSUS_API_KEY=your_key_here
```

`.env` is gitignored. Never commit a key.

## Layout

```
denver-canopy-equity/
├── README.md              you are here
├── environment.yml        exact dependency list — the reproducibility contract
├── pyproject.toml         makes src/canopy an importable package
├── .gitignore             keeps data and secrets out of version control
├── data/
│   ├── README.md          data dictionary: source and retrieval date per file
│   ├── raw/               downloaded, immutable, gitignored
│   ├── interim/           partially processed
│   └── processed/         the single analysis table everything downstream reads
├── notebooks/             numbered, run in order, each with one job
│   ├── 00_get_data.ipynb
│   ├── 01_build_analysis_table.ipynb
│   ├── 02_explore.ipynb
│   ├── 03_optimize_baseline.ipynb
│   ├── 04_fairness_frontier.ipynb
│   └── 05_report_figures.ipynb
├── src/canopy/            functions promoted out of notebooks once reused
│   ├── io.py              paths and loaders
│   ├── prep.py            geometry cleaning, overlay, aggregation
│   ├── model.py           the optimisation models
│   └── viz.py             figure styling
├── tests/                 tiny hand-checkable instances for the models
├── figures/               generated output — safe to delete and regenerate
└── reports/               written findings
```

## The model

Block groups indexed by *b*. Decision variable *x_b* ∈ ℤ≥0 is trees planted in
*b*. With area *A_b*, current canopy fraction *s_b*, population *p_b*, capacity
*k_b*, unit cost *c_b*, crown area *a*, and budget *C*, post-planting canopy is

&nbsp;&nbsp;&nbsp;&nbsp;*f_b(x) = s_b + a·x_b / A_b*

subject to Σ *c_b x_b* ≤ *C* and 0 ≤ *x_b* ≤ *k_b*. Three objectives are solved
and compared:

| Objective | Form | Type |
|---|---|---|
| Utilitarian | max Σ *p_b* · *a x_b / A_b* | LP / ILP |
| Rawlsian | max min_b *f_b(x)* | LP / ILP |
| Inequality-averse | max Σ *p_b* *U_ε*(*f_b(x)*), *U_ε* isoelastic | LP via piecewise-linear envelope |

The parameter ε interpolates between the first two. The headline result is the
**price of fairness** curve: utilitarian welfare forgone as a function of the
equity achieved.

## Known limitations

- The public tree inventory covers city-managed trees only; private canopy is
  visible in the canopy layer but not attributable to owners.
- Block-group aggregation invites the modifiable areal unit problem. Results
  should be checked at a second spatial resolution.
- Crown area and planting capacity are estimated, not measured. Sensitivity
  analysis is part of the deliverable, not an optional extra.
- Planting a tree is not the same as a tree surviving to maturity; mortality is
  not modelled.

## Data sources

- Denver Open Data — tree canopy (2014, 2020), tree inventory, neighborhoods
- U.S. Census — TIGER/Line block groups, ACS 5-year estimates
- Denver Urban Forest Strategic Plan (2024) — targets and policy context
