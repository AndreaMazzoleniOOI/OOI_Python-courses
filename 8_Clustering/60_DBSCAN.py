import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN, KMeans, AgglomerativeClustering
from sklearn.datasets import make_moons


x, y = make_moons(n_samples=200, noise=0.05, random_state=0)

plt.scatter(x[:,0], x[:, 1])
plt.show()

''' KMEANS '''

km = KMeans(n_clusters=2)
y_km = km.fit_predict(x)

''' AGGLOMERATIVE CLUSTERING '''

ac = AgglomerativeClustering(n_clusters=2, linkage='complete')
y_ac = ac.fit_predict(x)

''' DBSCAN '''

db = DBSCAN(eps=0.25,min_samples=3)
y_db = db.fit_predict(x)

plt.subplot(311)
plt.scatter(x[:,0], x[:, 1], c=y_km)
plt.title("KMeans")
plt.subplot(312)
plt.scatter(x[:,0], x[:, 1], c=y_ac)
plt.title("Agglomerative")
plt.subplot(313)
plt.scatter(x[:,0], x[:, 1], c=y_db)
plt.title("KMeans")

plt.show()


# kmeans crea solo forme sferiche per i cluster quindi non riesce a fare correttamente questa classificazione
