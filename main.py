import pandas as pd
from sqlalchemy import create_engine
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def run_spotify_etl():
    # --- DATABASE CONNECTION DETAILS ---
    db_user = os.getenv('DB_USER')
    db_host = os.getenv('DB_HOST')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # Create the database connection string
    # The f-string format is 'postgresql://user:password@host:port/dbname'
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    try:
        # Create a database engine
        engine = create_engine(connection_string)
        print("Successfully connected to PostgreSQL.")
    except Exception as e:
        print(f"Failed to connect to the database. Error: {e}")
        sys.exit(1)

    # --- 1. EXTRACT ---
    try:
        df = pd.read_csv('dataset.csv')
        print("Successfully extracted data from dataset.csv.")
    except FileNotFoundError:
        print("Error: dataset.csv not found. Make sure it's in the same folder.")
        sys.exit(1)

    # --- 2. TRANSFORM ---
    print("Starting data transformation...")
    # Handle missing values
    df.dropna(inplace=True)
    
    # Create a new column 'duration_min'
    df['duration_min'] = df['duration_ms'] / 60000
    
    # Drop the original 'duration_ms' column
    df = df.drop('duration_ms', axis=1)
    
    # Filter for tracks with popularity > 70
    df_transformed = df[df['popularity'] > 70].copy()
    print("Data transformation completed successfully.")

    # --- 3. LOAD ---
    try:
        print("Loading data into PostgreSQL...")
        # Load the transformed DataFrame into a new table named 'popular_tracks'
        # if_exists='replace' will drop the table if it already exists and create a new one
        df_transformed.to_sql('popular_tracks', engine, if_exists='replace', index=False)
        print("Data successfully loaded into the 'popular_tracks' table.")
    except Exception as e:
        print(f"Failed to load data into the database. Error: {e}")
        sys.exit(1)
        
    # --- 4. VERIFY ---
    try:
        print("\nVerifying data from the database...")
        # Read the data back from the table to verify it was loaded
        with engine.connect() as connection:
            verified_df = pd.read_sql_table('popular_tracks', connection)
            print("First 5 rows from the 'popular_tracks' table:")
            print(verified_df.head())
    except Exception as e:
        print(f"Failed to verify data. Error: {e}")

    # --- 5. SAVE TRANSFORMED DATA LOCALLY ---
    try:
        df_transformed.to_csv('processed_spotify_data.csv', index=False)
        print("Processed data saved to processed_spotify_data.csv")
    except Exception as e:
        print(f"Failed to save. Error: {e}")

if __name__ == '__main__':
    run_spotify_etl()