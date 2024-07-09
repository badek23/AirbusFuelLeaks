import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Airbus Fuel Leakages✈️")
st.title('Fuel Leakages Detection')
st.markdown(
    """
    Hello, Airbus crew! We're excited to welcome you to the new fuel leakages portal. 
    """
)

# Load the dataset
combined_leaks = pd.read_csv('data/combined_leaks.csv')

# Function to determine if a flight has a leakage
def has_leakage(flight_data):
    return flight_data['FAKE_LEAKAGE'].notnull().any()

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Summary Page", "Flight Details"])

if page == "Summary Page":
    
    st.markdown(
    """
    First, a quick summary of leakages across our fleet. 
    """
    )

    # Get unique flights and their leakage status
    flight_ids = combined_leaks['Flight'].unique()
    leakage_status = [has_leakage(combined_leaks[combined_leaks['Flight'] == flight]) for flight in flight_ids]

    # Create a dataframe for display
    summary_df = pd.DataFrame({
        'Flight ID': flight_ids.round().astype("str"),
        'Leakage Status': ['Leakage Detected' if status else 'OK' for status in leakage_status]
    })
    
    # Add a color indicator
    def color_leakage(val):
        color = 'red' if val == 'Leakage Detected' else 'green'
        return f'background-color: {color}'
    
    st.dataframe(summary_df.style.applymap(color_leakage, subset=['Leakage Status']), width=400)

elif page == "Flight Details":
    st.markdown(
    """
    Next, let's look at flight details and a leakage analysis. 
    """
    )
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
        fig = px.line(flight_data, x='UTC_TIME', y=['VALUE_FOB', 'FAKE_LEAKAGE'],
                    labels={'value': 'Fuel (kg)', 'UTC_TIME': 'Time'},
                    title=f'Trend of Fuel Usage with Simulated Leakage for Flight {flight_id}')
        fig.update_layout(legend_title_text='Fuel Metrics')
        st.plotly_chart(fig)
        
        # Display the data table
        st.write('Data Table')
        st.write(flight_data)

# Save the dataframe to a new CSV file
combined_leaks.to_csv('combined_leaks_updated.csv', index=False)