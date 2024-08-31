import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

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
    """Perform sentiment analysis using TextBlob."""
    return TextBlob(text).sentiment.polarity

def plot_sentiment_vs_price(merged_df, symbol):
    """Plot sentiment score vs. stock price."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sentiment_score', y='Close', data=merged_df)
    plt.title(f'Sentiment vs {symbol} Stock Price')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Stock Price')
    plt.show()

def main():
    """Main function to analyze news sentiment vs. stock prices."""
    news_df = pd.read_csv(NEWS_FILE_PATH)
    
    # Make sure the data is copied to avoid SettingWithCopyWarning
    news_df = news_df.copy()
    
    # Perform sentiment analysis
    news_df['sentiment_score'] = news_df['headline'].apply(perform_sentiment_analysis)

    # Ensure the 'date' column is in datetime format and remove timezone info
    news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce').dt.tz_localize(None)

    for symbol, stock_file_path in STOCK_DATA_PATHS.items():
        stock_df = pd.read_csv(stock_file_path)
        stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
        stock_df.set_index('Date', inplace=True)
        stock_df['Daily Return'] = stock_df['Close'].pct_change() * 100
        
        # Merge stock and news data
        merged_df = pd.merge(news_df, stock_df, left_on='date', right_index=True, how='inner')
        
        # Plot sentiment vs. stock price
        plot_sentiment_vs_price(merged_df, symbol)

if __name__ == "__main__":
    main()
