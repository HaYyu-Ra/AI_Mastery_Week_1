import talib

# Calculate moving averages
stock_data['SMA'] = talib.SMA(stock_data['Close'], timeperiod=30)
stock_data['EMA'] = talib.EMA(stock_data['Close'], timeperiod=30)

# Calculate RSI
stock_data['RSI'] = talib.RSI(stock_data['Close'], timeperiod=14)

# Calculate MACD
stock_data['MACD'], stock_data['MACD_Signal'], stock_data['MACD_Hist'] = talib.MACD(stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
