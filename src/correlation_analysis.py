import pandas as pd
from textblob import TextBlob
import numpy as np
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

def merge_and_analyze(news_df, stock_df):
    """Merge news and stock data, and perform correlation analysis."""
    merged_df = pd.merge(news_df, stock_df, left_on='date', right_index=True, how='inner')
    merged_df['average_sentiment'] = merged_df.groupby('date')['sentiment_score'].transform('mean')
    merged_df['daily_return'] = merged_df.groupby('date')['Daily Return'].transform('mean')
    
    correlation = merged_df[['average_sentiment', 'daily_return']].dropna().corr().iloc[0, 1]
    return correlation

def main():
    if os.path.exists(NEWS_FILE_PATH):
        news_df = pd.read_csv(NEWS_FILE_PATH).drop(columns=['Unnamed: 0'], errors='ignore')
        news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')
        news_df['sentiment_score'] = news_df['headline'].apply(perform_sentiment_analysis)

        for symbol, stock_file_path in STOCK_DATA_PATHS.items():
            if os.path.exists(stock_file_path):
                stock_df = pd.read_csv(stock_file_path)
                stock_df = calculate_daily_returns(stock_df)
                
                # Ensure 'Date' column in stock_df is timezone-naive
                stock_df.index = stock_df.index.tz_localize(None)
                
                correlation = merge_and_analyze(news_df, stock_df)
                print(f'Correlation between average news sentiment and daily stock returns for {symbol}: {correlation:.4f}')

if __name__ == "__main__":
    main()
