import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths for data files
sentiment_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv"
historical_data_paths = {
    'AAPL': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv",
    'AMZN': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv",
    'GOOG': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv",
    'META': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv",
    'MSFT': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv",
    'NVDA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv",
    'TSLA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv"
}

def load_data():
    """
    Load sentiment and historical stock data from CSV files.
    """
    sentiment_df = pd.read_csv(sentiment_data_path)
    historical_data = {stock: pd.read_csv(path) for stock, path in historical_data_paths.items()}
    return sentiment_df, historical_data

def plot_sentiment(sentiment_df):
    """
    Plot the sentiment scores over time.
    """
    st.subheader("Sentiment Analysis Over Time")
    sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date'])
    sentiment_df.set_index('Date', inplace=True)
    
    st.line_chart(sentiment_df[['Sentiment_Score']], use_container_width=True)

def plot_stock_data(historical_data):
    """
    Plot stock data with technical indicators.
    """
    st.subheader("Stock Data with Technical Indicators")
    stock = st.selectbox("Select Stock", list(historical_data.keys()))
    
    df = historical_data[stock]
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    st.line_chart(df[['Close']], use_container_width=True)
    
    if 'SMA_20' in df.columns and 'SMA_50' in df.columns:
        st.line_chart(df[['Close', 'SMA_20', 'SMA_50']], use_container_width=True)
    
    if 'EMA_20' in df.columns and 'EMA_50' in df.columns:
        st.line_chart(df[['Close', 'EMA_20', 'EMA_50']], use_container_width=True)
    
    if 'RSI' in df.columns:
        st.line_chart(df[['RSI']], use_container_width=True)
    
    if 'MACD' in df.columns and 'MACD_signal' in df.columns:
        st.line_chart(df[['MACD', 'MACD_signal']], use_container_width=True)
    
    if 'upper_band' in df.columns and 'middle_band' in df.columns and 'lower_band' in df.columns:
        st.line_chart(df[['Close', 'upper_band', 'middle_band', 'lower_band']], use_container_width=True)

def main():
    st.title("Financial News Sentiment and Stock Dashboard")
    
    sentiment_df, historical_data = load_data()
    
    plot_sentiment(sentiment_df)
    plot_stock_data(historical_data)

if __name__ == "__main__":
    main()
