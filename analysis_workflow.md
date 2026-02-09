# Brent Oil Price Analysis Workflow

This document outlines the systematic process for analyzing Brent oil prices and detecting significant change points.

## 1. Data Ingestion & Preprocessing
- **Source**: Historical Brent oil prices (1987-2022).
- **Cleaning**: Handle missing dates, outliers, and ensure consistent price formatting.
- **Filtering**: Segment data into relevant periods for focused analysis.

## 2. Exploratory Data Analysis (EDA)
- **Trend Analysis**: Moving averages and decomposition to identify long-term patterns.
- **Stationarity Testing**: Augmented Dickey-Fuller (ADF) test to determine if the series is stable.
- **Volatility Analysis**: GARCH modeling or rolling standard deviation to identify high-instability periods.

## 3. Event Research & Mapping
- **Compilation**: Gather 10-15 significant geopolitical and economic events.
- **Alignment**: Map event dates to price fluctuations observed in the EDA phase.

## 4. Change Point Modeling
- **Methodology**: Bayesian Change Point Analysis using `PyMC`.
- **Parameter Estimation**: Detect dates of structural breaks and quantify the shift in mean/variance.
- **Validation**: Compare model results with historical event data.

## 5. Insight Generation & Reporting
- **Cause Association**: Linking statistical change points to specific geopolitical events.
- **Impact Quantification**: Measuring the magnitude of price shifts post-event.
- **Communication**: Visualizing findings in a dashboard and summarizing actionable insights for stakeholders.
