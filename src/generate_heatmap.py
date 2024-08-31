import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# File paths
correlation_file_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\correlation_analysis.csv'
heatmap_image_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\sentiment_stock_correlation_heatmap.png'

def generate_heatmap(correlation_file_path, output_image_path):
    """Generate and save a heatmap from correlation data."""
    if os.path.exists(correlation_file_path):
        print(f'Correlation CSV found at {correlation_file_path}')
        try:
            # Load correlation data
            correlation_df = pd.read_csv(correlation_file_path)

            # Check the dataframe content
            print('Correlation data:')
            print(correlation_df.head())

            # Create a heatmap
            plt.figure(figsize=(10, 8))
            heatmap = sns.heatmap(correlation_df, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
            heatmap.set_title('Sentiment and Stock Movement Correlation Heatmap', size=16)

            # Save the heatmap image
            plt.savefig(output_image_path, format='png')
            plt.close()
            print(f'Heatmap saved to {output_image_path}')

        except Exception as e:
            print(f'Error generating heatmap: {e}')
    else:
        print(f'Correlation CSV not found at {correlation_file_path}')

# Generate heatmap
generate_heatmap(correlation_file_path, heatmap_image_path)
