import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Date': pd.date_range(start='2018-01-01', periods=5, freq='Y'),
    'Facebook': [2.2e9, 2.3e9, 2.4e9, 2.5e9, 2.6e9],
    'YouTube': [1.6e9, 1.7e9, 1.8e9, 1.9e9, 2.0e9],
    'WhatsApp': [1.5e9, 1.55e9, 1.6e9, 1.65e9, 1.7e9],
    # Add other platforms...
}

df = pd.DataFrame(data)
df_long = df.melt(id_vars=['Date'], var_name='Platform', value_name='Users')

# Create a line chart
fig = px.line(df_long, x='Date', y='Users', color='Platform')

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)