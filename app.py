

from flask import Flask, request, render_template, flash, redirect, url_for
import pickle
import numpy as np
from tensorflow import keras

# Load the model
model = keras.models.load_model('model.h5')

# Load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        gdp = request.form['gdp']
        unemployment = request.form['unemployment']
        
        # Validation
        if not gdp or not unemployment:
            flash('Please enter both GDP and Unemployment Rate', 'error')
            return redirect(url_for('home'))
        
        try:
            gdp = float(gdp)
            unemployment = float(unemployment)
        except ValueError:
            flash('Please enter valid numbers for GDP and Unemployment Rate', 'error')
            return redirect(url_for('home'))
        
        # Scale the input features
        input_features = scaler.transform([[gdp, unemployment]])
        
        # Make prediction
        prediction = model.predict(input_features)
        inflation = prediction[0][0]
        
        # Determine if the inflation rate is good or bad
        if inflation < 2:
            status = "Good"
        else:
            status = "Bad"
        
        return render_template('result.html', inflation=inflation, status=status)

if __name__ == '__main__':
    app.run(debug=True)
