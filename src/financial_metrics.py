import pynance as pn
import pandas as pd

# File paths for stock and market data
stock_data_path = 'data/AAPL_historical_data.csv'
market_data_path = 'data/market_historical_data.csv'

def load_data(file_path):
    """Load historical data from a CSV file."""
    return pd.read_csv(file_path)

def validate_data(stock_data, market_data):
    """Ensure data contains required columns."""
    if 'Close' not in stock_data.columns or 'Close' not in market_data.columns:
        raise ValueError("Both stock_data and market_data must contain a 'Close' column.")

def calculate_beta(stock_data, market_data):
    """Calculate the beta of a stock relative to the market."""
    validate_data(stock_data, market_data)
    beta = pn.ta.beta(stock_data['Close'], market_data['Close'])
    return beta

def main():
    """Main function to load data and calculate financial metrics."""
    # Load stock and market data
    stock_data = load_data(stock_data_path)
    market_data = load_data(market_data_path)
    
    # Calculate and print beta
    try:
        beta = calculate_beta(stock_data, market_data)
        print(f'Beta: {beta}')
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
