import pandas as pd
import os

# Set up file paths
data_dir = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data"
output_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/correlation_analysis"

# File paths for the data
news_file_path = os.path.join(data_dir, "raw_analyst_ratings.csv")
historical_files = {
    "AAPL": os.path.join(data_dir, "AAPL_historical_data.csv"),
    "AMZN": os.path.join(data_dir, "AMZN_historical_data.csv"),
    "GOOG": os.path.join(data_dir, "GOOG_historical_data.csv"),
    "META": os.path.join(data_dir, "META_historical_data.csv"),
    "MSFT": os.path.join(data_dir, "MSFT_historical_data.csv"),
    "NVDA": os.path.join(data_dir, "NVDA_historical_data.csv"),
    "TSLA": os.path.join(data_dir, "TSLA_historical_data.csv")
}

def load_and_prepare_data(news_file_path, historical_files):
    """Load news and stock data, merge on date, and prepare for correlation analysis."""
    # Load news data
    news_df = pd.read_csv(news_file_path)
    news_df.dropna(subset=['headline', 'date'], inplace=True)
    news_df['date'] = pd.to_datetime(news_df['date']).dt.date

    # Load stock data
    stock_dfs = {ticker: pd.read_csv(file) for ticker, file in historical_files.items()}
    for ticker, stock_df in stock_dfs.items():
        stock_df.dropna(subset=['Date'], inplace=True)
        stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date
        stock_df['Daily_Return'] = stock_df['Close'].pct_change()
    
    return news_df, stock_dfs

def analyze_correlation(news_df, stock_dfs):
    """Analyze the correlation between news sentiment and stock daily returns."""
    correlations = {}
    
    # Assuming news_df has a 'sentiment' column and stock_dfs has 'Daily_Return'
    for ticker, stock_df in stock_dfs.items():
        # Merge news and stock data
        merged_df = pd.merge(news_df, stock_df, left_on='date', right_on='Date', how='inner')

        # Check if there's sentiment data
        if 'sentiment' in merged_df.columns:
            # Calculate the correlation
            correlation = merged_df['sentiment'].corr(merged_df['Daily_Return'])
            correlations[ticker] = correlation

    return correlations

def save_correlation_results(correlations, output_path):
    """Save the correlation results to a CSV file."""
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Convert the correlations dictionary to a DataFrame
    correlation_df = pd.DataFrame(list(correlations.items()), columns=['Ticker', 'Correlation'])
    
    # Save to CSV
    output_file_path = os.path.join(output_path, "correlation_results.csv")
    correlation_df.to_csv(output_file_path, index=False)
    print(f"Correlation analysis results saved to {output_file_path}")

def main():
    news_df, stock_dfs = load_and_prepare_data(news_file_path, historical_files)
    correlations = analyze_correlation(news_df, stock_dfs)
    save_correlation_results(correlations, output_path)

if __name__ == "__main__":
    main()
