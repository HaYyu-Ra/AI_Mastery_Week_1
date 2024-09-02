import matplotlib.pyplot as plt
import seaborn as sns

def plot_technical_indicators(df):
    """Plot technical indicators."""
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['SMA'], label='SMA')
    plt.title('Stock Price and SMA')
    plt.legend()
    plt.show()

def plot_rsi(df):
    """Plot RSI indicator."""
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['RSI'], label='RSI')
    plt.axhline(70, linestyle='--', color='red')
    plt.axhline(30, linestyle='--', color='green')
    plt.title('Relative Strength Index (RSI)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv('data/AAPL_historical_data.csv', parse_dates=['Date'])
    df = apply_technical_indicators(df)
    plot_technical_indicators(df)
    plot_rsi(df)
