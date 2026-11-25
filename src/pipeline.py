
import sqlite3
import runpy
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATABASE_PATH = BASE_DIR / "database" / "otif_database.db"

INGESTION_SCRIPT = BASE_DIR / "src" / "ingestion" / "load_data.py"
VALIDATION_SCRIPT = BASE_DIR / "src" / "validation" / "validate_data.py"
EXPORT_SCRIPT = BASE_DIR / "src" / "export_data.py"

STAGING_SQL = BASE_DIR / "sql" / "staging" / "01_create_staging_tables.sql"
TRANSFORMATION_SQL = BASE_DIR / "sql" / "transformations" / "02_transform_otif.sql"

# Create logs folder
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"

# Configure logging
logger = logging.getLogger("OTIF_Pipeline")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def run_sql_script(connection, file_path):
    sql = file_path.read_text(encoding="utf-8")
    connection.executescript(sql)
    logger.info("Completed SQL script: %s", file_path.name)


def run_pipeline():
    logger.info("=" * 50)
    logger.info("Starting OTIF data engineering pipeline")

    try:
        # STEP 1: DATA INGESTION
        logger.info("STEP 1: DATA INGESTION")

        runpy.run_path(
            str(INGESTION_SCRIPT),
            run_name="__main__"
        )

        logger.info("Data ingestion completed")

        # STEP 2: SQL TRANSFORMATIONS
        logger.info("STEP 2: SQL TRANSFORMATIONS")

        connection = sqlite3.connect(DATABASE_PATH)

        try:
            connection.execute(
                "DROP VIEW IF EXISTS otif_order_performance"
            )

            for table in [
                "stg_customers",
                "stg_products",
                "stg_orders",
                "stg_order_items",
                "stg_deliveries",
                "stg_delivery_items"
            ]:
                connection.execute(
                    f'DROP TABLE IF EXISTS "{table}"'
                )

            run_sql_script(connection, STAGING_SQL)
            run_sql_script(connection, TRANSFORMATION_SQL)

            result = connection.execute(
                """
                SELECT COUNT(*), COALESCE(SUM(otif), 0)
                FROM otif_order_performance
                """
            ).fetchone()

            total_orders, successful_orders = result

            logger.info("Delivered orders: %s", total_orders)
            logger.info("Successful OTIF orders: %s", successful_orders)

            if total_orders == 0:
                raise ValueError("OTIF dataset is empty.")

            connection.commit()

        finally:
            connection.close()

        # STEP 3: DATA VALIDATION
        logger.info("STEP 3: DATA VALIDATION")

        runpy.run_path(
            str(VALIDATION_SCRIPT),
            run_name="__main__"
        )

        logger.info("Data validation completed")

        # STEP 4: DATA MART EXPORT
        logger.info("STEP 4: DATA MART EXPORT")

        runpy.run_path(
            str(EXPORT_SCRIPT),
            run_name="__main__"
        )

        logger.info("Data mart export completed")
        logger.info("OTIF PIPELINE COMPLETED SUCCESSFULLY!")
        logger.info("=" * 50)

    except Exception:
        logger.exception("OTIF PIPELINE FAILED")
        raise


if __name__ == "__main__":
    run_pipeline()
