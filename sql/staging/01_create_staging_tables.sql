
-- Create staging tables from the raw source tables.
-- The Python ingestion script loads the source CSVs into SQLite.

CREATE TABLE IF NOT EXISTS stg_customers AS
SELECT * FROM customers;

CREATE TABLE IF NOT EXISTS stg_products AS
SELECT * FROM products;

CREATE TABLE IF NOT EXISTS stg_orders AS
SELECT * FROM orders;

CREATE TABLE IF NOT EXISTS stg_order_items AS
SELECT * FROM order_items;

CREATE TABLE IF NOT EXISTS stg_deliveries AS
SELECT * FROM deliveries;

CREATE TABLE IF NOT EXISTS stg_delivery_items AS
SELECT * FROM delivery_items;
