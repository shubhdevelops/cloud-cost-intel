import pandas as pd

# Read raw dataset
df = pd.read_csv("data/raw/gcp_final_approved_dataset.csv")

# Rename columns
df.columns = [
    "resource_id",
    "service_name",
    "usage_quantity",
    "usage_unit",
    "region_zone",
    "cpu_utilization_pct",
    "memory_utilization_pct",
    "network_inbound_bytes",
    "network_outbound_bytes",
    "usage_start_date",
    "usage_end_date",
    "cost_per_quantity_usd",
    "unrounded_cost_usd",
    "rounded_cost_usd",
    "total_cost_inr"
]

# Convert dates
df["usage_start_date"] = pd.to_datetime(
    df["usage_start_date"],
    dayfirst=True
)

df["usage_end_date"] = pd.to_datetime(
    df["usage_end_date"],
    dayfirst=True
)

# Save curated data
df.to_csv("data/curated/billing_curated.csv", index=False)

print("Curated dataset created successfully!")
print("Rows:", len(df))
