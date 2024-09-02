import pytest
import pandas as pd
from eda_analysis import load_raw_data
from quantitative_analysis import load_stock_data
from correlation_analysis import perform_correlation_analysis

RAW_DATA_PATH = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\raw_analyst_ratings.csv'
HISTORICAL_DATA_PATH = r'C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\AI_Mastery_Week_1\data\AAPL_historical_data.csv'

def test_load_raw_data():
    df = load_raw_data(RAW_DATA_PATH)
    assert isinstance(df, pd.DataFrame), "Raw data should be a DataFrame"
    assert not df.empty, "Raw data should not be empty"

def test_load_stock_data():
    stock_data = load_stock_data({'AAPL': HISTORICAL_DATA_PATH})
    assert 'AAPL' in stock_data, "AAPL data should be loaded"
    assert not stock_data['AAPL'].empty, "AAPL data should not be empty"

def test_perform_correlation_analysis():
    raw_data, stock_data = load_raw_data(RAW_DATA_PATH), pd.read_csv(HISTORICAL_DATA_PATH, parse_dates=['Date'], index_col='Date')
    correlation = perform_correlation_analysis(raw_data, stock_data)
    assert isinstance(correlation, float), "Correlation should be a float"
