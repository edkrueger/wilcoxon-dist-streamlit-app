"""The App."""
# pylint: disable=redefined-outer-name, too-many-locals, invalid-name
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from scipy.stats import norm
from resc.wilcoxon import wilcoxon_approximate_mu_sigma, wilcoxon_exact_counts

GITHUB_URL = "https://github.com/edkrueger/wilcoxon-dist-streamlit-app"

MU_MAX, SIGMA_MAX = wilcoxon_approximate_mu_sigma(25)
X_MIN = norm.ppf(0.01, MU_MAX, SIGMA_MAX)
X_MAX = norm.ppf(0.99, MU_MAX, SIGMA_MAX)

Y_MIN = 0
Y_MAX = 0.5

COLOR_EXACT = "#1f77b4"
COLOR_APPROX = "#ff7f0e"


@st.cache(hash_funcs={matplotlib.figure.Figure: hash})
def make_plot(n_observations):
    """Make the plot."""
    exact_counts = np.array(wilcoxon_exact_counts(n_observations))
    exact_distribution = exact_counts / exact_counts.sum()
    max_statistic = exact_counts.size
    exact_x = list(range(max_statistic))

    mu, sigma = wilcoxon_approximate_mu_sigma(n_observations)
    approx_x_min = norm.ppf(0.01, mu, sigma)
    approx_x_max = norm.ppf(0.99, mu, sigma)

    centered_approx_x = np.linspace(approx_x_min, approx_x_max, 100)
    centered_approx_distribution = norm.pdf(centered_approx_x, mu, sigma)

    fixed_approx_x = np.linspace(X_MIN, X_MAX, 100)

    fig, axes = plt.subplots(nrows=1, ncols=2)

    ax_centered = axes[1]
    ax_fixed = axes[0]

    ax_fixed.bar(exact_x, exact_distribution, label="Exact", color=COLOR_EXACT)
    # hide the approximate line on the left plot because its not rendering correctly
    ax_fixed.plot(
        fixed_approx_x,
        np.zeros(len(fixed_approx_x)),
        label="Approximate",
        color=COLOR_APPROX,
    )
    ax_fixed.legend(title="Statistic Value",)
    ax_fixed.set_ylim(Y_MIN, Y_MAX)
    ax_fixed.set_xlabel("Coordinates Fixed")

    ax_centered.bar(exact_x, exact_distribution, color=COLOR_EXACT)
    ax_centered.plot(
        centered_approx_x, centered_approx_distribution, color=COLOR_APPROX
    )
    ax_centered.set_xlabel("Distribution Centered")
    ax_centered.set_yticks([])

    fig.suptitle("Wilcoxon Exact versus Approximate")
    fig.supylabel("Probability")

    return fig


st.title("Wilcoxon Exact versus Approximate")
st.header(f"[Github]({GITHUB_URL})")
n_observations = st.slider(
    "Number of Observations", min_value=1, max_value=25, value=1, step=1
)

st.pyplot(make_plot(n_observations))
