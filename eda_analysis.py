import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller
import os

# Create directory for results if it doesn't exist
os.makedirs('results', exist_ok=True)

# 1. Load Data
df = pd.read_csv('BrentPrice.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# 2. Plot Raw Prices
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Price'], label='Brent Oil Price')
plt.title('Brent Oil Prices (1987-2022)')
plt.xlabel('Date')
plt.ylabel('USD per Barrel')
plt.grid(True)
plt.legend()
plt.savefig('results/brent_prices.png')
plt.close()

# 3. Log Returns Analysis
df['Log_Price'] = np.log(df['Price'])
df['Log_Returns'] = df['Log_Price'].diff()
df = df.dropna()

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Log_Returns'], label='Log Returns', color='orange', alpha=0.7)
plt.title('Brent Oil Daily Log Returns')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.grid(True)
plt.legend()
plt.savefig('results/log_returns.png')
plt.close()

# 4. Stationarity Testing (ADF)
def run_adf(series, name):
    print(f'\n--- ADF Test for {name} ---')
    result = adfuller(series)
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    for key, value in result[4].items():
        print(f'Critical Value ({key}): {value}')
    if result[1] <= 0.05:
        print('Result: Stationary (Reject Null Hypothesis)')
    else:
        print('Result: Non-Stationary (Fail to Reject Null Hypothesis)')

run_adf(df['Price'], 'Raw Price')
run_adf(df['Log_Returns'], 'Log Returns')

# 5. Volatility Patterns (Rolling Standard Deviation)
df['Rolling_Vol'] = df['Log_Returns'].rolling(window=30).std()
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Rolling_Vol'], color='red', label='30-day Rolling Volatility')
plt.title('Brent Oil Price Volatility (30-day Rolling STD)')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.grid(True)
plt.legend()
plt.savefig('results/volatility.png')
plt.close()

print('\nEDA complete. Figures saved in results/ directory.')
