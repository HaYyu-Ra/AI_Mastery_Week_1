import pytest
import pandas as pd
from src.financial_metrics import calculate_metrics

def test_calculate_metrics():
    df = pd.read_csv('data/AAPL_historical_data.csv', parse_dates=['Date'])
    metrics = calculate_metrics(df)
    assert 'mean_return' in metrics
    assert 'volatility' in metrics
