import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = 'S&P 500 all-Table 1.csv'
data = pd.read_csv(file_path)
data.dropna(how='all', inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
data.sort_index(inplace=True)
data['Returns'] = data['Last Px'].pct_change()
data.dropna(subset=['Returns'], inplace=True)

# Monte Carlo simulation parameters
num_simulations = 1000
num_days = 90  # Approximate number of trading days in 3 months

# Calculate daily returns
returns = data['Returns']

# Initialize the matrix to store the simulation results
simulated_prices = np.zeros((num_days, num_simulations))
s`
# Set the last observed price as the starting price for all simulations
simulated_prices[0, :] = data['Last Px'].iloc[-1]

# Simulate the stock price for each day and each simulation
for day in range(1, num_days):
    daily_returns = np.random.choice(returns, size=num_simulations)
    simulated_prices[day, :] = simulated_prices[day - 1, :] * (1 + daily_returns)

# Plot the simulated stock price paths
plt.figure(figsize=(10, 6))
for i in range(num_simulations):
    plt.plot(simulated_prices[:, i], color='grey', alpha=0.1)
plt.title('Monte Carlo Simulation of Stock Price for Next 3 Months')
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.show()

# Calculate the average predicted stock price at the end of 3 months
average_predicted_price = np.mean(simulated_prices[-1, :])
print('Average predicted stock price:', average_predicted_price)
