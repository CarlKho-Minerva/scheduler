import streamlit as st
import plotly.express as px
import pandas as pd

# Create a custom dataset
data = {
    'Task': ['Task 1']*10 + ['Task 2']*10,
    'Priority': list(range(1, 11)) + list(range(1, 11)),
    'Count': list(range(10, 110, 10)) + list(range(10, 110, 10))
}
df = pd.DataFrame(data)

# Display the dataset in Streamlit
st.write(df)

# Create select boxes in Streamlit for task selection
task_options = df['Task'].unique().tolist()
task = st.multiselect('Which task would you like to see?', task_options, ['Task 1', 'Task 2'])

# Filter the DataFrame based on the selected tasks
df = df[df['Task'].isin(task)]

# Create an animated horizontal bar chart
fig = px.bar(df, y="Task", x="Count", color="Task", orientation='h', animation_frame="Priority", animation_group="Task")

# Update the layout of the plot to include a 'Play' button
fig.update_layout(
    width=800,
    showlegend=True,
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