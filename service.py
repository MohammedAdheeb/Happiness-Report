from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the label encoder and Random Forest model from their respective files
with open('country_encoder.pkl', 'rb') as file:
    country_encoder = pickle.load(file)

with open('model.pkl', 'rb') as file:
    random_forest_model = pickle.load(file)

def predict_happiness_score(input_data: pd.DataFrame):
    """
    This function takes a DataFrame of input values, encodes the 'Country' column using the saved LabelEncoder,
    and returns the predicted Happiness Score using the XGBoost regressor model.

    """

    # Encode the 'Country' column
    input_data['Country'] = country_encoder.transform(input_data['Country'])

    # Make predictions using the XGBoost model
    predictions = random_forest_model.predict(input_data)

    return predictions[0]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    country = [str(data.get('Country'))]
    GDP_per_Capita = [float(data.get('Economy (GDP per Capita)'))]
    Healthy_life_expectancy = [float(data.get('Health (Life Expectancy)'))]
    Freedom_to_make_life_choices = [float(data.get('Freedom'))]
    Generosity = [float(data.get('Generosity'))]
    Perceptions_of_corruption = [float(data.get('Trust (Government Corruption)'))]
    sample_input = pd.DataFrame({
    'Country': country,  # Replace with actual country names
    'Economy (GDP per Capita)': GDP_per_Capita,
    'Health (Life Expectancy)': Healthy_life_expectancy,
    'Freedom': Freedom_to_make_life_choices,
    'Trust (Government Corruption)': Perceptions_of_corruption,
    'Generosity': Generosity,
    # Add other features as needed
    })
    predicted_scores = predict_happiness_score(sample_input)
    

    
    # Return the prediction as a JSON response
    return jsonify({"prediction": predicted_scores})

if __name__ == '__main__':
    app.run(debug=True)