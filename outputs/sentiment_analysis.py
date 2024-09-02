import pandas as pd
from textblob import TextBlob
import os

# Define paths for raw data and historical stock data
raw_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\cleaned_sentiment_analysis.csv"

# Function to load data with custom error handling
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}. First few rows:")
        print(df.head())
        return df
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file {file_path}: {e}")
        raise
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    
    if sentiment_score > 0:
        sentiment_label = 'positive'
    elif sentiment_score == 0:
        sentiment_label = 'neutral'
    else:
        sentiment_label = 'negative'
    
    return sentiment_score, sentiment_label

# Function to analyze data and add sentiment scores/labels
def analyze_data(df):
    if 'headline' not in df.columns:
        print("Error: 'headline' column not found in the data.")
        raise ValueError("'headline' column is missing from the data.")
    
    df['Sentiment Score'] = df['headline'].apply(lambda x: perform_sentiment_analysis(x)[0])
    df['Sentiment Label'] = df['headline'].apply(lambda x: perform_sentiment_analysis(x)[1])
    
    return df

# Function to save results to a CSV file
def save_results(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Sentiment analysis results saved to {output_path}")
    except Exception as e:
        print(f"Error saving results: {e}")
        raise

def main():
    # Load the cleaned sentiment analysis data
    try:
        df = load_data(raw_data_path)
    except Exception as e:
        print("Sentiment analysis data could not be loaded.")
        print(f"Error: {e}")
        return
    
    # Perform sentiment analysis
    try:
        df = analyze_data(df)
    except Exception as e:
        print("Error during sentiment analysis.")
        print(f"Error: {e}")
        return
    
    # Convert the 'date' column to datetime64[ns] if it's not already
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Load another DataFrame to merge with (example)
    other_df = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'value': [10, 20, 30, 40, 50]
    })

    # Ensure the 'date' column in other_df is also datetime64[ns]
    other_df['date'] = pd.to_datetime(other_df['date'], errors='coerce')

    # Merge the DataFrames
    try:
        merged_data = pd.merge(df, other_df, on='date')
        print("DataFrames merged successfully.")
    except Exception as e:
        print(f"Error merging DataFrames: {e}")
        return

    # Save the sentiment analysis results
    output_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\sentiment_analysis_results.csv"
    try:
        save_results(merged_data, output_path)
    except Exception as e:
        print("Error saving sentiment analysis results.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
