from src.technical_indicators import apply_technical_indicators
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('data/processed_data.csv', parse_dates=['Date'])
    df = apply_technical_indicators(df)
    df.to_csv('data/indicators_data.csv', index=False)
