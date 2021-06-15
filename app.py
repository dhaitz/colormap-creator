import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

plt.style.use("seaborn-darkgrid")

(col1, col2) = st.beta_columns(2)

n_colors = col1.number_input("Number of colors", value=2)
n_segments = col2.number_input("Number of colormap segments", value=10)

color_columns = st.beta_columns(n_colors)
colors = [col.color_picker(f"Color {i}") for i, col in enumerate(color_columns)]

cmap = LinearSegmentedColormap.from_list('my_colormap', colors, N=n_segments)

@st.cache
def get_data():
    n = 100000
    x = np.random.standard_normal(n)
    y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)

    data = np.random.randn(50, 50)

    return x, y, data


x, y, data = get_data()

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(7, 4))

hb = ax1.hexbin(x, y, gridsize=50, cmap=cmap)
ax1.set(xlim=(x.min(), x.max()), ylim=(y.min(), y.max()))
fig.colorbar(hb, ax=ax1)

pcm = ax2.pcolormesh(data, cmap=cmap, vmin=-4, vmax=4)
fig.colorbar(pcm, ax=ax2)



st.write(fig)

st.markdown(f"""
Code:

    cmap = LinearSegmentedColormap.from_list('my_colormap', {colors}, N={n_segments})
""")

st.markdown("Code for example figures from Matplotlib docs: [1](https://matplotlib.org/stable/gallery/statistics/hexbin_demo.html#sphx-glr-gallery-statistics-hexbin-demo-py), [2](https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html)")
