import streamlit as st
import plotly.express as px
import pandas as pd

# Load the Gapminder dataset
df = px.data.gapminder()

# Display the dataset in Streamlit
st.write(df)

# Create a select box in Streamlit for year selection
year_options = df['year'].unique().tolist()
year = st.selectbox('Which year would you like to see?', year_options, 0)

# Create an animated scatter plot
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90], animation_frame="year", animation_group="country")

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

# Load the COVID-19 dataset
covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Code', 'Date', 'Confirmed', 'Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')

# Display the COVID-19 dataset in Streamlit
st.write(covid)

# Create select boxes in Streamlit for date and country selection
date_options = covid['Date'].unique().tolist()
date = st.selectbox('Which date would you like to see?', date_options, 100)
country_options = covid['Country'].unique().tolist()
country = st.multiselect('Which country would you like to see?', country_options, ['Brazil'])

# Filter the COVID-19 dataset based on the selected countries
covid = covid[covid['Country'].isin(country)]

# Create an animated bar chart
fig2 = px.bar(covid, x="Country", y="Confirmed", color="Country", range_y=[0,35000], animation_frame="Date", animation_group="Country")

# Update the layout of the plot to include a 'Play' button
fig2.update_layout(
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
st.write(fig2)