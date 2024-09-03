from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model and dataset
model = joblib.load('model.pkl')  # Assuming you saved your model as model.pkl
data = pd.read_csv('data/breast_cancer_wisconsin_dataset.csv')  # Assuming your dataset is stored in data/dataset.csv

@app.route('/')
def home():
    return render_template('home.html', title='Breast Cancer Prediction')

@app.route('/predict', methods=['GET'])
def predict():
    # Ensure you only select the features used during training
    features = data.drop(columns=['ID', 'Diagnosis'])  # Drop any non-feature columns
    prepared_data = features.iloc[0].values.reshape(1, -1)  # Prepare the first row for prediction
    
    # Make the prediction
    prediction = model.predict(prepared_data)  # Replace with actual data preparation logic
    
    return render_template('predict.html', title='Prediction', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
