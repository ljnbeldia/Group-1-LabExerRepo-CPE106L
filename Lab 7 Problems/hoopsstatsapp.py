import pandas as pd
from pathlib import Path


def cleanStats(df):
    """
    Splits 'FG', '3PT', and 'FT' columns from 'made-attempts'
    into separate numeric columns: FGM, FGA, 3PM, 3PA, FTM, FTA.
    """
    shot_columns = {
        "FG": ("FGM", "FGA"),
        "3PT": ("3PM", "3PA"),
        "FT": ("FTM", "FTA")
    }

    for original_col, (made_col, att_col) in shot_columns.items():
        if original_col in df.columns:
            idx = df.columns.get_loc(original_col)
            split_cols = df[original_col].str.split("-", expand=True)
            df[made_col] = split_cols[0].astype(int)
            df[att_col] = split_cols[1].astype(int)
            df.drop(columns=[original_col], inplace=True)
            made = df.pop(made_col)
            att = df.pop(att_col)
            df.insert(idx, att_col, att)
            df.insert(idx, made_col, made)

    return df


def main():
    try:
        # 👇 Automatically find the CSV in the same folder as this script
        file_path = Path(__file__).with_name("rawbrogdonstats.csv")
        df = pd.read_csv(file_path)

        # Clean the stats
        df = cleanStats(df)

        # Print the cleaned DataFrame
        print("\n✅ Cleaned Brogdon Stats:\n")
        print(df.to_string(index=False))

        # Optional: Save to a new cleaned CSV
        cleaned_path = file_path.with_name("cleaned_brogdonstats.csv")
        df.to_csv(cleaned_path, index=False)
        print(f"\n📁 Saved cleaned data to '{cleaned_path.name}'")

    except FileNotFoundError:
        print("❌ File 'rawbrogdonstats.csv' not found in the same folder as hoopsstatsapp.py")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


if __name__ == "__main__":
    main()
