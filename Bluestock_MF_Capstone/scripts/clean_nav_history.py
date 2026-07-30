import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Read CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["date"])

# Sort by fund and date
df = df.sort_values(["amfi_code", "date"])

# Forward fill missing NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
df = df.drop_duplicates()

# Keep only NAV > 0
df = df[df["nav"] > 0]

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print(df.head())