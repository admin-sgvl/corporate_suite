import streamlit as st

st.set_page_config(page_title="Corporate Intelligence Suite", layout="wide")

st.title("🏛️ Corporate Intelligence & Predictive Suite")
st.markdown("---")

st.header("Welcome to the Analytics Portal")
st.write("Select a specialized tool from the sidebar to begin your data-driven decision-making process.")

# Professional layout with 2x2 cards
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Customer RFM")
    st.info("**Benefit:** Maximizes Marketing ROI by identifying high-value customers and win-back opportunities.")
    
    st.subheader("📈 Inventory Forecast")
    st.info("**Benefit:** Prevents stockouts and reduces holding costs by predicting future demand patterns.")

with col2:
    st.subheader("🛒 Market Basket")
    st.info("**Benefit:** Increases Average Order Value (AOV) by discovering which products should be bundled.")
    
    st.subheader("🛡️ HR Attrition")
    st.info("**Benefit:** Reduces recruitment costs (up to 2x salary) by flagging high-performing flight risks.")

st.divider()
st.caption("Developed by the Data Science Team | Internal Use Only")