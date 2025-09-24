import pandas as pd

def extract_data(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
        print("✅ Successfully extracted data from dataset.csv.")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("❌ dataset.csv not found. Make sure it's in the correct folder.")