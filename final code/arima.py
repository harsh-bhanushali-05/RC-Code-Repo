import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def test(data):
    dftest = adfuller(data, autolag='AIC')
    print("1. ADF : ", dftest[0])
    print("2. P-Value : ", dftest[1])
    print("3. Num Of Lags : ", dftest[2])
    print("4. Num Of Observations Used For ADF Regression and Critical Values Calculation :", dftest[3])
    print("5. Critical Values :")
    for key, val in dftest[4].items():
        print("\t", key, ": ", val)

file_path = 'NASDAQ all-Table 1.csv'
data = pd.read_csv(file_path)
data.dropna(how='all', inplace=True)
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
data = data.iloc[::-1].reset_index(drop=True)

# Example usage of the test function (assuming you want to test the 'Last Px' column)
# Make sure to replace 'Last Px' with the actual column name you want to test
if 'Last Px' in data.columns:
    test(data['Last Px'])

data.plot()  # Specify the column(s) you want to plot, e.g., data['Last Px'].plot()
plt.show()
