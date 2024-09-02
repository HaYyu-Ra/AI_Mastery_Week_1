import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import talib as ta
from textblob import TextBlob
import streamlit as st

# File paths
RAW_DATA_PATH = os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "raw_analyst_ratings.csv")
HISTORICAL_DATA_PATHS = {
    "AAPL": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "AAPL_historical_data.csv"),
    "AMZN": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "AMZN_historical_data.csv"),
    "GOOG": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "GOOG_historical_data.csv"),
    "META": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "META_historical_data.csv"),
    "MSFT": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "MSFT_historical_data.csv"),
    "NVDA": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "NVDA_historical_data.csv"),
    "TSLA": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "TSLA_historical_data.csv"),
}

@st.cache_data
def load_news_data():
    return pd.read_csv(RAW_DATA_PATH)

@st.cache_data
def load_stock_data(ticker):
    return pd.read_csv(HISTORICAL_DATA_PATHS[ticker])

# Sentiment Analysis Function
def sentiment_analysis(headline):
    analysis = TextBlob(headline)
    return analysis.sentiment.polarity

# Calculate Technical Indicators using TA-Lib
def calculate_technical_indicators(df):
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    return df

# Visualize Data
def visualize_stock_data(df, ticker):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df['Date'], df['Close'], label='Close Price')
    ax.plot(df['Date'], df['SMA_20'], label='20-Day SMA')
    ax.set_title(f"{ticker} Stock Price and Technical Indicators")
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid()
    return fig

# Correlation Analysis
def correlation_analysis(sentiments, stock_returns):
    correlation = np.corrcoef(sentiments, stock_returns)[0, 1]
    return correlation

# Streamlit Dashboard
st.title("Financial News and Stock Market Dashboard")

# Load and Display News Data
news_data = load_news_data()
st.subheader("News Data")
st.dataframe(news_data.head())  # Display only the first few rows to avoid large data issues

# Perform Sentiment Analysis
news_data['Sentiment'] = news_data['headline'].apply(sentiment_analysis)
st.subheader("Sentiment Analysis")
st.dataframe(news_data[['headline', 'Sentiment']].head())  # Display only the first few rows

# Load and Analyze Stock Data
selected_stock = st.selectbox("Select Stock Symbol", list(HISTORICAL_DATA_PATHS.keys()))
stock_data = load_stock_data(selected_stock)

# Ensure 'Date' columns are in datetime format
news_data['Date'] = pd.to_datetime(news_data['date'], errors='coerce')
stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')

# Double-check the data types
st.write("News Data 'Date' column type:", news_data['Date'].dtype)
st.write("Stock Data 'Date' column type:", stock_data['Date'].dtype)

# Calculate Technical Indicators
stock_data = calculate_technical_indicators(stock_data)

# Visualize Stock Data
st.subheader(f"{selected_stock} Stock Data and Technical Indicators")
st.pyplot(visualize_stock_data(stock_data, selected_stock))

# Correlation Analysis between Sentiment and Stock Movements
st.subheader("Correlation Analysis")

# Merge data and ensure correct data types
merged_data = pd.merge(
    news_data[['Date', 'Sentiment']].dropna(),
    stock_data[['Date', 'Close']].dropna(),
    on='Date',
    how='inner'
)

merged_data['Daily_Return'] = merged_data['Close'].pct_change()
merged_data = merged_data.dropna()

correlation = correlation_analysis(merged_data['Sentiment'], merged_data['Daily_Return'])
st.write(f"The correlation between news sentiment and daily stock returns for {selected_stock} is: {correlation:.4f}")

# Investment Strategy Recommendation
st.subheader("Investment Strategy Recommendation")
if correlation > 0.1:
    st.write("Positive correlation detected. Consider buying on positive sentiment.")
elif correlation < -0.1:
    st.write("Negative correlation detected. Consider selling on negative sentiment.")
else:
    st.write("No strong correlation detected. No clear investment strategy based on sentiment analysis.")
