import streamlit as st
import pandas as pd
from textblob import TextBlob
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sentiment Tracker", layout="wide")

st.title("🗣️ Customer Sentiment & Brand Health")
st.markdown("Analyze customer reviews and feedback to identify common pain points and brand perception.")

uploaded_file = st.file_uploader("Upload Customer Reviews (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if 'ReviewText' not in df.columns:
        st.error("CSV must contain a 'ReviewText' column.")
    else:
        # 1. Sentiment Analysis Logic
        def get_sentiment(text):
            analysis = TextBlob(str(text))
            return analysis.sentiment.polarity

        with st.spinner("Analyzing text sentiment..."):
            df['Score'] = df['ReviewText'].apply(get_sentiment)
            df['Sentiment'] = df['Score'].apply(lambda x: 'Positive' if x > 0.1 else ('Negative' if x < -0.1 else 'Neutral'))

        # 2. Key Metrics
        c1, c2, c3 = st.columns(3)
        pos_perc = (len(df[df['Sentiment'] == 'Positive']) / len(df)) * 100
        neg_perc = (len(df[df['Sentiment'] == 'Negative']) / len(df)) * 100
        
        c1.metric("Brand Health (Avg Polarity)", f"{df['Score'].mean():.2f}")
        c2.metric("Positive Feedback", f"{pos_perc:.1f}%")
        c3.metric("Negative Feedback", f"{neg_perc:.1f}%", delta_color="inverse")

        # 3. Sentiment Distribution
        st.subheader("Sentiment Distribution")
        fig_pie = px.pie(df, names='Sentiment', color='Sentiment', 
                         color_discrete_map={'Positive':'#2ecc71', 'Neutral':'#f1c40f', 'Negative':'#e74c3c'})
        st.plotly_chart(fig_pie, use_container_width=True)

        # 4. Word Cloud (Common Themes)
        st.subheader("Word Cloud: Common Themes")
        text_combined = " ".join(review for review in df.ReviewText)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_combined)
        
        fig_wc, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig_wc)

        # 5. Review Explorer
        st.subheader("Drill Down into Feedback")
        filter_sent = st.multiselect("Filter by Sentiment:", ['Positive', 'Neutral', 'Negative'], default=['Negative'])
        st.table(df[df['Sentiment'].isin(filter_sent)][['ReviewText', 'Score']].head(10))
