import os
import pandas as pd
from textblob import TextBlob

# File path for the sentiment analysis dataset
DATA_PATH = os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "sentiment_analysis.csv")

def load_data(file_path):
    """
    Load the dataset for sentiment analysis.

    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def sentiment_analysis(text):
    """
    Perform sentiment analysis on a given text using TextBlob.

    Parameters:
    text (str): The text on which sentiment analysis will be performed.

    Returns:
    float: The sentiment polarity score, ranging from -1.0 (negative) to 1.0 (positive).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def apply_sentiment_analysis(data, text_column):
    """
    Apply sentiment analysis to each row in the specified text column of the dataset.

    Parameters:
    data (pd.DataFrame): The dataset containing the text data.
    text_column (str): The name of the column containing the text.

    Returns:
    pd.DataFrame: The dataset with an additional 'Sentiment' column containing sentiment scores.
    """
    data['Sentiment'] = data[text_column].apply(sentiment_analysis)
    return data

def save_results(data, output_path):
    """
    Save the dataset with sentiment scores to a CSV file.

    Parameters:
    data (pd.DataFrame): The dataset containing the sentiment scores.
    output_path (str): The file path where the results will be saved.
    """
    try:
        data.to_csv(output_path, index=False)
        print(f"Results saved successfully to {output_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

def main():
    # Load the data
    data = load_data(DATA_PATH)
    if data is None:
        return
    
    # Apply sentiment analysis
    data = apply_sentiment_analysis(data, 'headline')  # Assuming 'headline' is the text column

    # Save the results
    output_path = os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "sentiment_analysis_results.csv")
    save_results(data, output_path)

if __name__ == "__main__":
    main()
