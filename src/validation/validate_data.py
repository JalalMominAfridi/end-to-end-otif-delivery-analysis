
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_PATH = BASE_DIR / "database" / "otif_database.db"

EXPECTED_TABLES = [
    "customers",
    "products",
    "orders",
    "order_items",
    "deliveries",
    "delivery_items"
]

def validate_data():
    """Check that source tables exist and contain records."""

    if not DATABASE_PATH.exists():
        raise FileNotFoundError(
            f"Database not found: {DATABASE_PATH}"
        )

    connection = sqlite3.connect(DATABASE_PATH)

    failed_checks = []

    try:
        cursor = connection.cursor()

        for table in EXPECTED_TABLES:
            cursor.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type='table' AND name=?",
                (table,)
            )

            if cursor.fetchone() is None:
                print(f"FAIL: Table {table} does not exist.")
                failed_checks.append(table)
                continue

            cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
            row_count = cursor.fetchone()[0]

            if row_count == 0:
                print(f"FAIL: Table {table} is empty.")
                failed_checks.append(table)
            else:
                print(f"PASS: {table} contains {row_count} rows.")

        if failed_checks:
            print("\nData validation FAILED.")
            raise ValueError(
                f"Failed checks: {failed_checks}"
            )

        print("\nAll source table checks passed.")

    finally:
        connection.close()


if __name__ == "__main__":
    validate_data()
