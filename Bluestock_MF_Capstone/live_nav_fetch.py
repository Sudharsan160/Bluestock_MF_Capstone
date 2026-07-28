import requests
import pandas as pd
from pathlib import Path

# Save location
RAW_FOLDER = Path(__file__).parent / "data" / "raw"

schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    print(f"\nDownloading {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = RAW_FOLDER / f"{name}.csv"

        nav_df.to_csv(file_path, index=False)

        print(f" Saved to {file_path}")

    except Exception as e:
        print(f" Failed to download {name}: {e}")