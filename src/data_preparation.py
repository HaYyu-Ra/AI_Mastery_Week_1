import pandas as pd
import os

# Define paths for raw analyst ratings and historical data
raw_analyst_ratings_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv"
historical_data_paths = {
    'AAPL': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv",
    'AMZN': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv",
    'GOOG': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv",
    'META': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv",
    'MSFT': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv",
    'NVDA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv",
    'TSLA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv"
}
prepared_data_dir = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\prepared_data"

if not os.path.exists(prepared_data_dir):
    os.makedirs(prepared_data_dir)

def load_data(file_path):
    """
    Load data from the specified file path.
    """
    return pd.read_csv(file_path)

def preprocess_stock_data(df):
    """
    Preprocess stock data for analysis.
    """
    # Ensure the Date column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Sort data by Date
    df = df.sort_values(by='Date')
    
    # Drop any rows with missing values in critical columns
    df = df.dropna(subset=['Date', 'Close'])
    
    return df

def preprocess_analyst_ratings(df):
    """
    Preprocess raw analyst ratings data.
    """
    # Ensure the Date column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Drop rows with missing values in critical columns
    df = df.dropna(subset=['Date', 'Rating'])
    
    return df

def main():
    # Load and preprocess raw analyst ratings data
    raw_analyst_ratings_df = load_data(raw_analyst_ratings_path)
    raw_analyst_ratings_df = preprocess_analyst_ratings(raw_analyst_ratings_df)
    raw_analyst_ratings_df.to_csv(os.path.join(prepared_data_dir, 'preprocessed_analyst_ratings.csv'), index=False)
    
    for stock, path in historical_data_paths.items():
        # Load and preprocess historical stock data
        stock_df = load_data(path)
        stock_df = preprocess_stock_data(stock_df)
        
        # Save the preprocessed stock data
        stock_df.to_csv(os.path.join(prepared_data_dir, f'preprocessed_{stock}_historical_data.csv'), index=False)
    
    print(f"Preprocessed data saved in {prepared_data_dir}")

if __name__ == "__main__":
    main()
