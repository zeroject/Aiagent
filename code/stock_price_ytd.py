# filename: stock_price_ytd.py

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_price_ytd(ticker):
    # Get historical data for YTD
    data = yf.download(ticker, period='ytd')
    
    # Extract the date from the original data
    data['Date'] = pd.to_datetime(data.index)
    
    # Calculate the percentage change in price
    data['Price Change'] = (data['Close'].pct_change() * 100).fillna(0)
    
    # Create a new DataFrame with only the necessary columns
    ytd_data = data[['Date', 'Close']]
    
    # Print the summary statistics
    print("Summary Statistics:")
    print(ytd_data.describe())
    
    # Plot the chart
    plt.figure(figsize=(10,6))
    plt.plot(ytd_data['Date'], ytd_data['Close'])
    plt.title(f'{ticker} YTD Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.savefig('stock_price_ytd.png')
    
    # Print the mean and standard deviation of the closing price
    print("Mean:", ytd_data['Close'].mean())
    print("Standard Deviation:", ytd_data['Close'].std())

# Specify the ticker symbol
ticker = 'AAPL'  # Apple Inc.
get_stock_price_ytd(ticker)

print("Script execution completed.")