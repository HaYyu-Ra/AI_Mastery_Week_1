# quantitative_analysis.py
import pandas as pd

# Load the stock price data
stock_data = pd.read_csv('C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\stock_prices.csv')

# Ensure your data includes columns like Open, High, Low, Close, and Volume
print(stock_data.head())
