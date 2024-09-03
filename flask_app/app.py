from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.pkl')

# Load the test dataset
X_test = pd.read_csv('data/X_test.csv')

@app.route('/')
def home():
    return render_template('home.html', title='Breast Cancer Prediction')

@app.route('/predict', methods=['GET'])
def predict():
    # Pick an arbitrary row from X_test, for example, the 10th row (index 9)
    row_index = 9  # You can change this index to select a different row
    prepared_data = X_test.iloc[row_index].values.reshape(1, -1)
    
    # Make the prediction
    prediction = model.predict(prepared_data)[0]
    
    return render_template('predict.html', title='Prediction', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

