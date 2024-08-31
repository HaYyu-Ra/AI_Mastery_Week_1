import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load stock data with technical indicators
file_paths = {
    'AAPL': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv',
    'AMZN': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv',
    'GOOG': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv',
    'META': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv',
    'MSFT': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv',
    'NVDA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv',
    'TSLA': r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv'
}

stock_data = {}
for symbol, path in file_paths.items():
    df = pd.read_csv(path, parse_dates=['Date'])
    stock_data[symbol] = df

# Example visualization: Plotting AAPL Close Price and 50-Day SMA
st.title('Financial News Sentiment and Stock Market Dashboard')

symbol = 'AAPL'
df = stock_data[symbol]

plt.figure(figsize=(14, 7))
plt.title(f'{symbol} - Close Price and 50-Day SMA')
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA', color='orange')
plt.legend()
st.pyplot(plt)

# Further enhancements can include sentiment analysis plots and correlation analysis results
