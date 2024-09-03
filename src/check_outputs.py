import pandas as pd
import os

# Define paths for output files to check
prepared_data_dir = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\prepared_data"
technical_indicators_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\technical_indicators_results.csv"
visualizations_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\visualizations"

def check_file(file_path):
    """
    Check if a file exists and is not empty.
    """
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return False
    
    if os.path.getsize(file_path) == 0:
        print(f"File {file_path} is empty.")
        return False
    
    return True

def check_csv(file_path):
    """
    Check the contents of a CSV file by loading it into a DataFrame and printing basic information.
    """
    if not check_file(file_path):
        return
    
    df = pd.read_csv(file_path)
    print(f"\nContents of {file_path}:")
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"First few rows:\n{df.head()}")

def main():
    # Check prepared data files
    print("Checking prepared data files...")
    for file in os.listdir(prepared_data_dir):
        file_path = os.path.join(prepared_data_dir, file)
        check_csv(file_path)
    
    # Check technical indicators file
    print("\nChecking technical indicators file...")
    check_csv(technical_indicators_path)
    
    # Check visualizations directory for saved visualizations (if applicable)
    print("\nChecking visualizations directory...")
    if not os.path.exists(visualizations_path):
        print(f"Directory {visualizations_path} does not exist.")
    else:
        for file in os.listdir(visualizations_path):
            file_path = os.path.join(visualizations_path, file)
            if os.path.getsize(file_path) > 0:
                print(f"File {file_path} exists and is not empty.")
            else:
                print(f"File {file_path} is empty.")
    
    print("\nChecks complete.")

if __name__ == "__main__":
    main()
