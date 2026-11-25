# End-to-End OTIF Data Engineering Pipeline

An end-to-end data engineering project that transforms simulated order and delivery data into structured datasets for supply chain performance analysis.

The project demonstrates data ingestion, SQL transformations, data validation, automated testing, data exports and CI/CD using GitHub Actions.

## Project Overview

On-Time In-Full (OTIF) is a key supply chain performance metric used to measure whether customer orders are delivered on time and in the quantities ordered.

This project builds a Python and SQL-based pipeline to process order, product, customer and delivery data, calculate OTIF performance, and generate analytical outputs.

**Business objective:** Understand delivery performance, identify OTIF failures and provide reliable data for supply chain reporting.

> **Dataset:** This project uses simulated ABC Electronics business data. It does not contain real company or customer records.

## Architecture

```text
          Raw CSV Files
                |
                v
        Data Ingestion
          (Python)
                |
                v
         SQLite Database
                |
                v
       SQL Transformations
        (OTIF Calculation)
                |
                v
        Data Validation
                |
                v
       Processed CSV Outputs
                |
                v
       Power BI / Analytics
```

The pipeline is orchestrated through Python and can be executed locally or automatically through GitHub Actions.

## Technologies Used

| Area | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Query Language | SQL |
| Data Testing | Pytest |
| Logging | Python Logging |
| Version Control | GitHub |
| CI/CD | GitHub Actions |
| Data Visualisation | Power BI |

## Data Pipeline

The pipeline processes six source datasets:

- Customers
- Products
- Orders
- Order Items
- Deliveries
- Delivery Items

### Pipeline Steps

**1. Data Ingestion**

- Reads raw CSV files using Pandas.
- Loads the source data into SQLite tables.
- Creates a local database for processing.

**2. SQL Transformations**

- Creates staging tables.
- Calculates the final delivery date for each order.
- Aggregates ordered and delivered quantities by product.
- Determines whether each order was delivered on time and in full.
- Creates an OTIF performance view.

**3. Data Validation**

- Checks whether the required source tables exist.
- Checks that source tables contain records.
- Verifies that the pipeline produces valid output.

**4. Data Export**

Exports the transformed OTIF results into a processed CSV file for further analysis.

**5. Logging and Error Handling**

- Records pipeline execution steps.
- Logs successful operations and errors.
- Makes it easier to monitor pipeline execution.

## OTIF Business Logic

An order is considered OTIF successful only when it satisfies both conditions:

- **On Time:** The final delivery date is on or before the promised delivery date.
- **In Full:** The total delivered quantity meets the ordered quantity for every product in the order.

**OTIF Formula**

```text
OTIF % = (Orders delivered On Time and In Full
          / Eligible Delivered Orders) × 100
```

Additional calculation rules:

- Split shipments are aggregated at order and product level.
- The final delivery date
