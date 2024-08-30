# quantitative_analysis.py
import pandas as pd
import talib
import matplotlib.pyplot as plt
from pynance import Stock

# Load stock price data
stock_df = pd.read_csv('data/stock_data.csv')

# Apply TA-Lib indicators
stock_df['SMA'] = talib.SMA(stock_df['Close'], timeperiod=30)
stock_df['RSI'] = talib.RSI(stock_df['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(stock_df['Close'])
stock_df['MACD'] = macd
stock_df['MACD_signal'] = macdsignal

# Use PyNance for financial metrics
stock = Stock('AAPL')
financials = stock.financials
print(financials)

# Plot stock price with indicators
plt.figure(figsize=(14,7))
plt.plot(stock_df['Close'], label='Close Price')
plt.plot(stock_df['SMA'], label='SMA')
plt.title('Stock Price with Moving Average')
plt.legend()
plt.show()
