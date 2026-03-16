import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import plotly.express as px

st.set_page_config(page_title="Expense Auditor", layout="wide")

st.title("🔍 Anomalous Expense & Fraud Detector")
st.markdown("Automated auditing to identify unusual transactions, potential fraud, or billing errors.")

uploaded_file = st.file_uploader("Upload Expense/Transaction Data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # 1. Feature Selection
    # We focus on numerical values like Amount and Frequency
    features = ['Amount', 'VendorRating'] # Mock columns
    
    if not all(col in df.columns for col in features):
        st.error(f"CSV must contain {features} columns.")
    else:
        # 2. Train Isolation Forest
        # Contamination is the estimated % of outliers (e.g., 2%)
        model = IsolationForest(contamination=0.02, random_state=42)
        df['Anomaly_Score'] = model.fit_predict(df[features])
        
        # Mapping: -1 is Anomaly, 1 is Normal
        df['Status'] = df['Anomaly_Score'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')

        # 3. Visualization
        st.subheader("Transaction Outlier Analysis")
        fig = px.scatter(df, x="Amount", y="VendorRating", color="Status",
                         color_discrete_map={'Normal':'#636EFA', 'Anomaly':'#EF553B'},
                         hover_data=['TransactionID', 'Category'],
                         title="Expense Distribution (Red = Flagged for Audit)")
        st.plotly_chart(fig, use_container_width=True)

        # 4. The Audit List
        st.divider()
        st.subheader("🚩 Top Flagged Transactions")
        anomalies = df[df['Status'] == 'Anomaly'].sort_values('Amount', ascending=False)
        
        st.write(f"The AI has flagged **{len(anomalies)}** transactions for manual review.")
        st.dataframe(anomalies[['TransactionID', 'Category', 'Amount', 'VendorRating', 'Status']], use_container_width=True)

        # 5. Export for Finance Team
        st.download_button(
            label="Export Audit List",
            data=anomalies.to_csv(index=False).encode('utf-8'),
            file_name='audit_required.csv',
            mime='text/csv',
        )
