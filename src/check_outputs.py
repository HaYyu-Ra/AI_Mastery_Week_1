import os
import pandas as pd
from PIL import Image

# File paths
correlation_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\correlation_analysis.csv'
heatmap_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\sentiment_stock_correlation_heatmap.png'

def check_csv_existence(file_path):
    """Check if the CSV file exists and print its content."""
    if os.path.exists(file_path):
        print(f'CSV file found at {file_path}')
        try:
            df = pd.read_csv(file_path)
            print('CSV file content:')
            print(df.head())
        except Exception as e:
            print(f'Error reading CSV file: {e}')
    else:
        print(f'CSV file not found at {file_path}')

def check_image_existence(file_path):
    """Check if the image file exists and display the image."""
    if os.path.exists(file_path):
        print(f'Image file found at {file_path}')
        try:
            with Image.open(file_path) as img:
                img.show()
        except Exception as e:
            print(f'Error opening image file: {e}')
    else:
        print(f'Image file not found at {file_path}')

def main():
    """Main function to check the existence of output files."""
    check_csv_existence(correlation_file_path)
    check_image_existence(heatmap_file_path)

if __name__ == "__main__":
    main()
