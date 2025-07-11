"""
breadprice.py
-------------
Loads the Chapter 11 `breadprice.csv` file, cleans it, and
plots the average bread price for each year.
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1  Load the CSV
# --------------------------------------------------
file_path = Path(__file__).with_name("breadprice.csv")
df = pd.read_csv(file_path)

# --------------------------------------------------
# 2  Basic cleaning
#    – keep only the columns we expect
#    – coerce to numeric (turns blanks into NaN)
# --------------------------------------------------
month_cols = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# Make sure column names match exactly what’s in the CSV
expected_cols = ["Year"] + month_cols
df = df[expected_cols]        # drop any extras that sneak in
df[month_cols] = df[month_cols].apply(
    pd.to_numeric, errors="coerce"
)

# --------------------------------------------------
# 3  Calculate average price per year
#    (skip NaN so 2022—which only has data through July—still works)
# --------------------------------------------------
df["AveragePrice"] = df[month_cols].mean(axis=1, skipna=True)

# Optional: drop years that are completely empty
df = df.dropna(subset=["AveragePrice"])

# --------------------------------------------------
# 4  Plot
# --------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["AveragePrice"],
         marker="o", linestyle="-")

plt.title("Average Bread Price per Year")
plt.xlabel("Year")
plt.ylabel("Average Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 5  (Helpful console print‑out)
# --------------------------------------------------
print("\nAnnual averages:")
print(df[["Year", "AveragePrice"]].to_string(index=False))
