import pickle
from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load the scaler and ridge model
try:
    scaler_model = pickle.load(open('model/scaler.pkl', 'rb'))
    ridge_model = pickle.load(open('model/ridge.pkl', 'rb'))
    print("Models loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

# Routing for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Routing for the predict page
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Extracting form data
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))

            # Creating a DataFrame for the input data
            input_data = pd.DataFrame({
                'Temperature': [Temperature],
                'RH': [RH],
                'Ws': [Ws],
                'Rain': [Rain],
                'FFMC': [FFMC],
                'DMC': [DMC],
                'ISI': [ISI],
                'Classes': [Classes],
                'Region': [Region]
            })

            # Scaling the input data
            scaled_data = scaler_model.transform(input_data)
            print("Data scaled successfully")

            # Making a prediction
            prediction = ridge_model.predict(scaled_data)
            print(f"Prediction: {prediction}")

            # Returning the result
            return jsonify({'prediction': prediction[0]})
        except Exception as e:
            print(f"Error during prediction: {e}")
            return jsonify({"error": "An error occurred during prediction. Please try again."}), 500
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
