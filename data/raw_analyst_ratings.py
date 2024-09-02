import pandas as pd

# Define the data for the CSV file
data = {
    'stock_symbol': [
        "AAPL",
        "AMZN",
        "GOOG",
        "META",
        "MSFT",
        "NVDA",
        "TSLA",
        "AAPL"
    ],
    'Publisher': [
        "John Doe",
        "Jane Smith",
        "Emily Johnson",
        "Michael Brown",
        "Laura Wilson",
        "James Davis",
        "Alice Miller",
        "Robert Garcia"
    ],
    'rating': [
        "Buy",
        "Hold",
        "Buy",
        "Sell",
        "Buy",
        "Hold",
        "Buy",
        "Sell"
    ],
    'rating_date': [
        "2024-09-01",
        "2024-09-02",
        "2024-09-01",
        "2024-09-03",
        "2024-09-02",
        "2024-09-04",
        "2024-09-01",
        "2024-09-05"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the path where the CSV file will be saved
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv'

# Write the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"File saved to {file_path}")
