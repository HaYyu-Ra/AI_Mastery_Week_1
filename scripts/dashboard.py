# dashboard.py
import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv('data/financial_news.csv')

# Dashboard
st.title('Financial News Sentiment Dashboard')

# Display data
st.write(df.head())

# Plot sentiment distribution
st.subheader('Sentiment Distribution')
st.bar_chart(df['sentiment'].value_counts())
