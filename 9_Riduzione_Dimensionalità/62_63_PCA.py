import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score, log_loss
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
import time
import seaborn as sns
sns.set()


cols = ["label","alcol","acido malico","cenere","alcalinità della cenere","magnesio",
        "fenoli totali","flavonoidi","fenoli non-flavonoidi","proantocianidine",
        "intensità del colore","tonalità", "OD280/OD315 dei vini diluiti","prolina"]


wines = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                 names=cols)
print(wines.info())
print(wines.head())

x = wines.drop("label", axis=1).values
y = wines["label"].values

ss = StandardScaler()
x = ss.fit_transform(x)

''' PCA 2D per visualizzazione '''
pca = PCA(n_components=2)
x_pc = pca.fit_transform(x)

print(x_pc)

plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.scatter(x_pc[:,0], x_pc[:,1], c=y, cmap='viridis', edgecolors='black')
plt.show()

''' SELEZIONE NUMERO COMPONENTI CON VARIANZA '''

pca = PCA(n_components=None)
pca.fit(x)

vr = pca.explained_variance_ratio_  # varianza di ogni pca
vr_cum = np.cumsum(vr)              #varianza cumulativa
print(vr)

soglia = 0.85
plt.plot(range(1, 14), vr, label="Var")
plt.plot(range(1,14), vr_cum, label="VarCum")
plt.plot(range(1,14), soglia*np.ones(13), linestyle='--', color='black')
plt.xlabel("# label")
plt.ylabel("Var, VarCum")
plt.legend()
plt.xlim(1, 13)
plt.ylim(0, 1)
plt.show()