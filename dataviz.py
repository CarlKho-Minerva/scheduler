import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Date': pd.date_range(start='2018-01-01', periods=5, freq='Y').year,
    'Facebook': [2.2e9, 2.3e9, 2.4e9, 2.5e9, 2.6e9],
    # Add other platforms...
}

df = pd.DataFrame(data)
df_long = df.melt(id_vars=['Date'], var_name='Platform', value_name='Users')

# Create an animated line chart
fig = px.line(df_long, x='Date', y='Users', color='Platform', animation_frame='Date', animation_group='Platform', range_y=[df_long['Users'].min(), df_long['Users'].max()])

# Update layout
fig.update_layout(showlegend=True, updatemenus=[{"type": "buttons", "buttons": [{"label": "Play", "method": "animate", "args": [None]}]}])

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)