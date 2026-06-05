import pandas as pd

df = pd.read_csv("data/raw/gcp_final_approved_dataset.csv")

print("\n===== BASIC INFO =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n===== NULL VALUES =====")
print(df.isnull().sum())

print("\n===== UNIQUE SERVICES =====")
print(df["Service Name"].nunique())

print("\n===== UNIQUE REGIONS =====")
print(df["Region/Zone"].nunique())

print("\n===== TOP 10 COSTLIEST SERVICES =====")

print(
    df.groupby("Service Name")["Total Cost (INR)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
