# Understanding the Model and Data

This document provides a theoretical and practical overview of the data properties and the change point models used in this analysis.

## Expected Time Series Properties of Brent Oil Prices
Based on the historical context (1987-2022) of Brent oil prices:

### 1. Trend Analysis
- **Non-Stationarity**: Oil prices typically exhibit a "stochastic trend" or drift. They do not reliably return to a long-term mean, which is characteristic of a Random Walk or an I(1) process.
- **Long-term Growth**: Over several decades, there is a general upward trend driven by global inflation, increased demand from emerging markets, and resource depletion, punctuated by sharp crashes (2008, 2014, 2020).

### 2. Stationarity Testing
- **Raw Prices**: Expected to be non-stationary (highly likely to fail the Augmented Dickey-Fuller test).
- **First Differences (Log Returns)**: Usually stationary. This transformation is necessary for many statistical models to stabilize the mean and variance.

### 3. Volatility Patterns
- **Volatility Clustering**: Large changes tend to be followed by large changes, and small changes by small changes (heteroskedasticity).
- **Crisis Spikes**: High volatility is expected during the identified geopolitical events (e.g., Gulf War, 2008 Crisis, COVID-19).

## Change Point Models
Change point models are designed to identify "structural breaks" where the underlying parameters of a process change abruptly.

### Purpose
In the context of Brent oil, change point models help:
1.  **Detect Regime Shifts**: Identify when the market moved from a low-price/low-volatility regime to a high-price/high-volatility regime.
2.  **Quantify Event Impact**: Determine if an event caused a lasting shift in the price level or if it was a temporary shock.

### Bayesian Change Point Analysis (PyMC)
We use a Bayesian approach because:
- **Uncertainty Quantification**: It provides a probability distribution for the exact date of a change point, rather than a single point estimate.
- **Flexibility**: We can model multiple change points and incorporate prior knowledge about event dates.

## Expected Outputs and Limitations
### Outputs
- **Change Point Dates**: Probabilistic estimates of when structural breaks occurred.
- **Parameter Shifts**: The new mean and standard deviation of prices after each change point.
- **Associative Mapping**: Linking the detected dates to the `events.csv` dataset.

### Limitations
- **Model Complexity**: As the number of change points increases, the computational cost and risk of over-fitting grow.
- **Instantaneous vs. Gradual**: Change point models often assume sudden shifts. Some market changes are gradual (e.g., the transition to renewable energy), which may be harder to detect as a single "point."
- **Data Frequency**: Daily noise can sometimes mask legitimate structural breaks if the shift is subtle.
