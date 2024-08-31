import pandas as pd
from textblob import TextBlob
import os

# File paths
news_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv'
stock_data_paths = {
    'AAPL': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv',
    'AMZN': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv',
    'GOOG': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv',
    'META': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv',
    'MSFT': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv',
    'NVDA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv',
    'TSLA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv'
}
output_csv_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\correlation_analysis.csv'

def perform_sentiment_analysis(text):
    """Perform sentiment analysis using TextBlob and return the sentiment score."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def calculate_daily_returns(stock_data):
    """Calculate daily returns for stock data."""
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.set_index('Date', inplace=True)
    stock_data['Daily Return'] = stock_data['Close'].pct_change() * 100
    stock_data = stock_data.dropna(subset=['Daily Return'])
    return stock_data

def main():
    if os.path.exists(news_file_path):
        # Load news data
        news_df = pd.read_csv(news_file_path)
        news_df['date'] = pd.to_datetime(news_df['date'])
        news_df['sentiment_score'] = news_df['headline'].apply(perform_sentiment_analysis)
        print('Sentiment analysis complete.')

        # Prepare a DataFrame to hold correlation results
        correlation_results = []

        for symbol, stock_file_path in stock_data_paths.items():
            if os.path.exists(stock_file_path):
                # Load stock data
                stock_df = pd.read_csv(stock_file_path)
                stock_df = calculate_daily_returns(stock_df)
                
                # Merge stock data with news data
                merged_df = pd.merge(news_df, stock_df, how='inner', left_on='date', right_index=True)
                
                # Compute correlation
                correlation = merged_df[['sentiment_score', 'Daily Return']].corr().iloc[0, 1]
                correlation_results.append({
                    'Stock Symbol': symbol,
                    'Correlation': correlation
                })

        # Convert results to DataFrame and save to CSV
        results_df = pd.DataFrame(correlation_results)
        results_df.to_csv(output_csv_path, index=False)
        print(f'Correlation analysis results saved to {output_csv_path}')
    else:
        print(f'News data file not found at {news_file_path}')

if __name__ == "__main__":
    main()
