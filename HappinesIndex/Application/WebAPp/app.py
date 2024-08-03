import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API URL from environment variables
API_URL = os.getenv('API_URL')

endpoint = "/predict" 
API_URL = API_URL + endpoint


# Streamlit app
st.title("Happiness Score Prediction")

# Year slider
year = st.slider("Select the year", min_value=2020, max_value=2050, value=2024)

# Country selection
country = st.selectbox("Select the country", ["United States", "India", "Iran"])

# Input fields
GDP_per_Capita = st.number_input("Enter the GDP per Capita", min_value=0.0, format="%.2f")
Social_Support = st.number_input("Enter the Social Support", min_value=0.0, format="%.2f")
Healthy_life_expectancy = st.number_input("Enter the Healthy life expectancy", min_value=0.0, format="%.2f")
Freedom_to_make_life_choices = st.number_input("Enter the Freedom to make life choices", min_value=0.0, format="%.2f")
Generosity = st.number_input("Enter the Generosity", min_value=0.0, format="%.2f")
Perceptions_of_corruption = st.number_input("Enter the Perceptions of corruption", min_value=0.0, format="%.2f")

# Submit button
if st.button("Predict Happiness Score"):
    # Prepare data payload
    data = {
        "year": year,
        "country": country,
        "GDP per Capita": GDP_per_Capita,
        "Social Support": Social_Support,
        "Healthy life expectancy": Healthy_life_expectancy,
        "Freedom to make life choices": Freedom_to_make_life_choices,
        "Generosity": Generosity,
        "Perceptions of corruption": Perceptions_of_corruption
    }
    
    # Send POST request to the API
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Happiness Score: {result['prediction']}")
    else:
        st.error("Error in API call")


