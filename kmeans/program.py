from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=500, centers=4, random_state=42)


kmean = KMeans(n_clusters=4, random_state=42)
kmean.fit(X)
predicted_labels = kmean.predict(X)
plt.scatter(X[:,0], X[:,1], c=predicted_labels)
plt.title("K-Means clustering")
plt.show()