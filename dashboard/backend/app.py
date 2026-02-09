from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Paths to data files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PRICES_PATH = os.path.join(BASE_DIR, 'BrentPrice.csv')
EVENTS_PATH = os.path.join(BASE_DIR, 'events.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

@app.route('/api/prices', methods=['GET'])
def get_prices():
    try:
        df = pd.read_csv(PRICES_PATH)
        # To keep it lightweight, we can resample or limit
        # For the dashboard, daily data for 30 years might be heavy (~9k points)
        # Let's send every 2nd point for smoother dashboard performance if needed, 
        # but for now let's send full data.
        data = df.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    try:
        df = pd.read_csv(EVENTS_PATH)
        data = df.to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/results', methods=['GET'])
def get_results():
    try:
        results = {}
        interp_path = os.path.join(RESULTS_DIR, 'interpretation.txt')
        if os.path.exists(interp_path):
            with open(interp_path, 'r') as f:
                results['summary'] = f.read()
        
        summary_csv = os.path.join(RESULTS_DIR, 'model_summary.csv')
        if os.path.exists(summary_csv):
            df_sum = pd.read_csv(summary_csv)
            results['metrics'] = df_sum.to_dict(orient='records')
            
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
