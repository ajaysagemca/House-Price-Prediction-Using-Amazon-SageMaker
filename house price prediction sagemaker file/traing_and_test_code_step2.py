import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib  # For saving the model
import os
import pickle
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('house_prices.csv')  # Replace with your dataset
X = data.drop(columns=['price'])  # Features
y = data['price']  # Target variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
    
print("finish")    