import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = 'NIFTY50-Table 1.csv'
nifty50_data = pd.read_csv(file_path)

# Convert the 'SMAVG(15)' column to numeric format (in millions)
def convert_smavg(value):
    if pd.isna(value):
        return value
    if isinstance(value, str):
        if value.endswith('M'):
            return float(value.strip('M'))
        elif value.endswith('B'):
            return float(value.strip('B')) * 1000  # Convert billion to million
    return float(value)

nifty50_data['SMAVG(15)'] = nifty50_data['SMAVG(15)'].apply(convert_smavg)

# Prepare the data for clustering
cluster_data = nifty50_data[['Last Px', 'SMAVG(15)']].dropna()

# Standardize the data
scaler = StandardScaler()
scaled_cluster_data = scaler.fit_transform(cluster_data)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(scaled_cluster_data)

# Add the clusters to the DataFrame
cluster_data['Cluster'] = clusters

# Plot the data with clusters
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Last Px', y='SMAVG(15)', hue='Cluster', data=cluster_data, palette='Set2')
plt.title('Clustering of Nifty 50 Index Price and 15-Day SMA')
plt.xlabel('Last Px')
plt.ylabel('SMAVG(15)')
plt.legend(title='Cluster')
plt.show()

