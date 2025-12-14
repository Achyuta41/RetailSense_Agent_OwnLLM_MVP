import pandas as pd

DATA_PATH = "data/processed/walmart_processed.csv"

def sales_agent(store_id: int):
    df = pd.read_csv(DATA_PATH)

    store_df = df[df["Store"] == store_id]

    avg_sales = store_df["Weekly_Sales"].mean()
    holiday_sales = store_df[store_df["Holiday_Flag"] == 1]["Weekly_Sales"].mean()
    non_holiday_sales = store_df[store_df["Holiday_Flag"] == 0]["Weekly_Sales"].mean()

    trend = store_df["Weekly_Sales"].pct_change().mean()

    return {
        "store_id": store_id,
        "average_sales": round(avg_sales, 2),
        "holiday_avg_sales": round(holiday_sales, 2),
        "non_holiday_avg_sales": round(non_holiday_sales, 2),
        "trend": "UP" if trend > 0 else "DOWN"
    }
