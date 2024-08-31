import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load data
data_path = 'C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data/raw_analyst_ratings.csv'
news_data = pd.read_csv(data_path)

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Apply sentiment analysis
news_data['sentiment'] = news_data['headline'].apply(analyze_sentiment)

# Save sentiment data
news_data.to_csv('C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/data/sentiment_data.csv', index=False)

# Plot sentiment distribution
plt.hist(news_data['sentiment'], bins=20)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.savefig('C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/AI_Mastery_Week_1/plots/sentiment_distribution.png')
