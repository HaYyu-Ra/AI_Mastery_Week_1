import pandas as pd
import os

# Define directories and filenames
raw_data_dir = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data"
historical_data_files = {
    "AAPL": "AAPL_historical_data.csv",
    "AMZN": "AMZN_historical_data.csv",
    "GOOG": "GOOG_historical_data.csv",
    "META": "META_historical_data.csv",
    "MSFT": "MSFT_historical_data.csv",
    "NVDA": "NVDA_historical_data.csv",
    "TSLA": "TSLA_historical_data.csv"
}

# Paths for raw data and historical data
raw_data_file_path = os.path.join(raw_data_dir, "raw_analyst_ratings.csv")

# Ensure the directory exists
if not os.path.exists(raw_data_dir):
    os.makedirs(raw_data_dir)

# Save the raw DataFrame to CSV
# Assuming news_df is your DataFrame that you want to save
news_df.to_csv(raw_data_file_path, index=False)
print(f"Raw data file saved to {raw_data_file_path}")

# Load historical data
historical_data_paths = {ticker: os.path.join(raw_data_dir, filename) 
                         for ticker, filename in historical_data_files.items()}

# Example of how to load one of the historical data files
# You can load all historical data files similarly if needed
for ticker, path in historical_data_paths.items():
    if os.path.exists(path):
        historical_df = pd.read_csv(path)
        print(f"Loaded historical data for {ticker} from {path}")
    else:
        print(f"Historical data file not found for {ticker} at {path}")
