import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("🔄 Starting data transformation...")
    df.dropna(inplace=True)

    # Add duration column
    df['duration_min'] = df['duration_ms'] / 60000
    df = df.drop('duration_ms', axis=1)

    # Filter popular tracks
    df_transformed = df[df['popularity'] > 70].copy()
    print("✅ Data transformation completed.")
    return df_transformed
