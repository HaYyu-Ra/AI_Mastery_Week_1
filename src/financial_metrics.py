import os
import pandas as pd
import numpy as np

# Set up paths
processed_data_dir = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/processed_data"

# List of stock symbols to analyze
stock_symbols = ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]

# Function to load prepared data
def load_prepared_data(stock_symbol):
    file_path = os.path.join(processed_data_dir, f"{stock_symbol}_prepared_data.csv")
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Function to calculate moving averages
def calculate_moving_averages(df, window_sizes=[20, 50, 200]):
    for window in window_sizes:
        df[f"MA_{window}"] = df['Close'].rolling(window=window).mean()
    return df

# Function to calculate daily returns
def calculate_daily_returns(df):
    df['daily_return'] = df['Close'].pct_change()
    return df

# Function to calculate volatility
def calculate_volatility(df, window=20):
    df['volatility'] = df['daily_return'].rolling(window=window).std() * np.sqrt(window)
    return df

# Function to calculate cumulative returns
def calculate_cumulative_returns(df):
    df['cumulative_return'] = (1 + df['daily_return']).cumprod() - 1
    return df

# Function to calculate all financial metrics
def calculate_financial_metrics(df):
    df = calculate_moving_averages(df)
    df = calculate_daily_returns(df)
    df = calculate_volatility(df)
    df = calculate_cumulative_returns(df)
    return df

# Run financial metrics calculation for each stock symbol
if __name__ == "__main__":
    for stock_symbol in stock_symbols:
        df = load_prepared_data(stock_symbol)
        
        # Calculate financial metrics
        df = calculate_financial_metrics(df)
        
        # Save the resulting dataframe with financial metrics
        output_file_path = os.path.join(processed_data_dir, f"{stock_symbol}_financial_metrics.csv")
        df.to_csv(output_file_path, index=False)
        
        print(f"Financial metrics calculated and saved for {stock_symbol}")
