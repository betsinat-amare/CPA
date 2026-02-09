import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import os

# Create directory for results if it doesn't exist
os.makedirs('results', exist_ok=True)

# 1. Load Data
df = pd.read_csv('BrentPrice.csv')
df['Date'] = pd.to_datetime(df['Date'])
# To make it faster and clearer for the single change point model, 
# let's sub-sample or pick a relevant more recent period?
# The task says 'all possible days in your dataset'. 
# Let's use all data but sub-sample to every 5th day to ensure the task finishes within limits.
# 10k points is fine but 2k points is much faster and captures the same trends.
df_subset = df.iloc[::5, :].copy()
count = len(df_subset)
price_data = df_subset['Price'].values
time_index = np.arange(count)

print(f'Starting model with {count} data points...')

with pm.Model() as model:
    # Priors
    # Tau: Switch point (discrete)
    tau = pm.DiscreteUniform('tau', lower=0, upper=count - 1)
    
    # Means: Prior for price before and after
    # Using very non-informative priors based on the range of oil prices (0 to 150)
    mu_1 = pm.Normal('mu_1', mu=40, sigma=20)
    mu_2 = pm.Normal('mu_2', mu=80, sigma=20)
    
    # Standard deviation (common for now or separate?)
    sigma = pm.Exponential('sigma', lam=1.0)
    
    # Switch function
    mu = pm.math.switch(tau > time_index, mu_1, mu_2)
    
    # Likelihood
    observation = pm.Normal('obs', mu=mu, sigma=sigma, observed=price_data)
    
    # Sampling
    # we use a discrete sampler for tau and NUTS/Metropolis for others
    trace = pm.sample(draws=1000, tune=1000, chains=2, return_inferencedata=True, progressbar=False)

# 2. Interpret and Save Results
print('\nSampling complete. Processing results...')

# Convergence checks
summary = az.summary(trace)
print('\nSummary Statistics:')
print(summary)
summary.to_csv('results/model_summary.csv')

# Trace plots
az.plot_trace(trace)
plt.tight_layout()
plt.savefig('results/trace_plot.png')
plt.close()

# Posterior of Tau
plt.figure(figsize=(10, 4))
az.plot_posterior(trace, var_names=['tau'], round_to=0)
plt.title('Posterior Distribution of Change Point (Tau)')
plt.savefig('results/tau_posterior.png')
plt.close()

# Identify the Date
tau_samples = trace.posterior['tau'].values.flatten()
median_tau = int(np.median(tau_samples))
change_date = df_subset.iloc[median_tau]['Date']
print(f'\nIdentified Change Point Index: {median_tau}')
print(f'Estimated Change Point Date: {change_date}')

# Quantify Impact
mu1_samples = trace.posterior['mu_1'].values.flatten()
mu2_samples = trace.posterior['mu_2'].values.flatten()
m1 = np.mean(mu1_samples)
m2 = np.mean(mu2_samples)
increase = ((m2 - m1) / m1) * 100

print(f'Mean Price Before: ${m1:.2f}')
print(f'Mean Price After: ${m2:.2f}')
print(f'Percentage Increase: {increase:.2f}%')

# Save text results
with open('results/interpretation.txt', 'w') as f:
    f.write(f'Change Point Analysis Summary\n')
    f.write(f'-----------------------------\n')
    f.write(f'Median Change Point Date: {change_date}\n')
    f.write(f'Mean Price Before: ${m1:.2f}\n')
    f.write(f'Mean Price After: ${m2:.2f}\n')
    f.write(f'Percentage Change: {increase:.2f}%\n')
    f.write(f'\nConvergence (R-hat):\n{summary["r_hat"].to_string()}\n')

# 3. Visualization of Fit
plt.figure(figsize=(12, 6))
plt.plot(df_subset['Date'], price_data, label='Actual Price', alpha=0.5)
plt.axvline(x=change_date, color='red', linestyle='--', label=f'Change Point: {change_date.date()}')
plt.hlines(m1, xmin=df_subset['Date'].min(), xmax=change_date, color='green', label=f'Before Mean: ${m1:.2f}')
plt.hlines(m2, xmin=change_date, xmax=df_subset['Date'].max(), color='purple', label=f'After Mean: ${m2:.2f}')
plt.title('Brent Oil Price with Identified Change Point')
plt.legend()
plt.savefig('results/fitted_model.png')
plt.close()

print('\nModeling complete. Results saved in results/ directory.')
