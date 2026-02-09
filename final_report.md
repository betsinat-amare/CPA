# Brent Oil Price Analysis: Final Project Report

## Executive Summary
This project successfully analyzed the historical Brent oil price series (1987-2022) to identify structural breaks and quantify the impact of geopolitical and economic events. Using Bayesian Change Point Detection, we identified a primary regime shift in 2005, transitioning the market from a low-price environment (~$21/bbl) to a high-price era (~$76/bbl).

## Key Findings

### 1. Statistical Properties
- **Non-Stationarity**: Raw price data exhibits a strong stochastic trend, confirmed by an ADF test (p-value: 0.187).
- **Volatility Clustering**: Log returns are stationary (p-value: <0.001) but show significant clustering during historical shocks.

### 2. Bayesian Change Point Analysis
- **Detected Shift**: March 2, 2005.
- **Regime Transition**:
    - **Before Mean**: $21.46
    - **After Mean**: $75.90
    - **Relative Impact**: +253.7%
- **Confidence**: The posterior distribution for the change point $(\tau)$ showed a sharp peak, indicating high model certainty.

### 3. Event Association
The identified change point in March 2005 aligns with the rapid acceleration of global demand (led by emerging economies) and the multi-year commodity super-cycle. This shift preceded major geopolitical events like the Global Financial Crisis but established the "new normal" for energy pricing.

## Deliverables
1. **[task_2_analysis.ipynb](file:///home/betsinat/Documents/CPA/task_2_analysis.ipynb)**: Detailed code and modeling methodology.
2. **[Interactive Dashboard](file:///home/betsinat/Documents/CPA/dashboard/README.md)**: Full-stack application for stakeholder exploration.
3. **[events.csv](file:///home/betsinat/Documents/CPA/events.csv)**: Refined list of historical energy market drivers.

## Future Work
- **Multivariate Forecasting**: Incorporating GDP and inflation as explanatory variables.
- **Markov-Switching Models**: To capture recurrent high-volatility regimes (e.g., 2008 vs. 2020).
