import pandas as pd
import numpy as np
import yfinance as yf

# Define the cryptocurrencies you want to analyze
symbols = ['BTC-USD', 'ETH-USD']

# Fetch historical data from Yahoo Finance
df = pd.DataFrame()
for symbol in symbols:
    data = yf.download(symbol, start='2010-01-01', end='2023-02-22')
    data['symbol'] = symbol
    df = df.append(data)

# Calculate daily percentage change and moving averages
df['daily_pct_change'] = df['Adj Close'].pct_change()
df['30_day_ma'] = df['Adj Close'].rolling(window=30).mean()
df['90_day_ma'] = df['Adj Close'].rolling(window=90).mean()

# Pivot the DataFrame to create separate columns for each cryptocurrency
df = df.pivot_table(index='Date', columns='symbol', values='Adj Close')

# Create a DataFrame to store the results
results = pd.DataFrame(index=df.index)

# Determine which cryptocurrency had the highest daily percentage change on each day
results['highest_daily_pct_change'] = df['daily_pct_change'].idxmax(axis=1)

# Determine which cryptocurrency had the highest closing price on each day
results['highest_closing_price'] = df.idxmax(axis=1)

# Determine which cryptocurrency had the highest 30-day moving average on each day
results['highest_30_day_ma'] = df['30_day_ma'].idxmax(axis=1)

# Determine which cryptocurrency had the highest 90-day moving average on each day
results['highest_90_day_ma'] = df['90_day_ma'].idxmax(axis=1)

# Render the results as an HTML table
html_table = results.tail().to_html()

# Print the HTML table to the console
print(html_table)
