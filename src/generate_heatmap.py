import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define paths for raw analyst ratings, historical data, and output heatmaps
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
heatmaps_output_dir = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\heatmaps"

if not os.path.exists(heatmaps_output_dir):
    os.makedirs(heatmaps_output_dir)

def load_data(file_path):
    """
    Load data from the specified file path.
    """
    return pd.read_csv(file_path)

def generate_heatmap(df, stock):
    """
    Generate and save a heatmap of correlations between technical indicators and analyst ratings.
    """
    # Compute correlation matrix
    correlation_matrix = df.corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'{stock} Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(os.path.join(heatmaps_output_dir, f'{stock}_correlation_heatmap.png'))
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
        
        # Generate and save the heatmap
        generate_heatmap(merged_df, stock)
    
    print(f"Heatmaps saved in {heatmaps_output_dir}")

if __name__ == "__main__":
    main()
