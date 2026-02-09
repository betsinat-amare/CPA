# Task 1: Laying the Foundation for Analysis - Summary Report

## Overview
This report documents the foundational work for the Change Point Analysis and Statistical Modeling of Brent oil prices. The objective is to establish a rigorous analytical framework for understanding how geopolitical and economic events influence energy markets.

## Deliverables

### 1. Data Analysis Workflow
The workflow is documented in [analysis_workflow.md](file:///home/betsinat/Documents/CPA/analysis_workflow.md). It follows a five-stage process:
- Data Ingestion & Preprocessing
- Exploratory Data Analysis (EDA)
- Event Research & Mapping
- Change Point Modeling (PyMC)
- Insight Generation & Reporting

### 2. Key Geopolitical and Economic Events
A structured dataset of 13 significant events (1990–2022) has been compiled in [events.csv](file:///home/betsinat/Documents/CPA/events.csv). Key events include:
- **1990**: Invasion of Kuwait (Supply shock)
- **2008**: Global Financial Crisis (Demand shock)
- **2014**: Shale Revolution/Oil Price Crash (Oversupply)
- **2020**: COVID-19 & Russia-Saudi Price War
- **2022**: Russian Invasion of Ukraine

### 3. Assumptions and Limitations
The statistical rigor of the project is maintained by adhering to the principles documented in [assumptions_limitations.md](file:///home/betsinat/Documents/CPA/assumptions_limitations.md).
- **Core Distinction**: We clearly distinguish between **statistical correlation** (detected by models) and **causal impact** (associated via historical context).
- **Limitations**: Acknowledgment of lagged effects, intraday data gaps, and multivariate influences (USD strength, etc.).

### 4. Model and Data Understanding
The theoretical properties of the Brent oil price series and the rationale for using Bayesian Change Point models are detailed in [model_and_data_understanding.md](file:///home/betsinat/Documents/CPA/model_and_data_understanding.md).

## Current Status & Next Steps
- **Data Status**: Extensive searches for the specific daily dataset (1987-2022) were conducted across the system. The documentation has been prepared to handle the data as soon as it is ingested.
- **Immediate Task**: Load the dataset and perform the stationarity (ADF) and volatility testing outlined in the workflow.
- **Communication Channels**: Birhan Energies stakeholders will be engaged via a Streamlit dashboard and a final technical report.
