"""The App."""
# pylint: skip-file
import matplotlib.pyplot as plt
import streamlit as st
from resc.wilcoxon import wilcoxon_exact_counts


def make_plot(n_observations):
    exact_counts = wilcoxon_exact_counts(n_observations)
    x = list(range(len(exact_counts)))
    fig, ax = plt.subplots()
    ax.bar(x, exact_counts)
    return fig


st.title("Wilcoxon Exact versus Approximate")
n_observations = st.slider(
    "Number of Observations", min_value=1, max_value=25, value=1, step=1
)
fig = make_plot(n_observations)
st.pyplot(fig)
