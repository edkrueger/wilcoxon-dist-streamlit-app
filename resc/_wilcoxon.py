"""
Some math functions.
"""

import itertools
import numpy as np


def wilcoxon_counts(n_observations):
    """
    Gives the Wilcoxon distribution.
    Similar to the Scipy implementation, but roughly half as fast
    and a little easier to understand.

    Args:
        n_observations: number of observations.
    Returns:
        A list representing the distribution, where the value for an index is the count.
        """
    ranks = np.arange(n_observations) + 1
    possibilities = itertools.product((0, 1), repeat=n_observations)
    statistics = []
    for possibility in possibilities:
        statistic = np.sum(possibility * ranks)
        statistics.append(statistic)
    _, distribution = np.unique(statistics, return_counts=True)
    return list(distribution)


def wilcoxon_counts_matrix(n_observations):
    """
    Gives the Wilcoxon distribution.
    Similar to the Scipy implementation, but roughly twice as fast.

    Args:
        n_observations: number of observations.
    Returns:
        A list representing the distribution, where the value for an index is the count.
    """
    ranks = np.arange(n_observations) + 1
    possibilities = np.array(list(itertools.product((0, 1), repeat=n_observations)))
    statistics = possibilities.dot(ranks)
    _, distribution = np.unique(statistics, return_counts=True)

    return list(distribution)


def wilcoxon_table(max_n_observations):
    """
    Gives the Wilcoxon table up to max_n_observations.

    Args:
        max_n_observations: max number of observations.
    Returns:
        A dictionary with number of observations as the key.
        and a list representing the distribution as the value.
        The lists representing the distribution have the value for an index is the count.
    """
    return {
        n_observations: wilcoxon_counts_matrix(n_observations)
        for n_observations in range(1, max_n_observations + 1)
    }
