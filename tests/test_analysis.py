import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths
test_data_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\test_data.csv'
test_output_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\outputs\test_analysis_results.csv'
heatmap_output_path = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\plots\test_correlation_heatmap.png'

def load_test_data(file_path):
    """Load test data from a CSV file."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f'Test data file not found at {file_path}')

def perform_eda(df):
    """Perform Exploratory Data Analysis (EDA) on the test data."""
    # Describe the data
    description = df.describe()
    
    # Check for missing values
    missing_values = df.isnull().sum()
    
    # Display summary statistics
    print('Summary Statistics:')
    print(description)
    
    print('Missing Values:')
    print(missing_values)
    
    return description, missing_values

def calculate_correlations(df):
    """Calculate correlations between numerical features in the test data."""
    correlation_matrix = df.corr()
    return correlation_matrix

def plot_heatmap(correlation_matrix, output_path):
    """Plot and save a heatmap of the correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap')
    plt.savefig(output_path)
    plt.close()

def main():
    """Main function to perform test analysis."""
    try:
        # Load test data
        df = load_test_data(test_data_path)
        print('Test data loaded successfully.')
        
        # Perform EDA
        description, missing_values = perform_eda(df)
        
        # Calculate correlations
        correlation_matrix = calculate_correlations(df)
        print('Correlation analysis complete.')
        
        # Save correlation results
        correlation_matrix.to_csv(test_output_path)
        print(f'Correlation analysis results saved to {test_output_path}')
        
        # Plot and save heatmap
        plot_heatmap(correlation_matrix, heatmap_output_path)
        print(f'Heatmap saved to {heatmap_output_path}')
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
