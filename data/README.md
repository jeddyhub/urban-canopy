# Data dictionary

`data/raw/` is **immutable**. Download into it, never write to it. If a file
needs fixing, fix it in a notebook and write the result to `interim/` or
`processed/`.

| File | Level | Source | Retrieved | Notes |
|---|---|---|---|---|
| `tree_canopy_2020.geojson` | polygon | Denver Open Data | | |
| `tree_canopy_2014.geojson` | polygon | Denver Open Data | | |
| `tree_inventory.geojson` | point | Denver Open Data | | Public trees only |
| `block_groups_2020.geojson` | polygon | Census TIGER/Line | | |
| `acs_blockgroups.csv` | table | Census ACS 5-year | | |
| `neighborhoods.geojson` | polygon | Denver Open Data | | |

Fill in the *Retrieved* column with the date you downloaded each file. Open data
portals update layers silently; without a date, a result you can't reproduce in
six months has no explanation.

## Derived files

| File | Built by | Contents |
|---|---|---|
| `processed/analysis_table.gpkg` | `notebooks/01` | One row per block group: geometry, canopy fraction, demographics, planting capacity |
