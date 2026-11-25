
import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATABASE_PATH = BASE_DIR / "database" / "otif_database.db"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "otif_order_performance.csv"


def export_otif_data():
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        df = pd.read_sql_query(
            "SELECT * FROM otif_order_performance",
            connection
        )

        df.to_csv(OUTPUT_FILE, index=False)

        print("OTIF data mart exported successfully!")
        print(f"Records exported: {len(df)}")
        print(f"Output file: {OUTPUT_FILE}")

    finally:
        connection.close()


if __name__ == "__main__":
    export_otif_data()
