import matplotlib.pyplot as plt
import pandas as pd
import os

# File paths
stock_data_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv'

def load_stock_data(file_path):
    """Load stock data from a CSV file."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    else:
        raise FileNotFoundError(f'Stock data file not found at {file_path}')

def plot_moving_averages(df, symbol):
    """Plot the closing price and moving averages."""
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price')
    if 'SMA' in df.columns:
        plt.plot(df['SMA'], label='SMA', linestyle='--')
    if 'EMA' in df.columns:
        plt.plot(df['EMA'], label='EMA', linestyle='-.')
    plt.title(f'{symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/plots/{symbol}_moving_averages.png')
    plt.close()

def plot_rsi(df, symbol):
    """Plot the Relative Strength Index (RSI)."""
    plt.figure(figsize=(14, 7))
    if 'RSI' in df.columns:
        plt.plot(df['RSI'], label='RSI', color='orange')
        plt.axhline(70, linestyle='--', color='red', label='Overbought Threshold')
        plt.axhline(30, linestyle='--', color='green', label='Oversold Threshold')
    plt.title(f'{symbol} Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/plots/{symbol}_RSI.png')
    plt.close()

def plot_macd(df, symbol):
    """Plot the Moving Average Convergence Divergence (MACD) and related indicators."""
    plt.figure(figsize=(14, 7))
    if 'MACD' in df.columns:
        plt.plot(df['MACD'], label='MACD', color='blue')
        if 'MACD_Signal' in df.columns:
            plt.plot(df['MACD_Signal'], label='MACD Signal', color='red')
        if 'MACD_Hist' in df.columns:
            plt.bar(df.index, df['MACD_Hist'], label='MACD Histogram', color='gray', alpha=0.5)
    plt.title(f'{symbol} MACD')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/plots/{symbol}_MACD.png')
    plt.close()

def main():
    try:
        # Load stock data
        stock_data = load_stock_data(stock_data_path)
        
        # Plot visualizations
        symbol = 'AAPL'  # Example symbol
        plot_moving_averages(stock_data, symbol)
        plot_rsi(stock_data, symbol)
        plot_macd(stock_data, symbol)
        
        print(f'Visualizations for {symbol} completed.')
        
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
