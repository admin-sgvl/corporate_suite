import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import plotly.express as px

st.set_page_config(page_title="HR Flight Risk Predictor", layout="wide")

st.title("🛡️ Employee Attrition Early Warning System")
st.markdown("Identify which employees are most likely to leave and understand the 'Why' behind it.")

uploaded_file = st.file_uploader("Upload HR Historical Data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # 1. Data Prep: Convert text categories to numbers (Simple Encoding)
    # We assume 'Attrition' is our Target (1 = Left, 0 = Stayed)
    df_numeric = pd.get_dummies(df, drop_first=True)
    
    if 'Attrition' not in df.columns:
        st.error("The CSV must contain an 'Attrition' column (1 for left, 0 for stayed) to train the model.")
    else:
        # 2. Training the Model
        X = df_numeric.drop('Attrition', axis=1)
        y = df_numeric['Attrition']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # 3. Sidebar: What-If Analysis
        st.sidebar.header("🔍 Individual Employee Check")
        st.sidebar.info("Input employee stats to see their individual risk score.")
        
        # 4. Feature Importance (The 'Why')
        st.subheader("📊 Key Drivers of Turnover")
        importances = pd.DataFrame({
            'Feature': X.columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False).head(10)
        
        fig = px.bar(importances, x='Importance', y='Feature', orientation='h', 
                     title="Top 10 Reasons People Leave (Model Insights)")
        st.plotly_chart(fig, use_container_width=True)

        # 5. Risk List
        st.subheader("⚠️ High Risk Employee Watchlist")
        # Predict probability of leaving for all current employees (Attrition = 0)
        current_employees = df_numeric[df_numeric['Attrition'] == 0].drop('Attrition', axis=1)
        probs = model.predict_proba(current_employees)[:, 1]
        
        results = df[df['Attrition'] == 0].copy()
        results['Risk_Score'] = (probs * 100).round(2)
        
        watchlist = results.sort_values('Risk_Score', ascending=False).head(20)
        st.dataframe(watchlist[['EmployeeID', 'Department', 'MonthlyIncome', 'Risk_Score']], use_container_width=True)
