# 🏛️ Corporate Intelligence & Predictive Suite

A centralized "Master Portal" containing four high-impact Data Science applications. This suite transforms raw organizational data into actionable strategies for Marketing, Operations, Sales, and Human Resources.

## 🛠️ Included Applications

### 1. 🎯 Customer RFM Engine
- **Focus:** Marketing & CRM
- **Value:** Segments customers into behavioral groups (Champions, At Risk, etc.) and predicts the "Probability of Being Alive" (P-Alive).
- **Impact:** Optimizes ad spend and increases customer retention.

### 2. 📈 Inventory & Sales Forecasting
- **Focus:** Supply Chain & Operations
- **Value:** Uses Meta's **Prophet** model to forecast demand and calculate **Safety Stock** and **Reorder Points**.
- **Impact:** Reduces capital tied up in excess inventory and prevents lost sales from stockouts.

### 3. 🛒 Market Basket Analysis
- **Focus:** Sales & Merchandising
- **Value:** Mines transaction logs for product correlations using the **Apriori** algorithm.
- **Impact:** Powers "Frequently Bought Together" bundles and optimizes store/website layouts.

### 4. 🛡️ HR Attrition Early Warning
- **Focus:** Human Resources & Talent Management
- **Value:** A machine learning classifier that flags "Flight Risk" employees based on historical turnover patterns.
- **Impact:** Drastically reduces hiring costs by enabling proactive employee retention.

---

## 📂 Project Structure
```text
corporate_suite/
├── Home.py                <-- Main Entry Point
├── requirements.txt       <-- Combined dependencies
├── generate_all_data.py   <-- Script to create sample data for all apps
└── pages/                 <-- Streamlit multipage directory
    ├── 01_Customer_RFM.py
    ├── 02_Inventory_Forecast.py
    ├── 03_Market_Basket.py
    └── 04_HR_Attrition.py

Developed by SG Venture Consulting
Principal Consultant: Patrick Oh