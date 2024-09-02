import pandas as pd
import talib as ta

# Define paths for raw analyst ratings data and historical stock data
data_paths = {
    'raw_analyst_ratings': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv",
    'historical_data': {
        'AAPL': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv",
        'AMZN': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv",
        'GOOG': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv",
        'META': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv",
        'MSFT': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv",
        'NVDA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv",
        'TSLA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv"
    }
}

# Path to save technical indicators results
technical_indicators_output_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\technical_indicators_results.csv"

def load_data(file_path):
    """
    Load data from the specified file path.
    """
    return pd.read_csv(file_path)

def calculate_technical_indicators(df):
    """
    Calculate various technical indicators using the TA-Lib library.
    """
    # Calculate Moving Averages
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = ta.SMA(df['Close'], timeperiod=50)
    
    # Calculate Exponential Moving Average (EMA)
    df['EMA_20'] = ta.EMA(df['Close'], timeperiod=20)
    df['EMA_50'] = ta.EMA(df['Close'], timeperiod=50)
    
    # Calculate Relative Strength Index (RSI)
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    
    # Calculate Moving Average Convergence Divergence (MACD)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    # Calculate Bollinger Bands
    df['upper_band'], df['middle_band'], df['lower_band'] = ta.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    
    return df

def main():
    # Load raw analyst ratings data (for potential future use)
    raw_analyst_ratings_df = load_data(data_paths['raw_analyst_ratings'])
    print("Raw analyst ratings data loaded.")

    # Initialize a list to store the technical indicators for each stock
    technical_indicators_results = []

    # Iterate over each stock's historical data
    for stock, path in data_paths['historical_data'].items():
        print(f"Processing {stock}...")
        stock_df = load_data(path)
        
        # Calculate technical indicators for the stock
        stock_df = calculate_technical_indicators(stock_df)
        
        # Add stock identifier and append the result to the list
        stock_df['Stock'] = stock
        technical_indicators_results.append(stock_df)
    
    # Concatenate all the technical indicators results into one DataFrame
    all_technical_indicators_df = pd.concat(technical_indicators_results, ignore_index=True)
    
    # Save the technical indicators results to a CSV file
    all_technical_indicators_df.to_csv(technical_indicators_output_path, index=False)
    print(f"Technical indicators analysis results saved to {technical_indicators_output_path}")

if __name__ == "__main__":
    main()
