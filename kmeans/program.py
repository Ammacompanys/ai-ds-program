from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

x, y = make_blobs(n_samples=500, centers=4, random_state=42)
kmean = KMeans(n_clusters=4, random_state=42)
kmean.fit(x)
predicted_labels = kmean.predict(x)
plt.scatter(x[:,0], x[:,1], c=predicted_labels)
plt.title("K-Means clustering")
plt.show()