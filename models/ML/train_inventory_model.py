import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load processed data
df = pd.read_csv(r"B:/RetailSense_Agent_MVP/data/processed/walmart_processed.csv")

print("Dataset loaded:", df.shape)

# Features used for prediction
FEATURES = [
    "sales_lag_1",
    "sales_lag_2",
    "rolling_mean_3",
    "sales_pct_change",
    "Holiday_Flag",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment"
]

TARGET = "Weekly_Sales"

X = df[FEATURES]
y = df[TARGET]

# Time-based split (NO SHUFFLE)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

print("Model trained successfully")



# Evaluate model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)


# Save trained model
joblib.dump(model, "models/ml/inventory_model.pkl")
print("Model saved successfully")
