from extract import extract_data
from transform import transform_data
from load import load_data, verify_data
from utils import get_db_engine

def run_pipeline():
    # Extract
    df = extract_data("dataset.csv")

    # Transform
    df_transformed = transform_data(df)

    # Load
    engine = get_db_engine()
    load_data(df_transformed, engine)

    # Verify
    verify_data(engine)

    # Save locally
    df_transformed.to_csv("processed_spotify_data.csv", index=False)
    print("💾 Processed data saved locally as processed_spotify_data.csv")

if __name__ == "__main__":
    run_pipeline()