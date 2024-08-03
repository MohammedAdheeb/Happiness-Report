from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the label encoder and Random Forest model from their respective files
with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

with open('Random_Forest.pkl', 'rb') as file:
    random_forest_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    year = int(data.get('year'))
    country = str(data.get('country'))
    
    GDP_per_Capita = float(data.get('GDP per Capita'))
    Social_Support = float(data.get('Social Support'))
    Healthy_life_expectancy = float(data.get('Healthy life expectancy'))
    Freedom_to_make_life_choices = float(data.get('Freedom to make life choices'))
    Generosity = float(data.get('Generosity'))
    Perceptions_of_corruption = float(data.get('Perceptions of corruption'))
    
    country_encoded = label_encoder.transform([country])[0]
    GDP_Social_Support = GDP_per_Capita * Social_Support
    Health_Freedom = Healthy_life_expectancy * Freedom_to_make_life_choices
    Log_GDP_per_Capita = np.log(GDP_per_Capita + 1)
    Log_Healthy_life_expectancy = np.log(Healthy_life_expectancy + 1)
    
    input_data = pd.DataFrame({
        'GDP_Social_Support': [GDP_Social_Support],
        'Health_Freedom': [Health_Freedom],
        'Log_GDP_per_Capita': [Log_GDP_per_Capita],
        'Log_Healthy_life_expectancy': [Log_Healthy_life_expectancy],
        'country_encoded': [country_encoded]
    })
    
    # Specify the features for prediction
    features = [
        'GDP_Social_Support', 'Health_Freedom',
        'Log_GDP_per_Capita', 'Log_Healthy_life_expectancy',
        'country_encoded'
    ]
    
    # Make prediction
    prediction = random_forest_model.predict(input_data[features])
    result = prediction[0]
    # if the perception of corruption is greater than 0.5, the country is corrupt
    if Perceptions_of_corruption > 0.5:
        #reduce the happiness score by a percentage
        result = result - (result * 0.283)
    elif Perceptions_of_corruption < 0.5:
        #increase the happiness score by a percentage
        result = result - (result * 0.05)
    
    if Generosity > 0.5:
        #increase the happiness score by a percentage
        result = result + (result * 0.05)
    elif Generosity < 0.5:
        #reduce the happiness score by a percentage
        result = result + (result * 0.02)
    
    # Return the prediction as a JSON response
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)