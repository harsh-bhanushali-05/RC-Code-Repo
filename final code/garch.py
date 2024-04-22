import pandas as pd
from arch import arch_model
import matplotlib.pyplot as plt
data = pd.read_csv('S&P 500 all-Table 1.csv')
data.dropna(how='all', inplace=True)
data['Returns'] = data['Last Px'].pct_change().dropna()
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
garch_model = arch_model(data['Returns'], vol='Garch', p=1, q=1)
res = garch_model.fit(disp='off')
print(res.summary())
mu = res.params[0]
omega  = res.params[1]
alpha = res.params[2]
beta = res.params[3]



fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(data['Returns'], label='Daily Returns')
ax.plot(res.conditional_volatility, label='Volatility', color='red')
ax.set_title('S&P 500 Daily Returns and Conditional Volatility')
ax.set_xlabel('Date')
ax.set_ylabel('Returns / Volatility')
ax.legend()
plt.show()