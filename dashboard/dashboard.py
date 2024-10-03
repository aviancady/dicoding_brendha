import numpy as np
import matplotlib.pyplot as plt

# Ambil kolom data order_count untuk clustering
data = df_customer_order_count[['order_count']].values

# Fungsi untuk menghitung jarak Euclidean (1D)
def euclidean_distance_1d(point1, point2):
    return np.abs(point1 - point2)

# Fungsi untuk menginisialisasi centroid secara acak
def initialize_centroids_1d(data, k):
    indices = np.random.choice(len(data), k, replace=False)
    return data[indices]

# Fungsi untuk menetapkan cluster berdasarkan jarak terdekat ke centroid
def assign_clusters_1d(data, centroids):
    clusters = []
    for point in data:
        distances = [euclidean_distance_1d(point, centroid) for centroid in centroids]
        clusters.append(np.argmin(distances))
    return np.array(clusters)

# Fungsi untuk memperbarui posisi centroid
def update_centroids_1d(data, clusters, k):
    new_centroids = []
    for i in range(k):
        cluster_points = data[clusters == i]
        new_centroids.append(np.mean(cluster_points))
    return np.array(new_centroids)

# Fungsi utama K-Means 1D
def kmeans_clustering_1d(data, k, max_iterations=100):
    centroids = initialize_centroids_1d(data, k)
    for i in range(max_iterations):
        clusters = assign_clusters_1d(data, centroids)
        new_centroids = update_centroids_1d(data, clusters, k)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids

# Menggunakan fungsi K-Means pada order_count
k = 3
clusters, centroids = kmeans_clustering_1d(data, k)

# Visualisasi hasil clustering
plt.scatter(df_customer_order_count['customer_unique_id'], df_customer_order_count['order_count'], c=clusters, cmap='viridis', marker='o')
plt.scatter(range(len(centroids)), centroids, c='red', marker='x', s=100, label='Centroids')
plt.title("Clustering Customer Order Count (Manual K-Means)")
plt.xlabel("Customer ID")
plt.ylabel("Order Count")
plt.legend()
plt.show()
