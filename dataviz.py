import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Assuming the 'Priority' column represents the inverse of task urgency (lower is more urgent)
# and 'Count' somehow represents task progress or another metric for visualization.

# Create a custom dataset with 8 tasks, simulating a scheduling scenario
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
selected_tasks = st.multiselect('Which task would you like to see?', task_options, ['Task {}'.format(i+1) for i in range(8)])

# Filter the DataFrame based on the selected tasks
filtered_df = df[df['Task'].isin(selected_tasks)]

# Create an animated horizontal bar chart
# This animation will now represent the 'execution' of tasks based on their priority
fig = px.bar(filtered_df, y="Task", x="Count", color="Task", orientation='h',
             animation_frame="Priority", animation_group="Task")

# Update the layout of the plot to improve visualization
fig.update_layout(
    width=800,
    height=600,
    showlegend=False,
    xaxis_range=[0,1],  # Ensure the x-axis starts at 0
    updatemenus=[{
        "type": "buttons",
        "buttons": [{
            "label": "Play",
            "method": "animate",
            "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}]
        }]
    }]
)

# Display the plot in Streamlit
st.write(fig)
