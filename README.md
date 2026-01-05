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