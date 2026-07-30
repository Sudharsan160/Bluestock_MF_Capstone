import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# Remove rows with invalid dates
df = df.dropna(subset=["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# Keep only valid transaction types
valid_types = ["SIP", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep only valid KYC values
valid_kyc = ["Verified", "Pending", "Rejected"]
df = df[df["kyc_status"].isin(valid_kyc)]

# Remove duplicates
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file
output_file = "data/processed/investor_transactions_cleaned.csv"
df.to_csv(output_file, index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("Saved to:", output_file)
print(df.head())