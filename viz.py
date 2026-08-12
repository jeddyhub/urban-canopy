"""Figure helpers: consistent colours, scales, and basemaps."""


def choropleth(gdf, column, ax=None, **kwargs):
    """Standard-styled choropleth used across all figures."""
    raise NotImplementedError


def allocation_map(gdf, allocation, ax=None):
    """Map trees allocated per block group on a shared colour scale."""
    raise NotImplementedError
