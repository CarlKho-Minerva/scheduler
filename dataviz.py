import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time

# Your actual data
data = {
    'Facebook': [2.2e9, 2.3e9, 2.4e9, 2.5e9, 2.6e9],
    'YouTube': [1.6e9, 1.7e9, 1.8e9, 1.9e9, 2.0e9],
    'WhatsApp': [1.5e9, 1.55e9, 1.6e9, 1.65e9, 1.7e9],
    # Add other platforms...
}

fig, ax = plt.subplots()

max_x = len(data['Facebook'])  # Number of data points
max_y = max(max(data.values()))  # Maximum y-value in your data

x = np.arange(0, max_x)
ax.set_ylim(0, max_y)
line, = ax.plot(x, data['Facebook'])  # Start with Facebook data
the_plot = st.pyplot(plt)

def init():  # give a clean slate to start
    line.set_ydata([np.nan] * len(x))

def animate(i):  # update the y values (every 1000ms)
    platform = list(data.keys())[i % len(data)]  # Cycle through platforms
    line.set_ydata(data[platform])  # Update y-values with platform data
    ax.set_title(platform)  # Update title with current platform
    the_plot.pyplot(plt)

init()
for i in range(100):
    animate(i)
    time.sleep(0.1)