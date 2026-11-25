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
- The final delivery date is determined using the latest shipment date.
- Only delivered orders are included in the OTIF calculation.
- Open and cancelled orders are excluded.

## Key Results

The pipeline processed the simulated dataset and produced the following results:

| Metric | Result |
|---|---:|
| Total source orders | 500 |
| Eligible delivered orders | 455 |
| Successful OTIF orders | 122 |
| Failed OTIF orders | 333 |
| OTIF performance | 26.81% |
| On-Time performance | 36.04% |
| In-Full performance | 79.12% |

**Key observation:** Timeliness is the main area of concern in this dataset. Only 36.04% of eligible delivered orders were on time, compared with 79.12% delivered in full.

These results are descriptive findings from simulated data and do not establish the underlying causes of delivery delays.

## Automated Testing

The project uses Pytest to check important pipeline outputs.

Current automated tests include:

- Database creation.
- Duplicate order ID validation.
- Binary OTIF flag validation.
- Expected output record count and successful OTIF count.

Run the tests locally:

```bash
python -m pytest tests -v
```

## CI/CD with GitHub Actions

GitHub Actions automatically executes the pipeline and automated tests when changes are pushed to the main branch or a pull request is created.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Executes the data pipeline.
5. Runs automated tests.

**CI/CD status:** Successfully executed in GitHub Actions on Linux in two separate runs.

## Project Structure

```text
OTIF-Data-Engineering-Project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion/
│   ├── transformations/
│   ├── validation/
│   ├── pipeline.py
│   ├── export_data.py
│   └── OTIF_delivery_performance_analysis.ipynb
│
├── sql/
│   ├── staging/
│   ├── transformations/
│   └── data_marts/
│
├── tests/
│   └── test_pipeline.py
│
├── database/
├── powerbi/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── logs/
├── requirements.txt
└── README.md
```

*Note: The local database and execution logs are generated at runtime and are not required in the repository.*

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/JalalMominAfridi/end-to-end-otif-delivery-analysis.git
```

### 2. Navigate to the project directory

```bash
cd end-to-end-otif-delivery-analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Execute the pipeline

```bash
python src/pipeline.py
```

### 5. Run automated tests

```bash
python -m pytest tests -v
```

## Skills Demonstrated

- Building an end-to-end data pipeline.
- Ingesting and processing structured data.
- Working with relational databases and SQL.
- Applying business rules to operational data.
- Data validation and automated testing.
- Pipeline logging and error handling.
- Version control and CI/CD automation.
- Preparing structured datasets for BI reporting.

## Author

**Jalal Momin Afridi**

Management (Data Science) | Hasselt University

GitHub: [JalalMominAfridi](https://github.com/JalalMominAfridi)

---

*This project is developed for learning and portfolio demonstration purposes using simulated business data.*
