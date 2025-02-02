from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Start Flask App
app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON input
    df = pd.DataFrame([data])  # Convert input data to DataFrame

    # Check if all the expected features are present in the input
    expected_features = ['age', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    for feature in expected_features:
        if feature not in df.columns:
            df[feature] = 0  # Fill missing features with default values

    # Scale the features before passing to the model
    scaled_data = scaler.transform(df)

    # Make the prediction
    prediction = model.predict(scaled_data)  # Model predicts based on input
    prediction_label = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'

    return jsonify({'prediction': prediction_label})  # Return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run Flask app on port 5000

