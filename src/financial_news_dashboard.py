import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Define data paths
data_paths = {
    'AAPL': 'data/AAPL_historical_data.csv',
    'AMZN': 'data/AMZN_historical_data.csv',
    'GOOG': 'data/GOOG_historical_data.csv',
    'META': 'data/META_historical_data.csv',
    'MSFT': 'data/MSFT_historical_data.csv',
    'NVDA': 'data/NVDA_historical_data.csv',
    'TSLA': 'data/TSLA_historical_data.csv',
}

raw_data_path = 'data/raw_analyst_ratings.csv'

@st.cache_data
def load_data():
    raw_df = pd.read_csv(raw_data_path)
    stock_data = {stock: pd.read_csv(path, parse_dates=['Date']) for stock, path in data_paths.items()}
    return raw_df, stock_data

def plot_closing_prices(df, stock):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    ax.set_title(f'{stock} Closing Prices Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.legend()
    return fig

def plot_volume(df, stock):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df['Date'], df['Volume'], label='Volume', color='orange')
    ax.set_title(f'{stock} Volume Traded Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    ax.legend()
    return fig

def plot_distribution(df, stock):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['Close'], kde=True, ax=ax)
    ax.set_title(f'Distribution of {stock} Closing Prices')
    ax.set_xlabel('Close Price')
    ax.set_ylabel('Frequency')
    return fig

def plot_correlation(df, stock):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    ax.set_title(f'{stock} Correlation Matrix')
    return fig

def display_kpis(df, stock):
    kpis = {
        'Average Close Price': df['Close'].mean(),
        'Highest Close Price': df['Close'].max(),
        'Lowest Close Price': df['Close'].min(),
        'Total Volume Traded': df['Volume'].sum(),
    }
    st.write(f'**{stock} Key Performance Indicators (KPIs)**')
    for key, value in kpis.items():
        st.metric(label=key, value=f"${value:,.2f}")

def financial_dashboard():
    st.title('Financial Dashboard: Analyst Ratings and Stock Analysis')

    raw_df, stock_data = load_data()

    st.header('Raw Analyst Ratings Data')
    st.write(raw_df.head())

    for stock, df in stock_data.items():
        st.subheader(f'{stock} Analysis')
        
        st.write(f'**Basic Statistics: {stock}**')
        st.write(df.describe())

        st.write(f'**{stock} Data Preview**')
        st.write(df.head())

        st.write(f'**{stock} Closing Prices Over Time**')
        st.pyplot(plot_closing_prices(df, stock))

        st.write(f'**{stock} Volume Traded Over Time**')
        st.pyplot(plot_volume(df, stock))

        st.write(f'**Distribution of {stock} Closing Prices**')
        st.pyplot(plot_distribution(df, stock))

        st.write(f'**{stock} Correlation Matrix**')
        st.pyplot(plot_correlation(df, stock))

        display_kpis(df, stock)

    st.write("### End of Analysis")

if __name__ == "__main__":
    financial_dashboard()
