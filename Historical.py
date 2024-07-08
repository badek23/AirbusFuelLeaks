import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Airbus Fuel Leakages✈️")
st.title('Fuel Leakages Detection')

st.markdown(
    """
    Hello, Airbus crew! We're excited to welcome you to the new fuel leakages portal. 
    """
)

tab1, tab2 = st.tabs(["📜Historical", "✈️Detection"])

with tab1:
    # Load data
    data = pd.read_csv("data/dummy_data.csv")

    st.markdown(
    """
    This page will be most helpful for analysts and others who want to understand historical leakage trends at Airbus. 
    """
    )  

    st.divider()
            
    # Plot number of leaks by year of occurrence
    fig = px.bar(data, 
            x='year', 
            y='leak', 
            labels={"year": 'Year', "leak": 'Number of Leaks'},
            title='Number of Fuel Leaks by Year',
            color_discrete_sequence=['#00205b'])
    fig.update_layout(
            xaxis = dict(
                tickmode = 'array',
                tickvals = [2015, 2016, 2017, 2018],
                ticktext = [2015, 2016, 2017, 2018]
                ),
            
            )
    st.plotly_chart(fig)

    st.divider()
            
    # Upload all data thus far
    combined_leaks = pd.read_csv("data/combined_leaks_dummy2.csv")
    combined_leaks["Flight"] = combined_leaks["Flight"].round()

    # Select a flight to display
    flight_id = st.selectbox('Select Flight ID', combined_leaks['Flight'].unique(), index=None)

    if flight_id is not None:
        # Filter the data for the selected flight
        flight_data = combined_leaks[combined_leaks['Flight'] == flight_id]

        # Determine if there is a leakage
        leak_detected = flight_data['FAKE_LEAKAGE'].notnull().any()

        # Display the sign at the top of the page
        if leak_detected:
            st.markdown("<h1 style='text-align: center; color: red;'>Leakage Detected</h1>", unsafe_allow_html=True)
        else:
            st.markdown("<h1 style='text-align: center; color: green;'>OK</h1>", unsafe_allow_html=True)

        # Plot the trend of fuel usage with simulated leakage
        fig1 = px.line(flight_data, x='UTC_TIME', y=['VALUE_FOB', 'FAKE_LEAKAGE'],
                    labels={'value': 'Fuel (kg)', 'UTC_TIME': 'Time'},
                    title=f'Trend of Fuel Usage with Simulated Leakage for Flight {flight_id}')
        fig1.update_layout(legend_title_text='Fuel Metrics')
        st.plotly_chart(fig1)

        # Display the data table
        st.write('Data Table')
        st.write(flight_data)



with tab2:
    st.markdown(
    """
    This page will be most helpful for maintenance crews and in-flight crew members who want to understand what's happening for a particular flight.
    """
    )

    st.divider()

    uploaded = st.file_uploader("Upload a single flight's data here.")

    if uploaded is not None:

        uploaded = pd.read_csv(uploaded)

        # Determine if there is a leakage
        leak_detected = uploaded['FAKE_LEAKAGE'].notnull().any()

        # Display the sign at the top of the page
        if leak_detected:
            st.markdown("<h1 style='text-align: center; color: red;'>Leakage Detected</h1>", unsafe_allow_html=True)
        else:
            st.markdown("<h1 style='text-align: center; color: green;'>OK</h1>", unsafe_allow_html=True)

        # Plot the trend of fuel usage with simulated leakage
        fig = px.line(flight_data, x='UTC_TIME', y=['VALUE_FOB', 'FAKE_LEAKAGE'],
                    labels={'value': 'Fuel (kg)', 'UTC_TIME': 'Time'},
                    title=f'Trend of Fuel Usage with Simulated Leakage for Flight {flight_id}')
        fig.update_layout(legend_title_text='Fuel Metrics')
        st.plotly_chart(fig)

        # Display the data table
        st.write('Data Table')
        st.write(flight_data)
