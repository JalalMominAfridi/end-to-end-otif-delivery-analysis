# End-to-End OTIF Delivery Performance Analysis

## Project Overview

This project analyzes delivery performance for a simulated electronics company, ABC Electronics, using the On-Time In-Full (OTIF) metric.

The objective is to evaluate whether customer orders are delivered on time and in full, identify operational performance gaps, and provide data-driven recommendations.

## Business Problem

The company wants to understand its delivery performance across different months, regions, customer types, products, and warehouses.

## Tools & Technologies

- Python – Data cleaning and processing
- SQL – Data transformation and analysis
- SQLite – Database management
- Power BI – Interactive dashboards and visualization
- Google Colab – Python development environment

## Dataset

The project uses six simulated ERP datasets:

- Customers
- Products
- Orders
- Order Items
- Deliveries
- Delivery Items

The dataset contains 500 orders, including 455 delivered orders eligible for OTIF analysis.

## OTIF Calculation

OTIF measures the percentage of eligible orders delivered both on time and in full.

**OTIF = Successful OTIF Orders / Total Eligible Delivered Orders × 100**

- On Time: Final delivery date is on or before the promised date.
- In Full: All ordered product quantities are delivered.
- Cancelled and open orders are excluded.

## Key Results

| KPI | Result |
|---|---:|
| Delivered Orders | 455 |
| Successful OTIF Orders | 122 |
| Failed OTIF Orders | 333 |
| OTIF Performance | 26.81% |
| On-Time Performance | 36.04% |
| In-Full Performance | 79.12% |

## Key Business Findings

1. Delivery timeliness is the main performance challenge, with only 36.04% of delivered orders arriving on time.
2. East recorded the highest OTIF among known regions at 31.87%, while North recorded the lowest at 22.03%.
3. Wholesale customers achieved the highest OTIF at 28.71%.
4. Mouse recorded the highest product shortage, with 28 units.
5. WH04 had the highest on-time delivery rate at 37.12%, while WH02 had the lowest at 26.02%.
6. May recorded the highest monthly OTIF at 35.19%, while October recorded the lowest at 14%.

## Recommendations

- Investigate causes of delivery delays.
- Review warehouse dispatch and transportation processes.
- Improve inventory monitoring and replenishment planning.
- Investigate regional and customer-specific delivery challenges.
- Monitor OTIF performance regularly.

## Project Limitations

- The dataset is simulated and does not represent real company transactions.
- The analysis covers January to October 2026.
- Performance comparisons identify differences but do not establish their causes.
- Further investigation using real operational data would be required.

## Project Structure

The repository contains the original datasets, Python notebook, SQLite database, analysis exports, Power BI report, and this documentation.

## Author

Jalal Momin Afridi
