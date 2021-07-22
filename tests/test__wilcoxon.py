"""
Tests resc._wilcoxon
"""
from resc._wilcoxon import (
    wilcoxon_counts,
    wilcoxon_counts_matrix,
    wilcoxon_table,
)


def test_wilcoxon_counts():
    """Tests wilcoxon_distribution."""
    assert wilcoxon_counts(1) == [1, 1]
    assert wilcoxon_counts(2) == [1, 1, 1, 1]
    assert wilcoxon_counts(3) == [1, 1, 1, 2, 1, 1, 1]


def test_wilcoxon_counts_matrix():
    """Tests wilcoxon_distribution."""
    assert wilcoxon_counts_matrix(1) == [1, 1]
    assert wilcoxon_counts_matrix(2) == [1, 1, 1, 1]
    assert wilcoxon_counts_matrix(3) == [1, 1, 1, 2, 1, 1, 1]


def test_wilcoxon_table():
    """Tests wilcoxon_table."""
    assert wilcoxon_table(3) == {1: [1, 1], 2: [1, 1, 1, 1], 3: [1, 1, 1, 2, 1, 1, 1]}
