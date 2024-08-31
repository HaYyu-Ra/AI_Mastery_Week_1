import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    """Unit tests for sentiment analysis."""

    def test_positive_sentiment(self):
        """Test case for positive sentiment."""
        sentiment = analyze_sentiment("The stock is soaring high!")
        self.assertGreater(sentiment, 0, "Expected positive sentiment score for positive text.")

    def test_negative_sentiment(self):
        """Test case for negative sentiment."""
        sentiment = analyze_sentiment("The stock price is crashing.")
        self.assertLess(sentiment, 0, "Expected negative sentiment score for negative text.")

    def test_neutral_sentiment(self):
        """Test case for neutral sentiment."""
        sentiment = analyze_sentiment("The stock is stable.")
        self.assertEqual(sentiment, 0, "Expected neutral sentiment score for neutral text.")

if __name__ == '__main__':
    unittest.main()
