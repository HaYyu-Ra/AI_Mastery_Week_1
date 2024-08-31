import pandas as pd
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os

# File paths
news_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv'
historical_data_paths = {
    'AAPL': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv',
    'AMZN': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv',
    'GOOG': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv',
    'META': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv',
    'MSFT': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv',
    'NVDA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv',
    'TSLA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv'
}

# Output file paths
correlation_output_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\correlation_analysis.csv'
heatmap_output_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\sentiment_stock_correlation_heatmap.png'

# Create output directory if it doesn't exist
os.makedirs(os.path.dirname(correlation_output_path), exist_ok=True)

# Load news data
news_df = pd.read_csv(news_file_path)
news_df['date'] = pd.to_datetime(news_df['date'])

# Perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

news_df['sentiment'] = news_df['headline'].apply(get_sentiment)

# Aggregate sentiment scores by date
daily_sentiment = news_df.groupby('date')['sentiment'].mean().reset_index()

# Load stock data and calculate daily returns
def load_stock_data(symbol):
    df = pd.read_csv(historical_data_paths[symbol], parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    df['Return'] = df['Close'].pct_change()
    return df

stock_data = {symbol: load_stock_data(symbol) for symbol in historical_data_paths.keys()}

# Merge stock data with daily sentiment
merged_data = daily_sentiment.copy()
for symbol, df in stock_data.items():
    stock_returns = df['Return'].resample('D').mean().reset_index()
    stock_returns.rename(columns={'Return': 'Stock_Return'}, inplace=True)
    stock_returns['date'] = stock_returns['Date']
    merged_data = pd.merge(merged_data, stock_returns[['date', 'Stock_Return']], on='date', how='left')

# Drop rows with missing data
merged_data.dropna(inplace=True)

# Calculate correlation
correlations = {}
for symbol in stock_data.keys():
    correlation, _ = pearsonr(merged_data['sentiment'], merged_data['Stock_Return'])
    correlations[symbol] = correlation

# Save correlation results to CSV
correlation_df = pd.DataFrame(correlations.items(), columns=['Stock Symbol', 'Correlation'])
correlation_df.to_csv(correlation_output_path, index=False)

# Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(pd.DataFrame(correlations, index=['Correlation']).T, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation between News Sentiment and Stock Returns')
plt.savefig(heatmap_output_path)
plt.close()

print(f'Correlation results saved to {correlation_output_path}')
print(f'Heatmap saved to {heatmap_output_path}')
