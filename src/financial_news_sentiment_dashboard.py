import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from datetime import datetime
import os

# File paths
OUTPUT_CSV_PATH = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\correlation_analysis.csv'
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

def load_news_data():
    """Load financial news data."""
    try:
        df = pd.read_csv(NEWS_FILE_PATH, parse_dates=['date'])
        return df
    except Exception as e:
        st.error(f"Error loading news data: {e}")
        return pd.DataFrame()

def load_stock_data(symbol):
    """Load stock price data for a specific symbol."""
    try:
        df = pd.read_csv(STOCK_DATA_PATHS[symbol], parse_dates=['Date'])
        df.rename(columns={'Date': 'date'}, inplace=True)
        return df
    except Exception as e:
        st.error(f"Error loading stock data for {symbol}: {e}")
        return pd.DataFrame()

def perform_sentiment_analysis(headline):
    """Perform sentiment analysis on the given headline."""
    analysis = TextBlob(headline)
    return analysis.sentiment.polarity

def align_datasets(news_df, stock_df):
    """Align news and stock datasets by date."""
    # Convert to date (remove time) to ensure alignment
    stock_df['date'] = stock_df['date'].dt.date
    news_df['date'] = news_df['date'].dt.date
    return news_df, stock_df

def calculate_daily_returns(stock_df):
    """Calculate daily returns from stock data."""
    stock_df['daily_return'] = stock_df['Close'].pct_change()
    return stock_df

def aggregate_sentiments(news_df):
    """Aggregate daily sentiment scores."""
    daily_sentiment = news_df.groupby('date')['sentiment'].mean().reset_index()
    return daily_sentiment

def calculate_correlation(daily_sentiment_df, stock_df):
    """Calculate correlation between daily sentiment and stock returns."""
    combined_df = pd.merge(daily_sentiment_df, stock_df[['date', 'daily_return']], on='date', how='inner')
    correlation = combined_df['sentiment'].corr(combined_df['daily_return'])
    return correlation

def load_correlation_data():
    """Load correlation analysis results."""
    try:
        df = pd.read_csv(OUTPUT_CSV_PATH)
        return df
    except Exception as e:
        st.error(f"Error loading correlation data: {e}")
        return pd.DataFrame()

def save_correlation_result(symbol, correlation):
    """Save the correlation result to a CSV file."""
    result_df = pd.DataFrame({
        'Stock Symbol': [symbol],
        'Correlation': [correlation]
    })
    if os.path.exists(OUTPUT_CSV_PATH):
        result_df.to_csv(OUTPUT_CSV_PATH, mode='a', header=False, index=False)
    else:
        result_df.to_csv(OUTPUT_CSV_PATH, index=False)

def main():
    st.title("Financial News Sentiment and Stock Movement Correlation Analysis")

    # Load news data
    news_df = load_news_data()

    if not news_df.empty:
        st.write("News data loaded successfully!")
        st.write(news_df.head())

        # Make an explicit copy to avoid SettingWithCopyWarning
        news_df = news_df.copy()

        # Perform sentiment analysis on the news data using .loc
        news_df.loc[:, 'sentiment'] = news_df['headline'].apply(perform_sentiment_analysis)

        for symbol in STOCK_DATA_PATHS.keys():
            # Load stock data for each symbol
            stock_df = load_stock_data(symbol)

            if not stock_df.empty:
                # Align datasets by date
                news_df, stock_df = align_datasets(news_df, stock_df)

                # Calculate daily stock returns
                stock_df = calculate_daily_returns(stock_df)

                # Aggregate daily sentiment scores
                daily_sentiment_df = aggregate_sentiments(news_df)

                # Calculate the correlation between sentiment and stock returns
                correlation = calculate_correlation(daily_sentiment_df, stock_df)
                st.write(f"Correlation between sentiment and {symbol} stock returns: {correlation}")

                # Save the correlation result
                save_correlation_result(symbol, correlation)
            else:
                st.warning(f"Stock data for {symbol} is empty or could not be loaded.")
    else:
        st.warning("News data is empty or could not be loaded.")

    # Load correlation data
    correlation_df = load_correlation_data()

    if not correlation_df.empty:
        st.write("Correlation Analysis Results")
        st.write(correlation_df)

        # Visualize correlation results
        plt.figure(figsize=(10, 6))
        sns.barplot(data=correlation_df, x='Stock Symbol', y='Correlation')
        plt.title('Correlation between News Sentiment and Stock Returns')
        plt.xlabel('Stock Symbol')
        plt.ylabel('Correlation')
        st.pyplot(plt)

if __name__ == "__main__":
    main()
