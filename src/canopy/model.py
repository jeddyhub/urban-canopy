"""Optimisation models.

Each function builds and solves one variant and returns the allocation.
Keeping them here (rather than in a notebook) means notebook 04 can call the
same code notebook 03 validated.
"""


def solve_utilitarian(table, budget, cost, crown_area):
    """Maximise population-weighted canopy gain subject to budget and capacity."""
    raise NotImplementedError


def solve_maxmin(table, budget, cost, crown_area):
    """Maximise the minimum post-planting canopy fraction."""
    raise NotImplementedError


def solve_isoelastic(table, budget, cost, crown_area, epsilon, n_breakpoints=12):
    """Maximise an inequality-averse (isoelastic) welfare function.

    Uses a piecewise-linear upper envelope of the concave utility, so the
    problem stays an LP/ILP.
    """
    raise NotImplementedError


def price_of_fairness(alloc, utilitarian_optimum, table, crown_area):
    """Relative utilitarian welfare given up by ``alloc``."""
    raise NotImplementedError


def gini(values, weights=None):
    """Gini coefficient of a distribution, optionally population-weighted."""
    raise NotImplementedError
