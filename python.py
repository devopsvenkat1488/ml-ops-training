import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_diabetes
import joblib

# Load sample dataset (Diabetes dataset)
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = (data.target > 140).astype(int)  # Create a binary label (0 or 1)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Save the model for later deployment
joblib.dump(model, 'model.joblib')
