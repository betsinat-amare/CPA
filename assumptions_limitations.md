# Assumptions and Limitations

This document outlines the statistical assumptions and practical limitations of the Brent Oil Price Change Point Analysis.

## Statistical Assumptions
1.  **Stationarity**: For certain baseline models, we assume the price returns (log-returns) follow a stationary process, though the raw prices are non-stationary.
2.  **Structural Breaks**: We assume that change points represent discrete, identifiable shifts in the underlying statistical parameters (mean and variance) of the price series.
3.  **Bayesian Prior Beliefs**: PyMC modeling requires defining priors. We assume weakly informative priors to allow the data to dominate the posterior distribution unless domain expertise suggests otherwise.

## Limitations
1.  **Data Frequency**: The analysis uses daily prices. Intraday volatility may be lost, which could be relevant for reactive events.
2.  **Multivariate Factors**: Oil prices are influenced by countless variables (interest rates, USD strength, renewable energy shifts). This analysis primarily focuses on geopolitical and economic shocks.
3.  **Lagged Effects**: The impact of an event may not be immediate. Markets often anticipate events or take time to price in the full consequences of a conflict or policy change.

## Correlation vs. Causation
It is critical to distinguish between a statistical correlation in time and a proven causal impact:
- **Statistical Correlation**: A change point model may identify a structural break on February 24, 2022.
- **Geopolitical Alignment**: This date aligns with the Russian invasion of Ukraine.
- **Causal Inference**: While the temporal alignment is strong, "proving" causation in complex global markets is difficult. Other factors (e.g., existing supply chain issues, post-COVID demand) also contribute. We use the term "associated with" or "impact quantified during" rather than "caused by" to maintain scientific rigor.

## Communication Channels
Results will be communicated through:
1.  **Interactive Dashboard (Streamlit)**: For stakeholder exploration.
2.  **Technical Report (PDF/Markdown)**: For detailed methodology and model validation.
3.  **Summary Presentation**: For high-level executive briefings.
