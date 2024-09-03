import unittest
import pandas as pd
from your_sentiment_module import load_sentiment_data, perform_sentiment_analysis, summarize_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        # Setup paths for test data
        self.data_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data"
        self.news_file_path = f"{self.data_path}/raw_analyst_ratings.csv"

        # Load test data
        self.news_df = pd.read_csv(self.news_file_path)

    def test_load_sentiment_data(self):
        # Check if the sentiment data is loaded correctly
        df = load_sentiment_data(self.news_file_path)
        self.assertFalse(df.empty, "Sentiment DataFrame should not be empty")
        self.assertEqual(df.shape[1], self.news_df.shape[1], "Loaded DataFrame should have the same number of columns as the original DataFrame")

    def test_perform_sentiment_analysis(self):
        # Perform sentiment analysis and check if sentiment scores are computed
        sentiment_df = perform_sentiment_analysis(self.news_df)
        self.assertTrue('sentiment_score' in sentiment_df.columns, "Sentiment DataFrame should include 'sentiment_score'")
        self.assertTrue(sentiment_df['sentiment_score'].notna().all(), "Sentiment scores should not contain NaNs")

    def test_summarize_sentiment(self):
        # Summarize sentiment and check if summary statistics are computed
        sentiment_df = perform_sentiment_analysis(self.news_df)
        summary_stats = summarize_sentiment(sentiment_df)
        self.assertIn('average_sentiment', summary_stats, "Summary statistics should include 'average_sentiment'")
        self.assertIn('median_sentiment', summary_stats, "Summary statistics should include 'median_sentiment'")
        self.assertIn('std_dev_sentiment', summary_stats, "Summary statistics should include 'std_dev_sentiment'")

    def tearDown(self):
        # Clean up any resources if necessary
        pass

if __name__ == '__main__':
    unittest.main()
