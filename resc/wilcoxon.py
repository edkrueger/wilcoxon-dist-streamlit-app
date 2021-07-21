"""
Some math functions.
"""

import itertools
import numpy as np


def wilcoxon_distribution(n_observations):
    """
    Gives the Wilcoxon distributions.

    Args:
        n: number of observations
    Returns:
        a list representing the distribution, where the value for an index is the count
        """
    ranks = np.arange(n_observations) + 1
    possibilities = itertools.product((0, 1), repeat=n_observations)
    statistics = []
    for possibility in possibilities:
        statistic = np.sum(possibility * ranks)
        statistics.append(statistic)
    _, distribution = np.unique(statistics, return_counts=True)
    return list(distribution)
