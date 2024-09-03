from src.data_preparation import load_stock_data, preprocess_data

if __name__ == "__main__":
    file_path = 'data/AAPL_historical_data.csv'
    data = load_stock_data(file_path)
    data = preprocess_data(data)
    data.to_csv('data/processed_data.csv', index=False)
