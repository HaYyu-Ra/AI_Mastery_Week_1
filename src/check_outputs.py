import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# File paths
correlation_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\correlation_analysis.csv'
heatmap_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\sentiment_stock_correlation_heatmap.png'

def check_correlation_csv(file_path):
    """Check if the correlation CSV file exists and print its content."""
    if os.path.exists(file_path):
        print(f'Correlation results CSV found at {file_path}')
        try:
            df = pd.read_csv(file_path)
            print('Correlation results CSV content:')
            print(df.head())
        except Exception as e:
            print(f'Error reading CSV file: {e}')
    else:
        print(f'Correlation results CSV not found at {file_path}')

def check_heatmap_image(file_path):
    """Check if the heatmap image file exists and display the image."""
    if os.path.exists(file_path):
        print(f'Heatmap image found at {file_path}')
        try:
            with Image.open(file_path) as img:
                img.show()
        except Exception as e:
            print(f'Error opening image file: {e}')
    else:
        print(f'Heatmap image not found at {file_path}')

# Check files
check_correlation_csv(correlation_file_path)
check_heatmap_image(heatmap_file_path)
