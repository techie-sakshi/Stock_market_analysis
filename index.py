# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

# Step 1: Load and Inspect the Data
# ---------------------------------
# Load the dataset
df = pd.read_csv('infy_stock.csv')

# Display the first 10 rows
print("First 10 rows of the dataset:")
print(df.head(10))

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Step 2: Data Visualization
# --------------------------

# Convert 'Date' to datetime for better plotting
df['Date'] = pd.to_datetime(df['Date'])

# Plot the closing price over time
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

# Plot a candlestick chart using mplfinance of last 200 days
df_candle = df.set_index('Date').tail(200)
mpf.plot(df_candle, type='candle', style='charles', title='Candlestick Chart(last 200 data)', volume=True)


# Step 3: Statistical Analysis
# ----------------------------

# Calculate daily return percentage
df['Daily Return %'] = ((df['Close'] - df['Open']) / df['Open']) * 100
print("\nDaily Return Percentage:")
print(df[['Date', 'Daily Return %']].head())

# Calculate average and median of daily returns
avg_return = df['Daily Return %'].mean()
median_return = df['Daily Return %'].median()

print(f"\nAverage Daily Return: {avg_return}%")
print(f"Median Daily Return: {median_return}%")

# Calculate the standard deviation of the closing prices
std_close = df['Close'].std()
print(f"Standard Deviation of Closing Prices: {std_close}")

# Step 4: Moving Averages
# -----------------------

# Calculate 50-day and 200-day moving averages
df['50 Day MA'] = df['Close'].rolling(window=50).mean()
df['200 Day MA'] = df['Close'].rolling(window=200).mean()

# Plot the moving averages along with the closing price
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')
plt.plot(df['Date'], df['50 Day MA'], label='50 Day Moving Average', color='red')
plt.plot(df['Date'], df['200 Day MA'], label='200 Day Moving Average', color='green')
plt.title('Moving Averages (50-day and 200-day) with Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Step 5: Volatility Analysis
# ---------------------------

# Calculate rolling standard deviation (volatility) for 30 days
df['Volatility (30 Day)'] = df['Close'].rolling(window=30).std()

# Plot the volatility
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Volatility (30 Day)'], label='30 Day Rolling Volatility', color='purple')
plt.title('30 Day Rolling Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()

# Step 6: Trend Analysis
# ----------------------

# Identify bullish and bearish trends
df['Trend'] = 'Neutral'
df.loc[df['50 Day MA'] > df['200 Day MA'], 'Trend'] = 'Bullish'
df.loc[df['50 Day MA'] < df['200 Day MA'], 'Trend'] = 'Bearish'

# Plot the trends
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='blue')

# Highlight bullish and bearish regions
bullish = df[df['Trend'] == 'Bullish']
bearish = df[df['Trend'] == 'Bearish']

plt.scatter(bullish['Date'], bullish['Close'], color='green', label='Bullish Trend', marker='^', alpha=0.7)
plt.scatter(bearish['Date'], bearish['Close'], color='red', label='Bearish Trend', marker='v', alpha=0.7)

plt.title('Bullish and Bearish Trends')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
