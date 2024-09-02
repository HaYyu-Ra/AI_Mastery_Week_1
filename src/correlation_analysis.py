import pandas as pd

def load_sentiment_data(path):
    df = pd.read_csv(path)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    if 'sentiment_score' in df.columns:
        df['sentiment_score'] = pd.to_numeric(df['sentiment_score'], errors='coerce')
    return df

def perform_correlation_analysis(sentiment_df, stock_df):
    if 'Date' in sentiment_df.columns and 'Date' in stock_df.columns:
        sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date'])
        stock_df['Date'] = pd.to_datetime(stock_df['Date'])
        
        merged_df = pd.merge(sentiment_df, stock_df, on='Date')
        
        if 'sentiment_score' in merged_df.columns and 'Close' in merged_df.columns:
            correlation = merged_df['sentiment_score'].corr(merged_df['Close'])
            return correlation
        else:
            return None
    else:
        return None
