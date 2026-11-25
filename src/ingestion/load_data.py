
import pandas as pd
import sqlite3
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Source and database locations
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "otif_database.db"

# Create database directory if missing
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

# Source files
CSV_FILES = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "order_items.csv",
    "deliveries.csv",
    "delivery_items.csv"
]

def load_data():
    """Load raw ERP CSV files into SQLite staging tables."""

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        for file_name in CSV_FILES:
            file_path = RAW_DATA_DIR / file_name

            if not file_path.exists():
                raise FileNotFoundError(f"Missing source file: {file_path}")

            df = pd.read_csv(file_path)

            table_name = file_path.stem

            df.to_sql(
                table_name,
                connection,
                if_exists="replace",
                index=False
            )

            print(
                f"Loaded {file_name}: "
                f"{len(df)} rows into {table_name}"
            )

        print("\nData ingestion completed successfully.")

    finally:
        connection.close()


if __name__ == "__main__":
    load_data()
