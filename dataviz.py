import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Create a custom dataset with 8 tasks
data = {
    'Task': ['Task {}'.format(i+1) for i in range(8)],
    'Priority': list(range(1, 9)),
    'Count': list(np.linspace(0, 1, 8))
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

# Display the plot in Streamlit
st.write(fig)