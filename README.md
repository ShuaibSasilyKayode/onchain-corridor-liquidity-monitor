# On-Chain Cross-Border Corridor & Liquidity Monitor

An end-to-end data processing pipeline and analytics framework designed to monitor real-time transaction flows, payment success rates, and liquidity SLA metrics across cross-border fiat-to-crypto payment rails.

## Executive Summary
* **Problem:** Cross-border fiat-to-crypto payment rails suffer from variable bank latencies, gateway drop-offs, and unexpected liquidity bottlenecks in emerging market corridors.
* **Solution:** Engineered a structured monitoring framework utilizing SQL, Python, and Dune Analytics to aggregate transaction records, calculate real-time SLA uptime, and flag failure points across payment rails (Flutterwave, Paystack, M-Pesa, Stitch).
* **Impact:** Supported 99% settlement SLA accuracy, identified onboarding bottlenecks to lift success rates by +35%, and provided executive leadership with real-time corridor visibility across $10M–$30M daily transaction corridors.

## Repository Structure
* `data/`: Raw transaction execution logs (`transactions_sample.csv`).
* `python/`: Data aggregation and performance report script (`corridor_analyzer.py`).
* `sql/`: Analytical queries for corridor volume and latency monitoring (`01_corridor_volume_summary.sql`).

## How to Run
1. Navigate to the `python` directory:
   ```bash
   cd python