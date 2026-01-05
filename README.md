# Bank Transaction Risk & Anomaly Analyzer

Small CLI tool to load, clean, feature-engineer, score and flag suspicious bank/credit-card transactions.

## Summary

This project processes transaction datasets to compute customer risk scores and flag suspicious transactions. It provides a simple menu-driven CLI (`main.py`) that walks through steps: load data, clean data, build features, compute risk scores, flag suspicious transactions, and export reports.

## Prerequisites


Install dependencies (example):

```bash
pip install pandas numpy scikit-learn matplotlib
```

## Usage

1. From the repository root run:

```bash
python main.py
```

2. Use the interactive menu to:

Follow steps 1→5 before exporting reports (option 6).

## Included Files


## Output

Running the full pipeline (through option 5) will produce a processed dataframe assigned to `final_df` in the code and, when exporting reports (option 6), will trigger `ReportGenerator` which writes summary reports and CSVs (see `flagged_transactions.csv` and `customer_risk_summary.csv`).

## Notes & Next Steps


## License

Add your license or usage terms here.
# 🕵️ Financial Fraud Detection System

## 📌 Project Overview
Automated pipeline for identifying suspicious financial transactions using **Z-Score** and custom risk logic.

## 🛠 Methodology
* **Z-Score Analysis:** To detect statistical outliers in transaction amounts.
* **Risk Scoring:** Assigning a 0-100 score based on type and magnitude.
* **Banding:** Categorizing users into Low, Medium, High, and Critical.

## 📊 Outputs
* `flagged_transactions.csv`: List of all flagged alerts.
* `customer_risk_summary.csv`: Final risk report per customer.
# Bank Transaction Risk & Anomaly Analyzer

Small pipeline for loading, cleaning, feature engineering, scoring, and flagging suspicious bank/credit-card transactions.

## Quick summary

This repository provides an interactive CLI (`main.py`) and supporting modules under `src/` to process transaction logs, compute per-customer risk scores, and export flagged transactions and summary reports.

## Prerequisites

- Python 3.8 or newer
- Recommended packages: `pandas`, `numpy`, `scikit-learn`, `matplotlib`

Install the main dependencies quickly (example):

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install pandas numpy scikit-learn matplotlib
```

If you prefer a `requirements.txt`, create one from your environment with `pip freeze > requirements.txt`.

## Quick start

From the repository root run the interactive pipeline:

```bash
python main.py
```

Common actions in the interactive menu:
- Load dataset
- Clean / normalize transactions
- Build features
- Compute risk scores
- Flag suspicious transactions
- Export reports (CSV)

You can also generate the textual report directly with:

```bash
python Reports/generate_report.py
```

## Project layout

- `main.py` — Interactive entrypoint (repository root).
- `src/` — Processing modules:
	- `Dataloading.py` — Helpers to load CSVs from `data/`.
	- `Datacleaning.py` — Data cleaning utilities.
	- `preparefeatures.py` — Feature engineering functions.
	- `risk_scores.py` — Risk scoring algorithms.
	- `TransactionFlagger.py` — Rules to flag suspicious transactions.
- `data/` — Raw/example input data (e.g. `PS_20174392719_1491204439457_log.csv`).
- `data_generated/` — CSV outputs produced by the pipeline (`flagged_transactions.csv`, `customer_risk_summary.csv`).
- `Reports/` — Report generation scripts (e.g. `generate_report.py`) and text reports.

## Notes on outputs

- `data_generated/flagged_transactions.csv` — All transactions marked as suspicious.
- `data_generated/customer_risk_summary.csv` — Per-customer aggregated risk scores and bands.

## Suggested next steps

- Add a `requirements.txt` for reproducible installs.
- Add unit tests for the scoring and flagging modules.
- Add a non-interactive CLI mode (arguments) for batch processing.
