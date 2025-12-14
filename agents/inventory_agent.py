import pandas as pd
import joblib

# Load trained model
MODEL_PATH = "models/ml/inventory_model.pkl"
DATA_PATH = "data/processed/walmart_processed.csv"

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

def inventory_agent(store_id: int,weeks):
    """
    Predict demand and stock risk for a given store
    """

    store_data = df[df["Store"] == store_id].sort_values("Date").tail(weeks)

    if len(store_data) < 1:
        return {
            "error": "Insufficient data for store"
        }

    latest = store_data.iloc[-1]

    features = [[
        latest["sales_lag_1"],
        latest["sales_lag_2"],
        latest["rolling_mean_3"],
        latest["sales_pct_change"],
        latest["Holiday_Flag"],
        latest["Temperature"],
        latest["Fuel_Price"],
        latest["CPI"],
        latest["Unemployment"]
    ]]

    prediction = model.predict(features)[0]

    # Risk classification (simple rule-based)
    if prediction > latest["rolling_mean_3"] * 1.1:
        risk = "HIGH"
    elif prediction > latest["rolling_mean_3"] * 0.9:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "store_id": store_id,
        "predicted_weekly_sales": round(prediction, 2),
        "risk_level": risk
    }
