import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Text
st.title('Fuel Leakages Detection')
st.header("XXX")

st.markdown(
    """
    Hello, Airbus crew! We're excited to welcome you to the new fuel leakages portal. 
    """
)

# Load data
data = pd.read_csv("dummy_data.csv")


# Plot number of leaks by year of occurence
fig = px.bar(data, 
        x='year', 
        y='leak', 
        labels={"year": 'Year', "leak": 'Number of Leaks'},
        title='Number of Fuel Leaks by Year')
fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [2015, 2016, 2017, 2018],
            ticktext = [2015, 2016, 2017, 2018]
            )
        )
st.plotly_chart(fig)

