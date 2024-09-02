import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up paths
processed_data_dir = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/processed_data"

# List of stock symbols to analyze
stock_symbols = ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]

# Function to load prepared data
def load_prepared_data(stock_symbol):
    file_path = os.path.join(processed_data_dir, f"{stock_symbol}_prepared_data.csv")
    df = pd.read_csv(file_path)
    return df

# Function to plot sentiment score distribution
def plot_sentiment_distribution(df, stock_symbol):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['sentiment_score'], bins=20, kde=True, color='blue')
    plt.title(f"Sentiment Score Distribution for {stock_symbol}")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# Function to plot stock price trends
def plot_stock_price_trend(df, stock_symbol):
    plt.figure(figsize=(14, 8))
    plt.plot(df['date'], df['Close'], label='Close Price', color='orange')
    plt.title(f"Stock Price Trend for {stock_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Close Price (USD)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Function to plot sentiment vs. stock price
def plot_sentiment_vs_stock_price(df, stock_symbol):
    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Close Price (USD)", color='orange')
    ax1.plot(df['date'], df['Close'], color='orange', label='Close Price')
    ax1.tick_params(axis='y', labelcolor='orange')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel("Sentiment Score", color='blue')
    ax2.plot(df['date'], df['sentiment_score'], color='blue', label='Sentiment Score')
    ax2.tick_params(axis='y', labelcolor='blue')
    
    plt.title(f"Sentiment Score vs. Stock Price for {stock_symbol}")
    fig.tight_layout()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Function to calculate and plot correlation between sentiment and stock price
def plot_correlation(df, stock_symbol):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[['sentiment_score', 'Close']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f"Correlation between Sentiment Score and Close Price for {stock_symbol}")
    plt.show()

# Run EDA for each stock symbol
if __name__ == "__main__":
    for stock_symbol in stock_symbols:
        df = load_prepared_data(stock_symbol)
        
        # Convert date column to datetime for plotting
        df['date'] = pd.to_datetime(df['date'])
        
        # Plot sentiment score distribution
        plot_sentiment_distribution(df, stock_symbol)
        
        # Plot stock price trend
        plot_stock_price_trend(df, stock_symbol)
        
        # Plot sentiment score vs. stock price
        plot_sentiment_vs_stock_price(df, stock_symbol)
        
        # Plot correlation between sentiment score and stock price
        plot_correlation(df, stock_symbol)
