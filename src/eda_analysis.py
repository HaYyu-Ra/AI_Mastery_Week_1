import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_raw_data(path):
    df = pd.read_csv(path)
    if 'headline' in df.columns:
        df['headline'] = df['headline'].astype(str)
    if 'publication_date' in df.columns:
        df['publication_date'] = pd.to_datetime(df['publication_date'])
    return df

def perform_eda(df):
    descriptive_stats = df.describe(include='all', datetime_is_numeric=True)
    
    if 'publisher' in df.columns:
        articles_per_publisher = df['publisher'].value_counts()
    else:
        articles_per_publisher = pd.Series()

    if 'publication_date' in df.columns:
        df['publication_date'] = pd.to_datetime(df['publication_date'])
        publication_trends = df.groupby(df['publication_date'].dt.to_period('M')).size()
    else:
        publication_trends = pd.Series()
    
    return descriptive_stats, articles_per_publisher, publication_trends
