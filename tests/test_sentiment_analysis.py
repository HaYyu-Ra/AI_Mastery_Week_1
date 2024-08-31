import unittest
from src.sentiment_analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_positive_sentiment(self):
        self.assertGreater(analyze_sentiment("The stock is soaring high!"), 0)

    def test_negative_sentiment(self):
        self.assertLess(analyze_sentiment("The stock price is crashing."), 0)

if __name__ == '__main__':
    unittest.main()
