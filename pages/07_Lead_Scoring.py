import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import plotly.express as px

st.set_page_config(page_title="Sales Lead Scorer", layout="wide")

st.title("🎯 Predictive Lead Scoring")
st.markdown("Rank your sales leads by conversion probability to maximize sales team efficiency.")

uploaded_file = st.file_uploader("Upload Historical Lead Data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # 1. Check for target column 'Converted' (1 = Yes, 0 = No)
    if 'Converted' not in df.columns:
        st.error("CSV must contain a 'Converted' column for training.")
    else:
        # Prep data (handle categorical variables)
        df_encoded = pd.get_dummies(df.drop('LeadID', axis=1), drop_first=True)
        
        X = df_encoded.drop('Converted', axis=1)
        y = df_encoded['Converted']
        
        # 2. Train Model
        model = LogisticRegression(max_iter=1000)
        model.fit(X, y)
        
        # 3. Predict on current (unconverted) leads
        # We assume unconverted leads are rows where we don't know the outcome yet
        probs = model.predict_proba(X)[:, 1]
        df['Conversion_Probability'] = (probs * 100).round(2)
        
        # 4. Display Dashboard
        c1, c2 = st.columns([1, 2])
        
        with c1:
            st.subheader("Top Conversion Drivers")
            # Feature Importance
            importance = pd.DataFrame({
                'Feature': X.columns,
                'Weight': model.coef_[0]
            }).sort_values('Weight', ascending=False)
            st.dataframe(importance, use_container_width=True)
            
        with c2:
            st.subheader("Lead Priority List")
            # Filter for leads that haven't converted yet (mock logic)
            priority_list = df.sort_values('Conversion_Probability', ascending=False).head(20)
            
            def color_score(val):
                color = 'green' if val > 70 else ('orange' if val > 40 else 'red')
                return f'color: {color}'

            st.dataframe(priority_list[['LeadID', 'Source', 'Conversion_Probability']].style.applymap(color_score, subset=['Conversion_Probability']), use_container_width=True)

        # 5. Funnel Visualization
        st.divider()
        st.subheader("Lead Quality Distribution")
        fig_hist = px.histogram(df, x="Conversion_Probability", nbins=20, 
                               title="Distribution of Lead Scores",
                               color_discrete_sequence=['#636EFA'])
        st.plotly_chart(fig_hist, use_container_width=True)
