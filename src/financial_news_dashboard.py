import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Configuration: Define file paths using environment variables or default paths
OUTPUT_CSV_PATH = os.getenv('OUTPUT_CSV_PATH', 'outputs/correlation_analysis.csv')
NEWS_FILE_PATH = os.getenv('NEWS_FILE_PATH', 'data/raw_analyst_ratings.csv')
STOCK_DATA_DIR = os.getenv('STOCK_DATA_DIR', 'data/stock_data')
STOCK_SYMBOLS = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']
STOCK_DATA_PATHS = {symbol: os.path.join(STOCK_DATA_DIR, f"{symbol}_historical_data.csv") for symbol in STOCK_SYMBOLS}

# Streamlit Configuration
st.set_page_config(page_title='Financial News Sentiment Analysis Dashboard', layout='wide')


@st.cache(allow_output_mutation=True)
def load_correlation_data():
    """Load correlation analysis results."""
    try:
        df = pd.read_csv(OUTPUT_CSV_PATH, on_bad_lines='warn')
        if df.empty:
            st.warning("The correlation analysis CSV file is empty.")
            return pd.DataFrame()
        df.rename(columns={'symbol': 'Symbol', 'correlation': 'Correlation'}, inplace=True)
        return df
    except pd.errors.ParserError as e:
        st.error(f"Error parsing the correlation CSV file: {e}")
    except FileNotFoundError:
        st.error(f"Correlation file not found at path: {OUTPUT_CSV_PATH}")
    except Exception as e:
        st.error(f"Unexpected error loading correlation data: {e}")
    return pd.DataFrame()


@st.cache(allow_output_mutation=True)
def load_news_data():
    """Load and preprocess news data for sentiment analysis."""
    if os.path.exists(NEWS_FILE_PATH):
        try:
            news_df = pd.read_csv(NEWS_FILE_PATH)
            news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')
            news_df.dropna(subset=['date', 'headline'], inplace=True)
            news_df['sentiment_score'] = news_df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
            return news_df
        except pd.errors.ParserError as e:
            st.error(f"Error parsing the news CSV file: {e}")
        except Exception as e:
            st.error(f"Unexpected error loading news data: {e}")
    else:
        st.error(f"News file not found at path: {NEWS_FILE_PATH}")
    return pd.DataFrame()


@st.cache(allow_output_mutation=True)
def load_stock_data(symbol):
    """Load historical stock data for a given symbol."""
    file_path = STOCK_DATA_PATHS.get(symbol)
    if file_path and os.path.exists(file_path):
        try:
            stock_df = pd.read_csv(file_path)
            stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
            stock_df.dropna(subset=['Date', 'Close'], inplace=True)
            stock_df.set_index('Date', inplace=True)
            stock_df.sort_index(inplace=True)
            return stock_df
        except pd.errors.ParserError as e:
            st.error(f"Error parsing the stock CSV file for {symbol}: {e}")
        except Exception as e:
            st.error(f"Unexpected error loading stock data for {symbol}: {e}")
    else:
        st.error(f"Stock data file for {symbol} not found at path: {file_path}")
    return pd.DataFrame()


def plot_correlation_results(df):
    """Plot correlation results as a bar chart."""
    if not df.empty and 'Symbol' in df.columns and 'Correlation' in df.columns:
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Symbol', y='Correlation', data=df, palette='viridis')
        plt.title('Correlation between News Sentiment and Stock Returns', fontsize=16)
        plt.xlabel('Stock Symbol', fontsize=14)
        plt.ylabel('Correlation Coefficient', fontsize=14)
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.warning("Insufficient data to plot correlation results.")


def plot_stock_price(stock_df, symbol):
    """Plot historical stock closing prices."""
    if not stock_df.empty and 'Close' in stock_df.columns:
        plt.figure(figsize=(14, 7))
        plt.plot(stock_df.index, stock_df['Close'], label='Close Price', color='blue')
        plt.title(f'Historical Closing Prices for {symbol}', fontsize=16)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Price (USD)', fontsize=14)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
    else:
        st.warning(f"No 'Close' price data available for {symbol}.")


def plot_sentiment_vs_stock(stock_df, news_df, symbol):
    """Plot sentiment scores alongside stock closing prices."""
    if not stock_df.empty and not news_df.empty:
        try:
            # Aggregate sentiment scores by date
            sentiment_daily = news_df.groupby('date')['sentiment_score'].mean().reset_index()
            sentiment_daily.rename(columns={'date': 'Date'}, inplace=True)
            sentiment_daily['Date'] = pd.to_datetime(sentiment_daily['Date'])
            
            # Merge with stock data
            merged_df = pd.merge(stock_df, sentiment_daily, left_index=True, right_on='Date', how='left')
            merged_df['sentiment_score'].fillna(0, inplace=True)  # Handle missing sentiment scores

            # Plotting
            fig, ax1 = plt.subplots(figsize=(14, 7))

            ax1.set_xlabel('Date', fontsize=14)
            ax1.set_ylabel('Closing Price (USD)', color='blue', fontsize=14)
            ax1.plot(merged_df.index, merged_df['Close'], label='Close Price', color='blue')
            ax1.tick_params(axis='y', labelcolor='blue')

            ax2 = ax1.twinx()
            ax2.set_ylabel('Sentiment Score', color='orange', fontsize=14)
            ax2.plot(merged_df.index, merged_df['sentiment_score'], label='Sentiment Score', color='orange', alpha=0.6)
            ax2.tick_params(axis='y', labelcolor='orange')

            plt.title(f'Sentiment Scores vs Closing Prices for {symbol}', fontsize=16)
            fig.tight_layout()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error plotting sentiment vs stock data for {symbol}: {e}")
    else:
        st.warning("Insufficient data to plot sentiment vs stock prices.")


def display_correlation_table(df):
    """Display the correlation analysis table."""
    if not df.empty:
        st.dataframe(df.style.format({"Correlation": "{:.2f}"}))
    else:
        st.write("No correlation data available to display.")


def main():
    """Main function to run the Streamlit dashboard."""
    st.title('📈 Financial News Sentiment Analysis Dashboard')
    st.markdown("""
    This dashboard analyzes the correlation between financial news sentiment and stock market movements.
    Use the sidebar to navigate through different sections.
    """)

    # Sidebar for navigation
    st.sidebar.header("Navigation")
    options = st.sidebar.radio("Go to", ["Correlation Analysis", "Stock Analysis", "About"])

    if options == "Correlation Analysis":
        st.header("🔗 Correlation Analysis Results")
        correlation_df = load_correlation_data()
        display_correlation_table(correlation_df)
        st.subheader("📊 Correlation Results Plot")
        plot_correlation_results(correlation_df)

    elif options == "Stock Analysis":
        st.header("📉 Stock Price and Sentiment Analysis")
        news_df = load_news_data()

        # Sidebar for stock selection
        symbol = st.selectbox('Select Stock Symbol', STOCK_SYMBOLS)
        if symbol:
            stock_df = load_stock_data(symbol)

            st.subheader(f"💹 Historical Closing Prices for {symbol}")
            plot_stock_price(stock_df, symbol)

            st.subheader(f"🗣️ Sentiment Scores vs Closing Prices for {symbol}")
            plot_sentiment_vs_stock(stock_df, news_df[news_df['stock'] == symbol], symbol)

    elif options == "About":
        st.header("ℹ️ About")
        st.markdown("""
        **Financial News Sentiment Analysis Dashboard** helps in understanding the relationship between news sentiment and stock performance.
        
        **Features:**
        - **Correlation Analysis**: View the correlation coefficients between news sentiment and stock returns.
        - **Stock Analysis**: Analyze historical stock prices alongside sentiment scores derived from news headlines.
        
        **Technologies Used:**
        - **Pandas** for data manipulation
        - **Streamlit** for interactive dashboard
        - **Matplotlib & Seaborn** for visualization
        - **TextBlob** for sentiment analysis
        
        **Project Objective:**
        To enhance predictive analytics capabilities by uncovering how financial news sentiment influences stock market movements, thereby informing investment strategies.
        """)

    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2024 Nova Financial Insights")


if __name__ == "__main__":
    main()
