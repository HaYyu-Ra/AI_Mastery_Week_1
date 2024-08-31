import pandas as pd
import talib
import matplotlib.pyplot as plt
from pynance import PyNance
import os

# File paths
stock_data_paths = {
    'AAPL': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv',
    'AMZN': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv',
    'GOOG': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv',
    'META': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv',
    'MSFT': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv',
    'NVDA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv',
    'TSLA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv'
}
output_directory = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs'

def calculate_indicators(df):
    df['SMA'] = talib.SMA(df['Close'], timeperiod=30)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD Signal'], df['MACD Hist'] = talib.MACD(df['Close'])
    return df

def visualize_stock_data(df, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['SMA'], label='SMA', linestyle='--')
    plt.title(f'{symbol} Stock Price and Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_directory, f'{symbol}_stock_analysis.png'))
    plt.close()

def main():
    for symbol, file_path in stock_data_paths.items():
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df['Date'] = pd.to_datetime(df['Date'])
            df = calculate_indicators(df)
            visualize_stock_data(df, symbol)
            print(f'Quantitative analysis and visualization for {symbol} completed.')
        else:
            print(f'Stock data file not found for {symbol} at {file_path}')

if __name__ == "__main__":
    main()
