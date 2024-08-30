import matplotlib.pyplot as plt

# Plot the closing price and moving averages
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['SMA'], label='SMA')
plt.plot(stock_data['EMA'], label='EMA')
plt.title('Stock Price and Moving Averages')
plt.legend()
plt.show()

# Plot RSI
plt.figure(figsize=(14, 7))
plt.plot(stock_data['RSI'], label='RSI')
plt.title('Relative Strength Index (RSI)')
plt.legend()
plt.show()

# Plot MACD
plt.figure(figsize=(14, 7))
plt.plot(stock_data['MACD'], label='MACD')
plt.plot(stock_data['MACD_Signal'], label='MACD Signal')
plt.bar(stock_data.index, stock_data['MACD_Hist'], label='MACD Histogram')
plt.title('MACD')
plt.legend()
plt.show()
