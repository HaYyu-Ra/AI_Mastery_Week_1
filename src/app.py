import pandas as pd
import os

# Define file paths for sentiment analysis results and historical stock data
sentiment_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\sentiment_analysis.csv"

historical_data_paths = {
    'AAPL': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv",
    'AMZN': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AMZN_historical_data.csv",
    'GOOG': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\GOOG_historical_data.csv",
    'META': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\META_historical_data.csv",
    'MSFT': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\MSFT_historical_data.csv",
    'NVDA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\NVDA_historical_data.csv",
    'TSLA': r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\TSLA_historical_data.csv"
}

correlation_output_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\correlation_analysis_results.csv"

def load_data(file_path):
    """
    Load data from the specified file path with error handling.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

def calculate_daily_returns(df, price_column='Close'):
    """
    Calculate the daily percentage returns based on the closing prices.
    """
    if price_column not in df.columns:
        print(f"Price column '{price_column}' not found in the DataFrame.")
        return df
    
    df['Daily Return'] = df[price_column].pct_change()
    return df

def merge_sentiment_and_stock_data(sentiment_df, stock_df):
    """
    Merge the sentiment data with stock data on the date.
    """
    if 'date' not in sentiment_df.columns or 'Date' not in stock_df.columns:
        print("Date columns missing in one of the DataFrames.")
        return pd.DataFrame()
    
    sentiment_df['date'] = pd.to_datetime(sentiment_df['date'], errors='coerce')
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
    
    # Drop rows where dates could not be parsed
    sentiment_df = sentiment_df.dropna(subset=['date'])
    stock_df = stock_df.dropna(subset=['Date'])
    
    # Merging on the date column
    merged_df = pd.merge(sentiment_df, stock_df, left_on='date', right_on='Date', how='inner')
    return merged_df

def calculate_correlation(df):
    """
    Calculate the correlation between sentiment scores and daily returns.
    """
    if 'Sentiment Score' not in df.columns or 'Daily Return' not in df.columns:
        print("Required columns are missing from the DataFrame.")
        return None
    
    correlation = df['Sentiment Score'].corr(df['Daily Return'])
    return correlation

def main():
    # Load the sentiment analysis data
    sentiment_df = load_data(sentiment_data_path)
    
    if sentiment_df.empty:
        print("Sentiment analysis data could not be loaded.")
        return
    
    # Initialize a list to store the correlation results
    correlation_results = []

    # Iterate over each stock's historical data
    for stock, path in historical_data_paths.items():
        stock_df = load_data(path)
        
        if stock_df.empty:
            print(f"Historical data for {stock} could not be loaded.")
            continue
        
        # Calculate daily returns for the stock
        stock_df = calculate_daily_returns(stock_df)
        
        # Merge sentiment data with stock data
        merged_df = merge_sentiment_and_stock_data(sentiment_df, stock_df)
        
        if merged_df.empty:
            print(f"Data could not be merged for {stock}.")
            continue
        
        # Calculate the correlation between sentiment scores and stock returns
        correlation = calculate_correlation(merged_df)
        
        if correlation is not None:
            # Append the result to the list
            correlation_results.append({
                'Stock': stock,
                'Correlation': correlation
            })
    
    # Convert the correlation results to a DataFrame
    if correlation_results:
        correlation_df = pd.DataFrame(correlation_results)
        
        # Save the correlation results to a CSV file
        correlation_df.to_csv(correlation_output_path, index=False)
        print(f"Correlation analysis results saved to {correlation_output_path}")
    else:
        print("No valid correlation results to save.")

if __name__ == "__main__":
    main()
