import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with invalid return values
df = df.dropna(subset=return_columns)

# Convert expense ratio to numeric
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Remove invalid expense ratios (0.1% to 2.5%)
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Flag anomalous return values
df["anomaly"] = (
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100) |
    (df["return_3yr_pct"] > 100) |
    (df["return_3yr_pct"] < -100) |
    (df["return_5yr_pct"] > 100) |
    (df["return_5yr_pct"] < -100)
)

# Remove duplicate rows
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
output_file = "data/processed/scheme_performance_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("Saved to:", output_file)
print(df.head())