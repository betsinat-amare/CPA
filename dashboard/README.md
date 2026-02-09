# Brent Oil Price Analysis Dashboard

This folder contains the full-stack interactive dashboard for visualizing Brent oil price change point analysis.

## Structure
- `backend/`: Flask server that serve prices, events, and modeling results.
- `frontend/`: React application (Vite-powered) for interactive visualizations.

## Prerequisites
- Python 3.x
- Node.js & npm

## How to Run

### 1. Start the Backend
```bash
cd backend
pip install flask flask-cors pandas xlrd
python app.py
```
The API will run on `http://localhost:5000`.

### 2. Start the Frontend
```bash
cd frontend
npm install
npm run dev -- --port 3000
```
Open `http://localhost:3000` in your browser.

## Features
- **Price Timeline**: Interactive Area chart of historical prices.
- **Change Point Detection**: Visualizes the regime shift identified by the Bayesian model.
- **Geopolitical Events**: Hover/click events to see their historical context on the chart.
- **Key Metrics**: Real-time display of identified regime means and volatility.
