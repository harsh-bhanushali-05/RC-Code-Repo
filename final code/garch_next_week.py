import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from arch import arch_model
import numpy as np

# Load and prepare the data
data = pd.read_csv('S&P 500 all-Table 1.csv')
data.dropna(how='all', inplace=True)
data['Returns'] = data['Last Px'].pct_change()
data.dropna(subset=['Returns'], inplace=True)  # Drop rows with NaN returns
data['Scaled_Returns'] = data['Returns'] * 100  # Scale the returns

# Split the data into training and testing sets
train_size = int(len(data) * 0.7)
train_data = data['Scaled_Returns'][:train_size]
test_data = data['Scaled_Returns'][train_size:]

# Fit the GARCH model on the training data
garch_model = arch_model(train_data, vol='Garch', p=1, q=1)
model_result = garch_model.fit(disp='off')

# Forecast volatility on the test data
forecast_horizon = len(test_data)
forecasts = model_result.forecast(horizon=forecast_horizon, method='simulation')
forecasted_volatility = np.sqrt(forecasts.variance.values[-1, :])

# Calculate actual volatility using a rolling window on the test data
window_size = forecast_horizon
actual_volatility = test_data.rolling(window=window_size).std().dropna()

# Ensure that the lengths of actual_volatility and forecasted_volatility are the same
min_length = min(len(actual_volatility), len(forecasted_volatility))
actual_volatility = actual_volatility[-min_length:]
forecasted_volatility = forecasted_volatility[-min_length:]
# actual_volatility=actual_volatility*100
# Calculate error metrics
mae = mean_absolute_error(actual_volatility, forecasted_volatility)
mse = mean_squared_error(actual_volatility, forecasted_volatility)
rmse = np.sqrt(mse)
print("Mean: " ,np.mean(actual_volatility))
print("Mean: " ,np.mean(forecasted_volatility))
print("Mean Absolute Error:", mae)
print("Error % is --> " , mae/np.mean(actual_volatility)*100 , "%")
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)