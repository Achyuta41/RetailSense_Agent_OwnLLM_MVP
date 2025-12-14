import pandas as pd

df = pd.read_csv(r"B:/RetailSense_Agent_MVP/data/raw/walmart.csv")
print(df.head())
print(df.columns)
print(df.isnull().sum())
