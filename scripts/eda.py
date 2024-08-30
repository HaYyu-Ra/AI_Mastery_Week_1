# eda.py
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import statsmodels.api as sm

# Load your data
data = pd.read_csv('C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\your_data.csv')

# Descriptive Statistics
print(data.describe())

# Text Analysis (Sentiment Analysis)
data['sentiment'] = data['text_column'].apply(lambda x: TextBlob(x).sentiment.polarity)
print(data['sentiment'].describe())

# Time Series Analysis
data['date'] = pd.to_datetime(data['date_column'])
data.set_index('date', inplace=True)
data['value_column'].plot()
plt.show()

# Publisher Analysis
publisher_counts = data['publisher_column'].value_counts()
print(publisher_counts)
