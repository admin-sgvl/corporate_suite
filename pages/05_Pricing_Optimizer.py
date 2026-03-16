import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Price Optimizer", layout="wide")

st.title("🏷️ Dynamic Pricing Optimizer")
st.markdown("Analyze price elasticity to find the 'Sweet Spot' that maximizes total revenue.")

uploaded_file = st.file_uploader("Upload Price/Volume History (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # 1. Model Training
    # We predict Quantity (y) based on Price (X)
    X = df[['Price']].values
    y = df['Quantity'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    intercept = model.intercept_
    slope = model.coef_[0]

    # 2. Simulation Range
    min_p = int(df['Price'].min() * 0.5)
    max_p = int(df['Price'].max() * 1.5)
    price_range = np.linspace(min_p, max_p, 100).reshape(-1, 1)
    
    # Predicted Quantity and Revenue
    pred_qty = model.predict(price_range)
    pred_rev = price_range.flatten() * pred_qty

    # 3. Find Optimal Price
    opt_index = np.argmax(pred_rev)
    opt_price = price_range[opt_index][0]
    max_rev = pred_rev[opt_index]

    # 4. Visualization
    st.subheader("Revenue Maximization Curve")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=price_range.flatten(), y=pred_rev, name="Predicted Revenue", line=dict(color='green', width=4)))
    fig.add_vline(x=opt_price, line_dash="dash", line_color="red", annotation_text=f"Optimal: ${opt_price:.2f}")
    
    fig.update_layout(xaxis_title="Price ($)", yaxis_title="Total Revenue ($)", template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    # 5. Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Optimal Price", f"${opt_price:.2f}")
    c2.metric("Max Expected Revenue", f"${max_rev:,.2f}")
    
    # Calculate Elasticity (at current average price)
    avg_p = df['Price'].mean()
    elasticity = slope * (avg_p / df['Quantity'].mean())
    c3.metric("Price Elasticity", f"{elasticity:.2f}")
    
    st.info(f"💡 **Insight:** Your elasticity is {elasticity:.2f}. " + 
            ("A price increase will likely decrease total revenue (Elastic)." if elasticity < -1 
             else "You have room to raise prices without losing significant volume (Inelastic)."))
