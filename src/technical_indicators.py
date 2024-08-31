import talib
import pandas as pd

def calculate_moving_averages(stock_data):
    """Calculate Simple Moving Average (SMA) and Exponential Moving Average (EMA)."""
    stock_data['SMA'] = talib.SMA(stock_data['Close'], timeperiod=30)
    stock_data['EMA'] = talib.EMA(stock_data['Close'], timeperiod=30)
    return stock_data

def calculate_rsi(stock_data):
    """Calculate the Relative Strength Index (RSI)."""
    stock_data['RSI'] = talib.RSI(stock_data['Close'], timeperiod=14)
    return stock_data

def calculate_macd(stock_data):
    """Calculate the Moving Average Convergence Divergence (MACD) and its components."""
    stock_data['MACD'], stock_data['MACD_Signal'], stock_data['MACD_Hist'] = talib.MACD(
        stock_data['Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    return stock_data

def calculate_technical_indicators(stock_data):
    """Calculate all technical indicators."""
    stock_data = calculate_moving_averages(stock_data)
    stock_data = calculate_rsi(stock_data)
    stock_data = calculate_macd(stock_data)
    return stock_data

if __name__ == "__main__":
    # Example usage
    # Load stock data
    file_path = 'data/AAPL_historical_data.csv'
    stock_data = pd.read_csv(file_path)
    
    # Calculate technical indicators
    stock_data = calculate_technical_indicators(stock_data)
    
    # Save the updated data with technical indicators
    stock_data.to_csv('data/AAPL_with_indicators.csv', index=False)
    print("Technical indicators calculated and saved.")
