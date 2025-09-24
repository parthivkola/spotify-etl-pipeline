import pandas as pd
from sqlalchemy import create_engine

def load_data(df: pd.DataFrame, engine, table_name="popular_tracks"):
    try:
        print(f"⬆️ Loading data into PostgreSQL table: {table_name}...")
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print("✅ Data successfully loaded into PostgreSQL.")
    except Exception as e:
        raise RuntimeError(f"❌ Failed to load data into database: {e}")

def verify_data(engine, table_name="popular_tracks"):
    import pandas as pd
    with engine.connect() as connection:
        df = pd.read_sql_table(table_name, connection)
        print("🔍 First 5 rows from the DB:")
        print(df.head())
        return df
