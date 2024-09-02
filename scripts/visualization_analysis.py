from src.visualizations import plot_technical_indicators, plot_rsi
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('data/indicators_data.csv', parse_dates=['Date'])
    plot_technical_indicators(df)
    plot_rsi(df)
