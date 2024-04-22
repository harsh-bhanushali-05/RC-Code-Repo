import pandas as pd
import matplotlib.pyplot as plt

# Load the Nifty 50 data from the CSV file

file_path = 'NIFTY50-Table 1.csv'
nifty50_data = pd.read_csv(file_path)
# Data Preprocessing
# Remove rows with all missing values
nifty50_data.dropna(how='all', inplace=True)

# Fill missing numeric values with the median of the column
numeric_columns = nifty50_data.select_dtypes(include=['float64', 'int64']).columns
nifty50_data[numeric_columns] = nifty50_data[numeric_columns].fillna(nifty50_data[numeric_columns].median())

# Convert the 'Date' column to datetime format
nifty50_data['Date'] = pd.to_datetime(nifty50_data['Date'], format='%m/%d/%y')

# Convert the 'Volume' column to numeric format (in millions)
def convert_volume(volume):
    if pd.isna(volume):
        return volume
    if isinstance(volume, str):
        if volume.endswith('M'):
            return float(volume.strip('M'))
        elif volume.endswith('B'):
            return float(volume.strip('B')) * 1000  # Convert billion to million
    return float(volume)

nifty50_data['Volume'] = nifty50_data['Volume'].apply(convert_volume)

# Set the style of the plots
plt.style.use('seaborn-darkgrid')

# Plot the Nifty 50 index price over time
plt.figure(figsize=(12, 6))
plt.plot(nifty50_data['Date'], nifty50_data['Last Px'], label='Last Px')
plt.title('Nifty 50 Index Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot the Nifty 50 index volume over time
plt.figure(figsize=(12, 6))
plt.plot(nifty50_data['Date'], nifty50_data['Volume'], label='Volume', color='orange')
plt.title('Nifty 50 Index Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume (Millions)')
plt.legend()
plt.show()
#
# import pandas as pd
# import matplotlib.pyplot as plt

# Load the dataset
file_path = 'NASDAQ all-Table 1.csv'
data = pd.read_csv(file_path)

# Convert 'Date' to datetime format and set it as the index
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data = data.dropna(subset=['Date'])  # Drop rows with missing dates
data.set_index('Date', inplace=True)

# Convert 'Last Px' to numeric and handle missing values
data['Last Px'] = pd.to_numeric(data['Last Px'], errors='coerce')
data['Last Px'].fillna(method='ffill', inplace=True)  # Forward fill missing values

# Plot the time series
plt.figure(figsize=(10, 5))
plt.plot(data['Last Px'], label='NASDAQ Closing Price')

# Mark the estimated area in red dots
# plt.plot(data['Last Px'].iloc[-3000:], 'r:', label='Estimated Area')  # Example: last 30 days as estimated

plt.title('NASDAQ Closing Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()
