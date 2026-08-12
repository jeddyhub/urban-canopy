"""Tests for the optimisation models.

Start with tiny hand-solvable instances. If you can't predict the answer on a
three-block-group problem, you can't trust the answer on 480.
"""
import pytest


def test_maxmin_raises_the_floor():
    """On a toy instance, max-min must not leave the worst-off unit untouched."""
    pytest.skip("write me once model.solve_maxmin is implemented")
