from flask import Flask, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

# File paths
NEWS_DATA_PATH = os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "raw_analyst_ratings.csv")
STOCK_DATA_PATHS = {
    "AAPL": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "AAPL_historical_data.csv"),
    "AMZN": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "AMZN_historical_data.csv"),
    "GOOG": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "GOOG_historical_data.csv"),
    "META": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "META_historical_data.csv"),
    "MSFT": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "MSFT_historical_data.csv"),
    "NVDA": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "NVDA_historical_data.csv"),
    "TSLA": os.path.join("C:\\Users\\hayyu.ragea\\AppData\\Local\\Programs\\Python\\Python312\\AI_Mastery_Week_1\\data\\", "TSLA_historical_data.csv"),
}

@app.route('/news_data', methods=['GET'])
def get_news_data():
    try:
        news_data = pd.read_csv(NEWS_DATA_PATH)
        data = news_data.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stock_data', methods=['GET'])
def get_stock_data():
    ticker = request.args.get('ticker')
    if ticker not in STOCK_DATA_PATHS:
        return jsonify({"error": "Invalid stock ticker"}), 400
    try:
        stock_data = pd.read_csv(STOCK_DATA_PATHS[ticker])
        data = stock_data.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

