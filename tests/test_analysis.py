import unittest
import pandas as pd
import numpy as np
from your_analysis_module import load_data, clean_data, perform_eda, calculate_technical_indicators

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        # Setup paths for test data
        self.data_dir = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data"
        self.news_file_path = f"{self.data_dir}/raw_analyst_ratings.csv"
        self.historical_files = {
            "AAPL": f"{self.data_dir}/AAPL_historical_data.csv",
            "AMZN": f"{self.data_dir}/AMZN_historical_data.csv",
            "GOOG": f"{self.data_dir}/GOOG_historical_data.csv",
            "META": f"{self.data_dir}/META_historical_data.csv",
            "MSFT": f"{self.data_dir}/MSFT_historical_data.csv",
            "NVDA": f"{self.data_dir}/NVDA_historical_data.csv",
            "TSLA": f"{self.data_dir}/TSLA_historical_data.csv"
        }

        # Load test data
        self.news_df = pd.read_csv(self.news_file_path)
        self.stock_dfs = {ticker: pd.read_csv(file) for ticker, file in self.historical_files.items()}

    def test_load_data(self):
        # Check if data is loaded correctly
        self.assertFalse(self.news_df.empty, "News DataFrame should not be empty")
        for ticker, df in self.stock_dfs.items():
            self.assertFalse(df.empty, f"Stock DataFrame for {ticker} should not be empty")

    def test_clean_data(self):
        # Clean the data and check if no NaNs are present in critical columns
        clean_news_df = clean_data(self.news_df)
        clean_stock_dfs = {ticker: clean_data(df, is_stock=True) for ticker, df in self.stock_dfs.items()}
        self.assertTrue(clean_news_df['headline'].notna().all(), "News headlines should not contain NaNs after cleaning")
        for ticker, df in clean_stock_dfs.items():
            self.assertTrue(df['Close'].notna().all(), f"Stock prices for {ticker} should not contain NaNs after cleaning")

    def test_descriptive_statistics(self):
        # Test if descriptive statistics are computed
        desc_stats = perform_eda(self.news_df, self.stock_dfs['AAPL'])
        self.assertIn('headline_length', desc_stats, "Descriptive statistics should include headline length")
        self.assertIn('Close', desc_stats, "Descriptive statistics should include stock prices")

    def test_technical_indicators(self):
        # Test if technical indicators are computed correctly
        indicators_dfs = {ticker: calculate_technical_indicators(df) for ticker, df in self.stock_dfs.items()}
        for ticker, indicators_df in indicators_dfs.items():
            self.assertIn('SMA', indicators_df.columns, f"Technical indicators for {ticker} should include SMA")
            self.assertIn('RSI', indicators_df.columns, f"Technical indicators for {ticker} should include RSI")

    def tearDown(self):
        # Clean up any resources if necessary
        pass

if __name__ == '__main__':
    unittest.main()
