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
country = st.selectbox("Select the country", ['Switzerland', 'Iceland', 'Denmark', 'Norway', 'Canada', 'Finland',
       'Netherlands', 'Sweden', 'New Zealand', 'Australia', 'Israel',
       'Costa Rica', 'Austria', 'Mexico', 'United States', 'Brazil',
       'Luxembourg', 'Ireland', 'Belgium', 'United Arab Emirates',
       'United Kingdom', 'Venezuela', 'Singapore', 'Panama', 'Germany',
       'Chile', 'France', 'Argentina', 'Uruguay', 'Colombia', 'Thailand',
       'Saudi Arabia', 'Spain', 'Malta', 'El Salvador', 'Guatemala',
       'Uzbekistan', 'Slovakia', 'Japan', 'South Korea', 'Ecuador',
       'Bahrain', 'Italy', 'Bolivia', 'Moldova', 'Paraguay', 'Kazakhstan',
       'Slovenia', 'Lithuania', 'Nicaragua', 'Peru', 'Poland', 'Malaysia',
       'Croatia', 'Russia', 'Jamaica', 'Cyprus', 'Algeria', 'Kosovo',
       'Mauritius', 'Estonia', 'Indonesia', 'Vietnam', 'Kyrgyzstan',
       'Nigeria', 'Pakistan', 'Jordan', 'Montenegro', 'China', 'Zambia',
       'Romania', 'Serbia', 'Portugal', 'Latvia', 'Philippines',
       'Morocco', 'Albania', 'Bosnia and Herzegovina',
       'Dominican Republic', 'Mongolia', 'Greece', 'Lebanon', 'Hungary',
       'Honduras', 'Tajikistan', 'Tunisia', 'Bangladesh', 'Iran',
       'Ukraine', 'Iraq', 'South Africa', 'Ghana', 'Zimbabwe', 'Liberia',
       'India', 'Nepal', 'Ethiopia', 'Sierra Leone', 'Mauritania',
       'Kenya', 'Armenia', 'Botswana', 'Myanmar', 'Georgia', 'Malawi',
       'Sri Lanka', 'Cameroon', 'Bulgaria', 'Egypt', 'Mali', 'Uganda',
       'Senegal', 'Gabon', 'Niger', 'Cambodia', 'Tanzania', 'Madagascar',
       'Chad', 'Guinea', 'Ivory Coast', 'Burkina Faso', 'Afghanistan',
       'Benin', 'Togo'])

# Input fields
# Define the slider ranges
GDP_per_Capita = st.slider(
    "Enter the GDP per Capita", 
    min_value=0.0, 
    max_value=100.0,  # Example max value, adjust as needed
    value=0.0,  # Default value
    step=0.01,  # Step size for increments
    format="%.2f"
)

Social_Support = st.slider(
    "Enter the Social Support", 
    min_value=0.0, 
    max_value=1.0,  # Example max value, adjust as needed
    value=0.0,  # Default value
    step=0.01,  # Step size for increments
    format="%.2f"
)

Healthy_life_expectancy = st.slider(
    "Enter the Healthy life expectancy", 
    min_value=0.0, 
    max_value=100.0,  # Example max value, adjust as needed
    value=0.0,  # Default value
    step=0.01,  # Step size for increments
    format="%.2f"
)

Freedom_to_make_life_choices = st.slider(
    "Enter the Freedom to make life choices", 
    min_value=0.0, 
    max_value=1.0,  # Example max value, adjust as needed
    value=0.0,  # Default value
    step=0.01,  # Step size for increments
    format="%.2f"
)

Generosity = st.slider(
    "Enter the Generosity", 
    min_value=0.0, 
    max_value=1.0,  # Example max value, adjust as needed
    value=0.0,  # Default value
    step=0.01,  # Step size for increments
    format="%.2f"
)

Perceptions_of_corruption = st.slider(
    "Enter the Perceptions of corruption", 
    min_value=0.0, 
    max_value=1.0,  # Example max value, adjust as needed
    value=0.0,  # Default value
    step=0.01,  # Step size for increments
    format="%.2f"
)

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


