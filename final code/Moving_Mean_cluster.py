# Prepare the data for clustering
file_path = NIGFTY
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

