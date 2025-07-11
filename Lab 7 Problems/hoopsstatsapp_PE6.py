"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    """
    Cleans FG, 3PT, and FT columns from <makes-attempts> format.
    Splits each into two numeric columns: <Stat>M and <Stat>A.
    Inserts them in place and removes the original columns.
    """
    columns_to_clean = {
        "FG": ("FGM", "FGA"),
        "3PT": ("3PTM", "3PTA"),
        "FT": ("FTM", "FTA")
    }

    for col, (made_col, att_col) in columns_to_clean.items():
        # Find the column index to preserve order
        idx = df.columns.get_loc(col)

        # Split "5-8" into ["5", "8"]
        split_data = df[col].str.split("-", expand=True)

        # Insert made and attempted columns at the original index
        df.insert(idx, made_col, pd.to_numeric(split_data[0]))
        df.insert(idx + 1, att_col, pd.to_numeric(split_data[1]))
        # Remove the original column
        df.drop(columns=[col], inplace=True)

def run():
    """
    The main function to run the HoopStats application.
    """
    # Load your data
    df = pd.read_csv("rawbrogdonstats.csv")

    # Clean the stats
    cleanStats(df)

    # Now df is ready for analysis or viewing
    view = HoopStatsView(df)
    view.mainloop()

if __name__ == "__main__":
    run()