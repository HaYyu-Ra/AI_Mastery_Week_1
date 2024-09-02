import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths for raw analyst ratings, historical data, and output visualizations
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
visualizations_output_dir = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\visualizations"

if not os.path.exists(visualizations_output_dir):
    os.makedirs(visualizations_output_dir)

def load_data(file_path):
    """
    Load data from the specified file path.
    """
    return pd.read_csv(file_path)

def plot_analyst_ratings_vs_price(df, stock):
    """
    Plot raw analyst ratings against the historical closing prices for the given stock.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='black')
    
    # Plot raw analyst ratings if available
    if 'Rating' in df.columns:
        plt.plot(df['Date'], df['Rating'], label='Analyst Rating', color='orange', linestyle='--')
    
    plt.title(f'{stock} Analyst Ratings vs. Price')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(visualizations_output_dir, f'{stock}_analyst_ratings_vs_price.png'))
    plt.close()

def main():
    # Load raw analyst ratings data
    raw_analyst_ratings_df = load_data(raw_analyst_ratings_path)
    
    for stock, path in historical_data_paths.items():
        # Load historical data for each stock
        stock_df = load_data(path)
        
        # Merge historical data with raw analyst ratings based on the Date column
        if 'Date' in raw_analyst_ratings_df.columns:
            merged_df = pd.merge(stock_df, raw_analyst_ratings_df, on='Date', how='left')
        else:
            merged_df = stock_df
        
        # Plot analyst ratings vs. price
        plot_analyst_ratings_vs_price(merged_df, stock)
    
    print(f"Visualizations saved in {visualizations_output_dir}")

if __name__ == "__main__":
    main()
