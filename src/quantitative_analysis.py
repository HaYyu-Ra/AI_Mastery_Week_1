import pandas as pd
import numpy as np
import talib as ta
import matplotlib.pyplot as plt

# Define paths for historical stock data
historical_data_paths = {
    'AAPL': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv",
    'AMZN': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv",
    'GOOG': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv",
    'META': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv",
    'MSFT': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv",
    'NVDA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv",
    'TSLA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv"
}

# Path for raw analyst ratings
raw_analyst_ratings_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv"

# Path to save quantitative analysis results
quantitative_analysis_output_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\quantitative_analysis_results.csv"

def load_data(file_path):
    """
    Load data from the specified file path.
    """
    return pd.read_csv(file_path)

def calculate_financial_metrics(df):
    """
    Calculate financial metrics and technical indicators using the TA-Lib library.
    """
    df['SMA_20'] = ta.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = ta.SMA(df['Close'], timeperiod=50)
    
    df['EMA_20'] = ta.EMA(df['Close'], timeperiod=20)
    df['EMA_50'] = ta.EMA(df['Close'], timeperiod=50)
    
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = ta.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    df['upper_band'], df['middle_band'], df['lower_band'] = ta.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    
    # Calculate additional financial metrics
    df['Daily_Return'] = df['Close'].pct_change()
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod()
    
    return df

def visualize_data(df, stock):
    """
    Visualize stock data with technical indicators.
    """
    plt.figure(figsize=(14, 10))

    # Plot closing price and SMAs
    plt.subplot(2, 1, 1)
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20', color='red')
    plt.plot(df['Date'], df['SMA_50'], label='SMA 50', color='green')
    plt.title(f'{stock} Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()

    # Plot RSI
    plt.subplot(2, 1, 2)
    plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red')
    plt.axhline(30, linestyle='--', color='green')
    plt.title(f'{stock} Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig(f'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data/{stock}_technical_indicators.png')
    plt.show()

def main():
    results = []
    
    # Load raw analyst ratings data
    analyst_ratings_df = load_data(raw_analyst_ratings_path)
    print("Loaded raw analyst ratings data.")
    
    for stock, path in historical_data_paths.items():
        df = load_data(path)
        df = calculate_financial_metrics(df)
        
        # Save the processed data to a CSV file
        df.to_csv(quantitative_analysis_output_path, index=False)
        
        # Visualize the data
        visualize_data(df, stock)
        
        # Append results
        results.append(df)
    
    # Combine results and save to a single file
    all_results_df = pd.concat(results, ignore_index=True)
    all_results_df.to_csv(quantitative_analysis_output_path, index=False)
    print(f"Quantitative analysis results saved to {quantitative_analysis_output_path}")

if __name__ == "__main__":
    main()
