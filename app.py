from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Start Flask App
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON input
    df = pd.DataFrame([data])  # Convert input data to DataFrame
    expected_features = ['age', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6', 'extra_feature']
    for feature in expected_features:
        if feature not in df.columns:
            df[feature] = 0 # Fill missing features with default values
    prediction = model.predict(df)  # Model predicts based on input
    return jsonify({'prediction': int(prediction[0])})  # Return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Run Flask app on port 5000
