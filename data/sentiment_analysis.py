import pandas as pd

# Define the data for the CSV file
data = {
    'Headline': [
        "Apple unveils new iPhone model with advanced features",
        "Amazon expands AWS services with new data centers",
        "Google's algorithm update improves search results significantly",
        "Meta's VR headset faces regulatory challenges",
        "Microsoft reports record earnings for the quarter",
        "NVIDIA introduces new GPU for gaming enthusiasts",
        "Tesla's self-driving feature encounters regulatory issues",
        "Apple's market share grows in the smartphone industry"
    ],
    'Sentiment_Score': [0.8, -0.3, 0.6, -0.5, 0.9, 0.7, -0.4, 0.5],
    'Publication_Date': [
        "2024-09-01",
        "2024-09-02",
        "2024-09-01",
        "2024-09-03",
        "2024-09-02",
        "2024-09-04",
        "2024-09-01",
        "2024-09-05"
    ],
    'Publisher': [
        "TechCrunch",
        "Business Insider",
        "The Verge",
        "Reuters",
        "Bloomberg",
        "CNET",
        "Forbes",
        "Wired"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the path where the CSV file will be saved
file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\sentiment_analysis.csv'

# Write the DataFrame to a CSV file
df.to_csv(file_path, index=False)

print(f"File saved to {file_path}")
