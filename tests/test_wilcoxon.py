"""
Tests resc.wilcoxon.
"""
from resc.wilcoxon import wilcoxon_exact_counts


def test_wilcoxon_exact_counts():
    """Tests wilcoxon_distribution."""
    assert wilcoxon_exact_counts(1) == [1, 1]
    assert wilcoxon_exact_counts(2) == [1, 1, 1, 1]
    assert wilcoxon_exact_counts(3) == [1, 1, 1, 2, 1, 1, 1]
