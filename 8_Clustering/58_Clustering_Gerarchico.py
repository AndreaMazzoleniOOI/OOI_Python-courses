import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import  linkage, dendrogram

x, y = make_blobs(n_samples=100, n_features=3, cluster_std=0.5, random_state=0)

plt.scatter(x[:,0], x[:,1], s=50)
plt.show()

''' Costruire matrice associazione '''

link_matrix = linkage(x, method="ward")
link_matrix = pd.DataFrame(link_matrix)	# 0,1 = identificativi cluster uniti,
										# 2 = distanza cluster, # 3 = numero punti nel cluster
''' Stampa dendrogramma '''

fig = plt.figure()
fig = dendrogram(link_matrix)
fig = plt.show()

''' Scelta soglia e clustering '''
# soglia distanza = 10 sembra una buona soglia--> 3 cluster

ac = AgglomerativeClustering(n_clusters=3)
y_pred = ac.fit_predict(x)

plt.scatter(x[:,0], x[:,1], c=y_pred, s=50, cmap="viridis", edgecolors='black')
plt.show()



