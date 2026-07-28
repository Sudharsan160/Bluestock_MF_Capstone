import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Unique Fund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nTotal Fund Houses:", df["fund_house"].nunique())
print("Total Categories:", df["category"].nunique())
print("Total Sub Categories:", df["sub_category"].nunique())
print("Total Risk Categories:", df["risk_category"].nunique())