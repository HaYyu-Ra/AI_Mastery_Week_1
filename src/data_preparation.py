import pandas as pd

# File path for the raw data
data_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv'
cleaned_data_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\cleaned_analyst_ratings.csv'

def load_data(file_path):
    """Load data from a CSV file."""
    if pd.io.common.file_exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f'Data file not found at {file_path}')

def clean_data(df):
    """Perform data cleaning tasks such as handling missing values."""
    df = df.dropna()  # Drop rows with missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df

def save_data(df, file_path):
    """Save cleaned data to a CSV file."""
    df.to_csv(file_path, index=False)

def main():
    """Main function to load, clean, and save data."""
    try:
        raw_data = load_data(data_path)
        print('Raw data loaded successfully.')
        
        cleaned_data = clean_data(raw_data)
        print('Data cleaned successfully.')
        
        save_data(cleaned_data, cleaned_data_path)
        print(f'Cleaned data saved to {cleaned_data_path}')
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
