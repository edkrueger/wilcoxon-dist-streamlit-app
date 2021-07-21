"""
Tests resc.py.
"""
from resc.wilcoxon import wilcoxon_distribution  # pylint: disable=import-error


def test_wilcoxon_distribution():
    """Tests wilcoxon_distribution."""
    assert wilcoxon_distribution(1) == [1, 1]
    assert wilcoxon_distribution(2) == [1, 1, 1, 1]
    assert wilcoxon_distribution(3) == [1, 1, 1, 2, 1, 1, 1]
