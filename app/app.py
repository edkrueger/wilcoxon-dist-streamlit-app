"""The App."""
# pylint: skip-file
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from resc.wilcoxon import wilcoxon_approximate_mu_sigma, wilcoxon_exact_counts
from scipy.stats import norm


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
    approx_x = np.linspace(approx_x_min, approx_x_max, 100)
    approx_distribution = norm.pdf(approx_x, mu, sigma)

    fig, ax = plt.subplots()
    ax.bar(exact_x, exact_distribution)
    ax.plot(approx_x, approx_distribution)
    return fig


st.title("Wilcoxon Exact versus Approximate")
st.header("[Github](https://github.com/edkrueger/wilcoxon-dist-streamlit-app)")
n_observations = st.slider(
    "Number of Observations", min_value=1, max_value=25, value=1, step=1
)
fig = make_plot(n_observations)
st.pyplot(fig)
