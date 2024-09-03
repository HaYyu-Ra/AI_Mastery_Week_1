import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import talib

def load_stock_data(file_paths):
    stock_data = {}
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
        if 'Close' in df.columns:
            df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
        symbol = file_path.split("\\")[-1].split('_')[0]
        stock_data[symbol] = df
    return stock_data

def calculate_technical_indicators(df):
    df['SMA'] = talib.SMA(df['Close'])
    return df

def visualize_data(df, symbol):
    if 'Date' in df.columns and 'Close' in df.columns:
        st.subheader(f'{symbol} Stock Price Over Time')
        st.line_chart(df.set_index('Date')['Close'], use_container_width=True)
    else:
        st.write('Date or Close column not found for visualization.')
