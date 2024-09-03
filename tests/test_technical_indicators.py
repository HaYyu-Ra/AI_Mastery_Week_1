import pytest
import pandas as pd
from src.technical_indicators import apply_technical_indicators

def test_apply_technical_indicators():
    df = pd.read_csv('data/AAPL_historical_data.csv', parse_dates=['Date'])
    df = apply_technical_indicators(df)
    assert 'SMA' in df.columns
    assert 'RSI' in df.columns
    assert 'MACD' in df.columns
