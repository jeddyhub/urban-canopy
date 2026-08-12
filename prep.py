"""Data preparation: geometry cleaning, overlay, aggregation.

Move a function here once you have written it twice in a notebook.
"""


def canopy_fraction_by_unit(canopy, units, unit_id="GEOID"):
    """Fraction of each unit's area covered by canopy polygons.

    Parameters
    ----------
    canopy, units : geopandas.GeoDataFrame
        Must already share a projected CRS in metres.
    unit_id : str
        Column in ``units`` identifying each analysis unit.

    Returns
    -------
    pandas.Series indexed by ``unit_id``, values in [0, 1].
    """
    raise NotImplementedError


def planting_capacity(units, method="frontage"):
    """Estimate the maximum number of trees each unit can accommodate."""
    raise NotImplementedError
