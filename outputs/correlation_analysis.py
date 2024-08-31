import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import os
from textblob import TextBlob

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

def load_data():
    """Load news and stock data."""
    try:
        # Load news data
        news_data = pd.read_csv(NEWS_FILE_PATH)
        # Load stock data
        stock_data = {symbol: pd.read_csv(path, parse_dates=['Date'], index_col='Date') for symbol, path in STOCK_DATA_PATHS.items()}
        return news_data, stock_data
    except FileNotFoundError as e:
        st.error(f'File not found: {e}')
        raise

def calculate_sentiment(text):
    """Calculate sentiment of a text using TextBlob."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze_sentiment(news_data):
    """Analyze sentiment for news data and merge with stock data."""
    news_data['Sentiment'] = news_data['Title'].apply(calculate_sentiment)
    return news_data

def calculate_correlations(news_data, stock_data):
    """Calculate correlations between news sentiment and stock data."""
    results = []
    for symbol, df in stock_data.items():
        if 'Sentiment' in news_data.columns:
            df['Sentiment'] = news_data['Sentiment'].reindex(df.index, method='ffill')
            df['Return'] = df['Close'].pct_change()
            correlation = df[['Sentiment', 'Return']].dropna().corr().iloc[0, 1]
            results.append({'Symbol': symbol, 'Correlation': correlation})
    return pd.DataFrame(results)

def plot_correlation_heatmap(correlation_df):
    """Plot heatmap of the correlation between news sentiment and stock returns."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_df.set_index('Symbol').T, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation between News Sentiment and Stock Returns')
    plt.savefig(r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\plots\sentiment_stock_correlation_heatmap.png')
    plt.close()

def main():
    """Main function to run the analysis."""
    try:
        # Load data
        news_data, stock_data = load_data()
        
        # Analyze sentiment
        news_data = analyze_sentiment(news_data)
        
        # Calculate correlations
        correlation_df = calculate_correlations(news_data, stock_data)
        correlation_df.to_csv(OUTPUT_CSV_PATH, index=False)
        st.write(f'Correlation analysis results saved to {OUTPUT_CSV_PATH}')
        
        # Plot heatmap
        plot_correlation_heatmap(correlation_df)
        st.image(r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\plots\sentiment_stock_correlation_heatmap.png', caption='Sentiment vs. Stock Returns Correlation Heatmap')

    except Exception as e:
        st.error(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
