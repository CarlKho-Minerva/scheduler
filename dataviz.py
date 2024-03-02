import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def create_data(n_tasks):
    data = {
        'Task': ['Task {}'.format(i+1) for i in range(n_tasks) for _ in range((i+1)*10)],
        'Priority': [j+1 for i in range(n_tasks) for j in range((i+1)*10)],
        'Count': [np.linspace(0, 1, (i+1)*10) for i in range(n_tasks) for _ in range((i+1)*10)]
    }
    return pd.DataFrame(data)

df = create_data(8)

st.write(df)

task_options = df['Task'].unique().tolist()
task = st.multiselect('Which task would you like to see?', task_options, ['Task {}'.format(i+1) for i in range(8)])

df = df[df['Task'].isin(task)]

fig = px.bar(df, y="Task", x="Count", color="Task", orientation='h', animation_frame="Priority", animation_group="Task")

fig.update_layout(
    width=800,
    showlegend=True,
    xaxis_range=[0,1],
    updatemenus=[{
        "type": "buttons",
        "buttons": [{
            "label": "Play",
            "method": "animate",
            "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}]
        }]
    }]
)

st.write(fig)