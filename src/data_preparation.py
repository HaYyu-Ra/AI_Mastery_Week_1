import pandas as pd

def load_stock_data(file_path):
    """Load stock price data from CSV."""
    return pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)

def preprocess_data(df):
    """Preprocess stock data: handle missing values, etc."""
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    # Example usage
    file_path = 'data/AAPL_historical_data.csv'
    data = load_stock_data(file_path)
    data = preprocess_data(data)
    print(data.head())
