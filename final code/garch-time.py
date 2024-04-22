import pandas as pd
from arch import arch_model
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('NASDAQ all-Table 1.csv')
# data = pd.read_csv('NIFTY50-Table 1.csv')
data.dropna(how='all', inplace=True)

# Calculate the daily returns using the 'Last Px' column
data['Returns'] = data['Last Px'].pct_change().dropna()
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')

# Remove rows with NaN values in the 'Last Px' column
# data = data.dropna(subset=['Last Px'])®

data.dropna(how='all', inplace=True)

# Calculate the daily returns using the 'Last Px' column
data['Returns'] = data['Last Px'].pct_change().dropna()
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())


# Fit a GARCH(1,1) model to the returns
garch_model = arch_model(data['Returns'], vol='Garch', p=1, q=1)
res = garch_model.fit(disp='off')

# Print the model summary
print(res.summary())

# Plot the fitted conditional volatility
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data['Date'],data['Returns'], label='Daily Returns')
ax.plot(res.conditional_volatility, label='Volatility', color='red')
ax.set_title('S&P 500 Daily Returns and Conditional Volatility')
ax.set_xlabel('Date')
ax.set_ylabel('Returns / Volatility')
plt.xticks(rotation=45)
ax.legend()
plt.show()



