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
    # Pass the maximum index to the template for validation
    return render_template('home.html', title='Breast Cancer Prediction', max_index=len(X_test)-1)

@app.route('/predict', methods=['GET'])
def predict():
    # Get the row index from the request, default to 0 if not provided
    row_index = int(request.args.get('row_index', 0))
    
    # Ensure row_index is within bounds
    if row_index < 0 or row_index >= len(X_test):
        row_index = 0  # Default to the first row if out of bounds
    
    # Prepare the data by selecting the row and converting it into a DataFrame with the same column names
    prepared_data = pd.DataFrame([X_test.iloc[row_index].values], columns=X_test.columns)
    
    # Make the prediction
    prediction = model.predict(prepared_data)[0]
    
    return render_template('predict.html', title='Prediction', prediction=prediction, row_index=row_index)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


