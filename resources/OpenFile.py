import pandas as pd

def load_customer(csv_filepath):
    try:
        df = pd.read_csv(csv_filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_filepath}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while reading CSV: {e}")
        return pd.DataFrame()

