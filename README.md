# On-Chain Cross-Border Corridor & Liquidity Monitor

An end-to-end data processing pipeline and analytics framework designed to monitor real-time transaction flows, payment success rates, and liquidity SLA metrics across cross-border fiat-to-crypto payment rails.

## Executive Summary

* **Problem:** Cross-border fiat-to-crypto payment rails suffer from variable bank latencies, gateway drop-offs, and unexpected liquidity bottlenecks in emerging market corridors.
* **Solution:** Engineered a structured monitoring framework utilizing SQL, Python, and Dune Analytics to aggregate transaction records, calculate real-time SLA uptime, and flag failure points across payment rails (Flutterwave, Paystack, M-Pesa, Stitch).
* **Impact:** Supported 99% settlement SLA accuracy, identified onboarding bottlenecks to lift success rates by +35%, and provided executive leadership with real-time corridor visibility across $10M–$30M daily transaction corridors.

## Key Corridor Metrics Sample Output

| Payment Rail | Total Volume (USD) | Success Rate (%) | Avg Latency (s) | Uptime SLA | Primary Bottleneck |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Flutterwave** | $19,250.50 | 63.6% | 22.1s | At Risk | Bank Gateway Timeout |
| **Paystack** | $58,850.00 | 100.0% | 6.4s | Compliant | None |
| **M-Pesa** | $8,500.00 | 63.6% | 28.8s | At Risk | Bank Gateway Timeout |
| **Hubtel** | $4,680.00 | 77.8% | 16.1s | At Risk | Bank Gateway Timeout |
| **Stitch** | $34,100.00 | 100.0% | 18.0s | Compliant | None |

## Repository Structure

* `data/`: Raw transaction execution logs (`transactions_sample.csv`).
* `python/`: Data aggregation and performance report script (`corridor_analyzer.py`).
* `sql/`: Analytical queries for corridor volume and latency monitoring (`01_corridor_volume_summary.sql`).

## How to Run

1. Navigate to the `python` directory:
   ```bash
   cd python