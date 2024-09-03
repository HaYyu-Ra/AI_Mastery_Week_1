import numpy as np
import pandas as pd
import streamlit as st

def calculate_financial_metrics(df):
    # Initialize an empty DataFrame for metrics
    metrics_df = pd.DataFrame()

    # Check if the DataFrame is empty or missing necessary columns
    if df.empty or 'Close' not in df.columns or 'Daily_Return' not in df.columns:
        st.error("DataFrame is empty or missing necessary columns.")
        return metrics_df

    # Handle missing values by forward-filling and replacing NaNs in 'Daily_Return' with 0
    df['Close'].fillna(method='ffill', inplace=True)
    df['Daily_Return'].fillna(0, inplace=True)

    # Calculate Volatility: Standard deviation of 'Close' prices
    volatility = np.std(df['Close'])
    
    # Calculate Sharpe Ratio: Mean of 'Daily_Return' divided by its standard deviation
    daily_return_std = np.std(df['Daily_Return'])
    sharpe_ratio = np.mean(df['Daily_Return']) / daily_return_std if daily_return_std != 0 else np.nan
    
    # Calculate Maximum Drawdown: Maximum drop from the peak of 'Close' prices
    max_drawdown = ((df['Close'].cummax() - df['Close']) / df['Close'].cummax()).max()
    
    # Populate metrics DataFrame
    metrics_df = pd.DataFrame({
        'Metric': ['Volatility', 'Sharpe Ratio', 'Maximum Drawdown'],
        'Value': [volatility, sharpe_ratio, max_drawdown]
    })

    # Check for any NaN values in the metrics DataFrame
    if metrics_df.isnull().values.any():
        st.error("Some financial metrics could not be calculated. Check your data.")
    
    return metrics_df

# Example usage in a Streamlit app
def financial_dashboard():
    st.title('Financial Dashboard: Analyst Ratings and Stock Analysis')

    # Load stock data (Example: using a placeholder DataFrame for demonstration)
    stock_data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'Close': np.random.randn(10).cumsum() + 100,
        'Daily_Return': np.random.randn(10)
    })

    stock_data.set_index('Date', inplace=True)

    # Calculate and display financial metrics
    metrics_df = calculate_financial_metrics(stock_data)
    
    if not metrics_df.empty:
        st.subheader('Financial Metrics')
        st.write(metrics_df)

if __name__ == "__main__":
    financial_dashboard()
