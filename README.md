# 🕵️ Bank Transaction Risk & Anomaly Analyzer

A Python-based CLI pipeline for identifying suspicious financial transactions using statistical anomaly detection and custom risk scoring.

---

## 📋 Overview

This system automates the detection of high-risk and anomalous transactions in banking datasets. It processes raw transaction logs through a multi-stage pipeline:

1. **Data Loading** — Import transaction CSVs
2. **Data Cleaning** — Normalize and validate records
3. **Feature Engineering** — Create derived signals
4. **Risk Scoring** — Compute 0–100 risk scores per customer
5. **Transaction Flagging** — Mark suspicious transactions
6. **Report Generation** — Export CSVs and summaries

### Key Features
- **Z-Score Analysis** — Detect statistical outliers in transaction amounts
- **Risk Banding** — Categorize customers into Low, Medium, High, and Critical tiers
- **Interactive Menu** — User-friendly CLI for running the pipeline step-by-step
- **CSV Export** — Generate structured reports for compliance and review

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or newer
- Virtual environment (optional but recommended)

### Setup
```bash
# Clone or navigate to the project directory
cd "Bank Transaction Risk & Anomaly Analyzer"

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install pandas numpy scikit-learn matplotlib
```

### Run the Pipeline
```bash
python main.py
```

Then follow the interactive menu:
- Press `1` to load dataset
- Press `2` to clean data
- Press `3` to build features
- Press `4` to score customers
- Press `5` to flag suspicious transactions
- Press `6` to export reports
- Press `7` for a quick console summary
- Press `0` to exit

### Generate a Text Report
```bash
python Reports/generate_report.py
```

---

## 📁 Project Structure

```
Bank Transaction Risk & Anomaly Analyzer/
├── main.py                          # Interactive CLI entrypoint
├── README.md                        # This file
├── data/
│   └── PS_20174392719_1491204439457_log.csv    # Raw transaction data
├── data_generated/
│   ├── flagged_transactions.csv     # Output: all flagged transactions
│   └── customer_risk_summary.csv    # Output: per-customer risk scores
├── src/
│   ├── Dataloading.py               # Load and read CSVs
│   ├── Datacleaning.py              # Cleaning utilities
│   ├── preparefeatures.py           # Feature engineering
│   ├── risk_scores.py               # Risk scoring logic
│   └── TransactionFlagger.py        # Flagging rules and logic
└── Reports/
    ├── generate_report.py           # Text report generator
    └── report.txt                   # Generated report output
```

---

## 📊 Outputs

After running the full pipeline, you'll get:

| File | Description |
|------|-------------|
| `data_generated/flagged_transactions.csv` | All transactions marked as suspicious (includes risk scores and reasons) |
| `data_generated/customer_risk_summary.csv` | One row per customer with aggregated risk score and risk band |
| `Reports/report.txt` | Human-readable text summary of the analysis |

---

## 🔧 Methodology

### Risk Scoring
Each transaction is assigned a risk score (0–100) based on:
- Transaction amount and frequency patterns
- Deviation from customer baseline (Z-Score)
- Transaction type and associated risk factors

### Risk Bands
Customers are categorized into tiers:
- **Low** (0–25)
- **Medium** (26–50)
- **High** (51–75)
- **Critical** (76–100)

---

