import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Corporate Intelligence Suite",
    page_icon="🏛️",
    layout="wide"
)

# --- HEADER ---
st.title("🏛️ Corporate Intelligence & Predictive Suite")
st.markdown("""
Welcome to the **Master Analytics Portal**. This suite integrates eight high-impact Data Science 
applications to drive data-driven decision-making across all core business functions.
---
""")

# --- NAVIGATION INFO ---
st.sidebar.success("Select a module above to begin.")
st.sidebar.divider()
st.sidebar.markdown("""
### 🛡️ Data Privacy
All processing is done **in-memory**. 
No data is stored on our servers.
""")

# --- APP GRID ---
# Using columns to create a "Dashboard" feel
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)
row3_col1, row3_col2 = st.columns(2)
row4_col1, row4_col2 = st.columns(2)

# --- ROW 1: Operations & Marketing ---
with row1_col1:
    st.subheader("🎯 01. Customer RFM Engine")
    st.info("**Value:** Maximizes Marketing ROI by segmenting customers into behavioral groups (Champions vs. At-Risk).")

with row1_col2:
    st.subheader("📈 02. Inventory Forecasting")
    st.info("**Value:** Prevents stockouts and reduces waste by predicting demand and optimal reorder points.")

# --- ROW 2: Sales Strategy ---
with row2_col1:
    st.subheader("🛒 03. Market Basket Analysis")
    st.info("**Value:** Increases Average Order Value (AOV) by discovering which products are frequently bought together.")

with row2_col2:
    st.subheader("🛡️ 04. HR Attrition Early Warning")
    st.info("**Value:** Reduces turnover costs by identifying 'flight risk' employees before they resign.")

# --- ROW 3: Finance & Revenue ---
with row3_col1:
    st.subheader("🏷️ 05. Dynamic Pricing Optimizer")
    st.info("**Value:** Finds the 'Sweet Spot' price to maximize total revenue based on historical demand elasticity.")

with row3_col2:
    st.subheader("🗣️ 06. Sentiment & Brand Tracker")
    st.info("**Value:** Monitors brand health by analyzing customer reviews to identify product flaws or PR wins.")

# --- ROW 4: Sales Efficiency & Audit ---
with row4_col1:
    st.subheader("🎯 07. Predictive Lead Scoring")
    st.info("**Value:** Ranks sales prospects by conversion probability so teams can focus on the 'hottest' leads.")

with row4_col2:
    st.subheader("🔍 08. Anomaly & Fraud Detector")
    st.info("**Value:** Protects revenue by flagging unusual transactions, duplicate invoices, or potential fraud.")

st.divider()

# --- FOOTER ---
st.markdown("""
### 🚀 Getting Started
1. Prepare your data in **CSV format**.
2. Navigate to the desired tool using the **sidebar on the left**.
3. Upload your file to see real-time predictive insights.
""")

st.caption("© 2026 SG Venture Consulting - Data Science Suite | Version 2.0.0")
