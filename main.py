import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from textblob import TextBlob
import numpy as np
import talib
from datetime import datetime

# Define data paths
DATA_PATH = 'data/sentiment_analysis.csv'
STOCK_DATA_PATHS = {
    'AAPL': 'data/AAPL_historical_data.csv',
    'AMZN': 'data/AMZN_historical_data.csv',
    'GOOG': 'data/GOOG_historical_data.csv',
    'META': 'data/META_historical_data.csv',
    'MSFT': 'data/MSFT_historical_data.csv',
    'NVDA': 'data/NVDA_historical_data.csv',
    'TSLA': 'data/TSLA_historical_data.csv',
}

def load_data():
    try:
        news_df = pd.read_csv(DATA_PATH)
        news_df['Date'] = pd.to_datetime(news_df['Date'])
        news_df['Sentiment'] = news_df['Headline'].apply(lambda x: TextBlob(x).sentiment.polarity)

        stock_data = {}
        for stock, path in STOCK_DATA_PATHS.items():
            df = pd.read_csv(path)
            df['Date'] = pd.to_datetime(df['Date'])
            df['Daily_Return'] = df['Close'].pct_change() * 100
            stock_data[stock] = df

        return news_df, stock_data
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def render_dashboard(stock):
    news_df, stock_data = load_data()
    if news_df is None or stock_data is None:
        st.error("Error loading data.")
        return

    if stock not in stock_data:
        st.error("Selected stock data is not available.")
        return

    stock_df = stock_data[stock]

    st.header("Exploratory Data Analysis (EDA)")
    st.subheader("Sentiment Analysis on Headlines")
    sentiment_counts = news_df['Sentiment'].value_counts()
    st.bar_chart(sentiment_counts)

    st.subheader("Headline Length Distribution")
    news_df['Headline_Length'] = news_df['Headline'].apply(len)
    st.write("Distribution of Headline Lengths")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(news_df['Headline_Length'], kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Publication Trends Over Time")
    publication_trends = news_df.groupby('Date').size()
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(publication_trends.index, publication_trends, label='Number of Articles')
    ax.set_title('Publication Trends Over Time')
    st.pyplot(fig)

    st.header("Time Series Analysis")
    st.subheader("Stock Price Over Time")
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(stock_df['Date'], stock_df['Close'], label='Close Price')
    st.pyplot(fig)

    st.subheader("Stock Price Volatility")
    rolling_volatility = stock_df['Close'].rolling(window=30).std()
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(stock_df['Date'], rolling_volatility, label='30-Day Rolling Volatility', color='red')
    st.pyplot(fig)

    st.header("Quantitative Analysis")
    st.subheader("Technical Indicators")
    stock_df['SMA'] = talib.SMA(stock_df['Close'], timeperiod=30)
    stock_df['RSI'] = talib.RSI(stock_df['Close'], timeperiod=14)
    stock_df['MACD'], stock_df['MACD_Signal'], _ = talib.MACD(stock_df['Close'])

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(stock_df['Date'], stock_df['Close'], label='Close Price')
    ax.plot(stock_df['Date'], stock_df['SMA'], label='30-Day SMA')
    st.pyplot(fig)

    st.subheader("RSI and MACD Indicators")
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(stock_df['Date'], stock_df['RSI'], label='RSI')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(stock_df['Date'], stock_df['MACD'], label='MACD')
    ax.plot(stock_df['Date'], stock_df['MACD_Signal'], label='MACD Signal')
    st.pyplot(fig)

    st.header("Correlation Between News and Stock Movement")
    merged_df = pd.merge(stock_df, news_df, on='Date', how='inner')
    daily_sentiments = merged_df.groupby('Date')['Sentiment'].mean()
    daily_returns = merged_df.groupby('Date')['Daily_Return'].mean()
    correlation = daily_sentiments.corr(daily_returns)
    st.write(f'**Correlation between news sentiment and stock returns: {correlation:.2f}**')

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(daily_sentiments.index, daily_sentiments, label='Average Daily Sentiment', color='blue')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(daily_returns.index, daily_returns, label='Daily Returns', color='orange')
    st.pyplot(fig)

if __name__ == "__main__":
    st.title('Financial Dashboard')
    stock = st.selectbox("Select a Stock:", list(STOCK_DATA_PATHS.keys()))
    if stock:
        render_dashboard(stock)
