import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


X, Y = make_blobs(n_samples=500, centers=4, cluster_std=0.8, random_state=0)

plt.scatter(X[:,0], X[:,1], s=50)
plt.show()

''' scelta k '''
ssd = {}
for k in range(1, 10):
	km = KMeans(init="k-means++", n_clusters=k)	# kmeans ++ ottimizza la selezione random dei centroidi
	km.fit(X)
	ssd[k] = km.inertia_
plt.plot(list(ssd.keys()), list(ssd.values()), marker='o')
plt.xlabel("K")
plt.ylabel("SSD")
plt.show()

# k = 4 è dove cambia pendenza

km = KMeans(n_clusters=4)
km.fit(X)
y_pred = km.predict(X)
centers = km.cluster_centers_	#coordinate centroidi

plt.scatter(X[:,0], X[:,1], s=50, c=y_pred)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.show()

