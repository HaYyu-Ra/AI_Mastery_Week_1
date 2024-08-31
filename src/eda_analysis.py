import pandas as pd
import numpy as np
from textblob import TextBlob
import streamlit as st
import os

# File paths
NEWS_FILE_PATH = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv'
STOCK_DATA_PATHS = {
    'AAPL': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv',
    'AMZN': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv',
    'GOOG': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv',
    'META': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv',
    'MSFT': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv',
    'NVDA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv',
    'TSLA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv'
}

def perform_sentiment_analysis(text):
    """Perform sentiment analysis using TextBlob and return the sentiment score."""
    return TextBlob(text).sentiment.polarity

def calculate_daily_returns(stock_data):
    """Calculate daily returns for stock data."""
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')
    stock_data.set_index('Date', inplace=True)
    stock_data['Daily Return'] = stock_data['Close'].pct_change() * 100
    return stock_data.dropna(subset=['Daily Return'])

def parse_dates(date_series):
    """Parse dates with multiple formats."""
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%m/%d/%Y %H:%M:%S",
        "%m/%d/%Y"
    ]
    for fmt in formats:
        try:
            return pd.to_datetime(date_series, format=fmt, errors='coerce')
        except ValueError:
            continue
    return pd.to_datetime(date_series, errors='coerce')

def plot_linear_regression(x, y, title):
    """Plot linear regression with a scatter plot and fit line."""
    if len(x) > 1 and len(y) > 1:
        m, b = np.polyfit(x, y, 1)
        fit_line = m * x + b
        st.line_chart(pd.DataFrame({
            'Sentiment Score': y,
            'Daily Return': x,
            'Fit Line': fit_line
        }).set_index(x.name))
        st.write(f'Linear regression coefficients: m={m:.4f}, b={b:.4f}')
    else:
        st.warning(f'Not enough data points for visualization.')

def main():
    st.title("Financial News Sentiment Analysis Dashboard")

    # Load and preprocess news data
    if os.path.exists(NEWS_FILE_PATH):
        news_df = pd.read_csv(NEWS_FILE_PATH).drop(columns=['Unnamed: 0'], errors='ignore')
        st.write("Sample date values before parsing:")
        st.write(news_df['date'].head(20))
        
        news_df['date'] = parse_dates(news_df['date'])
        
        if news_df['date'].isnull().any():
            error_dates = news_df[news_df['date'].isnull()]['date']
            st.error("Some dates could not be parsed. Check the date format.")
            st.write("Problematic date values:")
            st.write(error_dates)

        news_df['sentiment_score'] = news_df['headline'].apply(perform_sentiment_analysis)
        st.write('Sentiment analysis complete.')

        # Prepare a DataFrame to hold correlation results
        correlation_results = []

        for symbol, stock_file_path in STOCK_DATA_PATHS.items():
            if os.path.exists(stock_file_path):
                stock_df = pd.read_csv(stock_file_path)
                stock_df = calculate_daily_returns(stock_df)
                
                # Ensure 'Date' column in stock_df is timezone-naive
                stock_df.index = stock_df.index.tz_localize(None)
                
                # Merge stock data with news data based on 'Date'
                merged_df = pd.merge(news_df, stock_df, left_on='date', right_index=True, how='inner')
                
                # Plot linear regression
                plot_linear_regression(merged_df['sentiment_score'], merged_df['Daily Return'], f'{symbol} - Sentiment vs Return')

        st.write("EDA and sentiment analysis complete.")

if __name__ == "__main__":
    main()
