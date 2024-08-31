import pandas as pd
import talib as ta
import matplotlib.pyplot as plt

# Define file paths
file_paths = {
    'AAPL': 'data/AAPL_historical_data.csv',
    'AMZN': 'data/AMZN_historical_data.csv',
    'GOOG': 'data/GOOG_historical_data.csv',
    'META': 'data/META_historical_data.csv',
    'MSFT': 'data/MSFT_historical_data.csv',
    'NVDA': 'data/NVDA_historical_data.csv',
    'TSLA': 'data/TSLA_historical_data.csv'
}

# Load data into pandas DataFrame
stock_data = {}
for symbol, path in file_paths.items():
    df = pd.read_csv(path, parse_dates=['Date'])
    stock_data[symbol] = df

# Display a sample of the loaded data
print(stock_data['AAPL'].head())
for symbol, df in stock_data.items():
    df['SMA_50'] = ta.SMA(df['Close'], timeperiod=50)
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], _ = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

# Save the updated data
for symbol, df in stock_data.items():
    df.to_csv(f'data/{symbol}_technical_indicators.csv', index=False)
# Visualize technical indicators
for symbol, df in stock_data.items():
    plt.figure(figsize=(14,7))
    plt.title(f'{symbol} - Moving Average, RSI, and MACD')
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA', color='orange')
    plt.legend()
    plt.show()
