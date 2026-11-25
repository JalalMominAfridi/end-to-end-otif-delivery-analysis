
import sqlite3
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parents[1]
DATABASE_PATH = BASE_DIR / "database" / "otif_database.db"


@pytest.fixture
def connection():
    conn = sqlite3.connect(DATABASE_PATH)
    yield conn
    conn.close()


def test_database_exists():
    assert DATABASE_PATH.exists()


def test_no_duplicate_order_ids(connection):
    result = connection.execute("""
        SELECT order_id, COUNT(*)
        FROM otif_order_performance
        GROUP BY order_id
        HAVING COUNT(*) > 1
    """).fetchall()

    assert len(result) == 0


def test_otif_values_are_binary(connection):
    result = connection.execute("""
        SELECT DISTINCT otif
        FROM otif_order_performance
    """).fetchall()

    values = {row[0] for row in result}
    assert values.issubset({0, 1})


def test_expected_order_counts(connection):
    result = connection.execute("""
        SELECT COUNT(*), SUM(otif)
        FROM otif_order_performance
    """).fetchone()

    assert result[0] == 455
    assert result[1] == 122
