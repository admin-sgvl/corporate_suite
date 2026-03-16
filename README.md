# 🏛️ Corporate Intelligence & Predictive Suite
**An Enterprise-Grade Analytics Portal for Data-Driven Decision Making.**

This repository contains a centralized suite of eight high-impact Data Science applications. Designed for modern organizations, these tools transform raw data into strategic insights across Marketing, Sales, Operations, Finance, and HR.

---

## 🚀 The Analytics Portfolio

### 📈 Operations & Growth
* **Customer RFM Engine:** Segments customers by value and predicts "Probability of Activity" (P-Alive) to optimize retention.
* **Inventory & Sales Forecasting:** Uses Meta’s **Prophet** model to predict demand, calculate **Safety Stock**, and define **Reorder Points**.
* **Dynamic Pricing Optimizer:** Analyzes price elasticity to find the "Sweet Spot" that maximizes total gross revenue.

### 🛒 Sales & Marketing
* **Market Basket Analysis:** Mines transaction logs for product correlations using the **Apriori** algorithm to drive cross-selling.
* **Sales Lead Scorer:** A predictive model that ranks leads by conversion probability, focusing sales efforts on "Hot" prospects.
* **Sentiment & Brand Tracker:** An NLP engine that analyzes customer reviews to monitor brand health and identify product flaws.

### 🛡️ Risk & Talent Management
* **HR Attrition Early Warning:** A classification model that identifies "Flight Risk" employees before they resign.
* **Anomalous Expense Detector:** An unsupervised AI auditor that flags unusual financial transactions and potential fraud.

---

## 📂 Project Architecture
The suite is built using a **Streamlit Multipage** architecture for a seamless user experience.

```text
corporate_suite/
├── Home.py                  <-- Master Portal Landing Page
├── requirements.txt         <-- Unified library dependencies
├── README.md                <-- Project Documentation
├── pages/                   <-- Application Modules
│   ├── 01_Customer_RFM.py
│   ├── 02_Inventory_Forecast.py
│   ├── 03_Market_Basket.py
│   ├── 04_HR_Attrition.py
│   ├── 05_Pricing_Optimizer.py
│   ├── 06_Sentiment_Tracker.py
│   ├── 07_Lead_Scoring.py
│   └── 08_Anomaly_Detector.py

Developed by SG Venture Consulting
Principal Consultant: Patrick Oh
