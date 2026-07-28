from pathlib import Path
import pandas as pd

# Path to the raw data folder
RAW_FOLDER = Path(__file__).parent / "data" / "raw"

print(f"Reading files from: {RAW_FOLDER}")

csv_files = list(RAW_FOLDER.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 80)
    print(f"Processing: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("=" * 80)