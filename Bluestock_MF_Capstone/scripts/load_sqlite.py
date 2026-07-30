import pandas as pd
from sqlalchemy import create_engine
import os

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Files to load
files = {
    "nav_history": "data/processed/nav_history_cleaned.csv",
    "investor_transactions": "data/processed/investor_transactions_cleaned.csv",
    "scheme_performance": "data/processed/scheme_performance_cleaned.csv"
}

for table_name, file_path in files.items():

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded successfully ({len(df)} rows).")

    else:
        print(f"File not found: {file_path}")

print("\nSQLite database created successfully!")