# Inflation Predictor ML Project Using Flask – Predict Inflation Rates with Machine Learning

![image](https://github.com/dmsLakmal/Inflation-Predictor-ML-Flask-App/assets/143265507/4ec045b8-68d9-41e8-b09d-c4c0b9f10eea)

## Overview
The Inflation Predictor ML Flask Web App is designed to predict the inflation rate based on key economic indicators such as GDP and the unemployment rate. This project leverages machine learning techniques to provide an interactive web-based tool for economic forecasting and analysis.

## Workflow

1. **Data Collection**: Collect historical data on GDP, unemployment rates, and inflation rates.
2. **Data Preprocessing**: Clean and normalize the data to prepare it for model training.
3. **Model Training**: Train a neural network model using the preprocessed data.
4. **Model Evaluation**: Evaluate the model's performance using metrics like mean squared error (MSE) and R² score.
5. **Model Deployment**: Deploy the trained model using a Flask web application, allowing users to input new data and receive predictions.

## Flask

Flask is a lightweight web framework for Python that is used to build web applications. It is designed to be simple and easy to use, making it ideal for small to medium-sized projects. Flask provides the necessary tools to set up web routes, handle HTTP requests, and integrate with machine learning models.

## Architecture

The architecture of the Inflation Predictor ML Flask Web App consists of the following components:

1. **Frontend**: A simple web interface built using HTML and CSS, allowing users to input economic indicators and receive predicted inflation rates.
2. **Backend**: A Flask application that handles user input, processes data, and serves the prediction results. The backend integrates the trained machine learning model to generate predictions.
3. **Model**: A neural network model trained using TensorFlow/Keras, which is responsible for predicting the inflation rate based on input features.
4. **Data Storage**: The dataset used for training the model is stored in CSV format, and the trained model is saved as an HDF5 file. The scaler used for data normalization is saved using the pickle module.

## Libraries Used

The following libraries are used in this project:

1. **Pandas**: For data manipulation and analysis.
2. **Scikit-learn**: For data preprocessing, model evaluation, and splitting the dataset.
3. **TensorFlow/Keras**: For building and training the neural network model.
4. **Pickle**: For saving and loading the scaler object.
5. **Flask**: For creating the web application.

## Setup Instructions

To set up and run the Inflation Predictor ML Flask Web App, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/inflation-predictor-ml-flask.git
   cd inflation-predictor-ml-flask

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask App**:
   ```sh
   python app.py
   ```

5. **Access the Web App**:
  Open your web browser and navigate to ``` http://127.0.0.1:8000 ``` to access the Inflation Predictor ML Flask Web App.

## Conclusion
This project presents a basic machine learning model for predicting the inflation rate, implemented as a prototype using Flask. While it demonstrates the potential of using economic indicators such as GDP and the unemployment rate for forecasting inflation, it is not accurate enough for real-world applications. To predict the actual inflation rate with higher accuracy, more comprehensive data and a more sophisticated model would be required. This prototype serves as a foundational step towards developing a robust inflation prediction tool, highlighting the need for further data collection and model refinement.

## Accessing the Model Creation Repository

For those interested in the model creation aspect of this project, you can access the repository containing the model creation code and assets using the following 
link: [Inflation Predictor Model Repository](https://github.com/dmsLakmal/InflationPredictorModel.git).
