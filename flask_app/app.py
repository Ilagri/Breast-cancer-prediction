from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model and dataset
model = joblib.load('model.pkl')  # Assuming you saved your model as model.pkl
data = pd.read_csv('data/dataset.csv')  # Assuming your dataset is stored in data/dataset.csv

@app.route('/')
def home():
    return render_template('home.html', title='Breast Cancer Prediction')

@app.route('/predict', methods=['GET'])
def predict():
    # Here, you would prepare the data and make predictions.
    # For demonstration, let's assume you're predicting on the first row of the dataset:
    prediction = model.predict([data.iloc[0]])  # Replace with actual data preparation logic

    return render_template('predict.html', title='Prediction', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
