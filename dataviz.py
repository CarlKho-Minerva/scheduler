import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Create a custom dataset with 8 tasks
data = {
    'Task': sum([['Task {}'.format(i+1)]*((i+1)*10) for i in range(8)], []),
    'Priority': sum([list(range(1, (i+1)*10 + 1)) for i in range(8)], []),
    'Count': sum([list(np.linspace(0, 1, (i+1)*10)) for i in range(8)], [])
}
df = pd.DataFrame(data)

# Display the dataset in Streamlit
st.write(df)

# Create select boxes in Streamlit for task selection
task_options = df['Task'].unique().tolist()
task = st.multiselect('Which task would you like to see?', task_options, ['Task {}'.format(i+1) for i in range(8)])

# Filter the DataFrame based on the selected tasks
df = df[df['Task'].isin(task)]

# Create an animated horizontal bar chart
fig = px.bar(df, y="Task", x="Count", color="Task", orientation='h', animation_frame="Priority", animation_group="Task")

# Update the layout of the plot to include a 'Play' button and set the range of x-axis
fig.update_layout(
    width=800,
    showlegend=False,
    xaxis_range=[0,1],  # Set the range of x-axis to start from 0
    updatemenus=[{
        "type": "buttons",
        "buttons": [{
            "label": "Play",
            "method": "animate",
            "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}]
        }]
    }]
)

# https://www.youtube.com/watch?v=VZ_tS4F6P2A&t=445s

# Display the plot in Streamlit
st.write(fig)