import pytest
import pandas as pd
from src.visualizations import plot_technical_indicators, plot_rsi

def test_plot_technical_indicators():
    df = pd.read_csv('data/AAPL_historical_data.csv', parse_dates=['Date'])
    df = apply_technical_indicators(df)
    plot_technical_indicators(df)  # This function will display the plot

def test_plot_rsi():
    df = pd.read_csv('data/AAPL_historical_data.csv', parse_dates=['Date'])
    df = apply_technical_indicators(df)
    plot_rsi(df)  # This function will display the plot
