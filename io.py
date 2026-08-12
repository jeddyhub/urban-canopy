"""Paths and loading helpers.

Every notebook imports paths from here rather than hard-coding them, so the
project works no matter which directory you launched Jupyter from.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
PROCESSED = DATA / "processed"
FIGURES = ROOT / "figures"
REPORTS = ROOT / "reports"

#: Projected CRS used for all area and distance computation.
#: NAD83 / Colorado Central (metres). Verify against the city's published CRS.
CRS_PROJECTED = 26953


def load_analysis_table():
    """Return the processed one-row-per-block-group table."""
    import geopandas as gpd
    return gpd.read_file(PROCESSED / "analysis_table.gpkg")
