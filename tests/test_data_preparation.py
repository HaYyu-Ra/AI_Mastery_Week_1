import pytest
import pandas as pd
from src.data_preparation import load_stock_data, preprocess_data

def test_load_stock_data():
    df = load_stock_data('data/AAPL_historical_data.csv')
    assert isinstance(df, pd.DataFrame)
    assert 'Date' in df.columns

def test_preprocess_data():
    df = load_stock_data('data/AAPL_historical_data.csv')
    df = preprocess_data(df)
    assert df.isnull().sum().sum() == 0
