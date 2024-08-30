# eda_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load dataset
df = pd.read_csv('data/financial_news.csv')

# Descriptive Statistics
df['headline_length'] = df['headline'].apply(len)
print(df['headline_length'].describe())

# Articles per publisher
publisher_counts = df['publisher'].value_counts()
print(publisher_counts)

# Publication dates
df['date'] = pd.to_datetime(df['date'])
print(df['date'].describe())

# Sentiment Analysis
df['sentiment'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
print(df[['headline', 'sentiment']].head())

# Plot publication frequency
df.set_index('date', inplace=True)
df.resample('D').size().plot()
plt.title('Publication Frequency Over Time')
plt.show()
