import pandas as pd

# Load raw data
df = pd.read_csv(r"B:/RetailSense_Agent_MVP/data/raw/walmart.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Sort data for time-series safety
df = df.sort_values(by=["Store", "Date"])

# Drop rows with missing sales
df = df.dropna(subset=["Weekly_Sales"])

# Forward fill remaining missing values
df = df.fillna(method="ffill")

print("Data cleaned successfully")




# Lag features (previous weeks sales)
df["sales_lag_1"] = df.groupby("Store")["Weekly_Sales"].shift(1)
df["sales_lag_2"] = df.groupby("Store")["Weekly_Sales"].shift(2)

# Rolling mean (trend)
df["rolling_mean_3"] = (
    df.groupby("Store")["Weekly_Sales"]
    .rolling(window=3)
    .mean()
    .reset_index(level=0, drop=True)
)

# Percentage change (momentum)
df["sales_pct_change"] = (
    df.groupby("Store")["Weekly_Sales"]
    .pct_change()
)

# Holiday flag as integer
df["Holiday_Flag"] = df["Holiday_Flag"].astype(int)

# Drop rows created due to lag features
df = df.dropna()
print(df.head())
print("Features engineered successfully")


# Save processed data
df.to_csv(r"B:/RetailSense_Agent_MVP/data/processed/walmart_processed.csv", index=False)
print("Processed data saved")
