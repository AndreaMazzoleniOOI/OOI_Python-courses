import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
sns.set()

iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                 names=['sepal length','sepal width','petal length','petal width','target'])

x = iris.drop("target", axis=1).values
y = iris["target"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

ll = LabelEncoder()
y_train = ll.fit_transform(y_train)
y_test = ll.transform(y_test)

ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test = ss.transform(x_test)

''' PCA '''
pca = PCA(n_components=2)
pca_train = pca.fit_transform(x_train)
pca_test = pca.fit_transform(x_test)

plt.scatter(pca_train[:, 0], pca_train[:, 1], c=y_train, cmap='viridis')
plt.scatter(pca_test[:, 0], pca_test[:, 1], c=y_test, alpha = 0.5, cmap='viridis')
plt.title("PCA")
plt.show()

lr = LogisticRegression()
lr.fit(pca_train, y_train)
print("PCA")
print("TRAIN Accuracy:", accuracy_score(y_train, lr.predict(pca_train)), "Log loss: ", log_loss(y_train, lr.predict(pca_train)))
print("TEST  Accuracy:", accuracy_score(y_test, lr.predict(pca_test)), "Log loss: ", log_loss(y_test, lr.predict(pca_train)))

''' LDA '''

# check bilanciamento
print(np.unique(y, return_counts=True))

lda = LDA(n_components=2)

lda_train = lda.fit_transform((x_train, y_train))   # supervisionato --> passo target
lda_test = lda.transform(x_train)

plt.scatter(lda_train[:, 0], lda_train[:, 1], c=y_train, cmap='viridis')
plt.scatter(lda_test[:, 0], lda_test[:, 1], c=y_test, alpha = 0.5, cmap='viridis')
plt.title("LDA")
plt.show()

lr = LogisticRegression()
lr.fit(lda_train, y_train)
print("\nLDA")
print("TRAIN Accuracy:", accuracy_score(y_train, lr.predict(lda_train)), "Log loss: ", log_loss(y_train, lr.predict(lda_train)))
print("TEST  Accuracy:", accuracy_score(y_test, lr.predict(lda_test)), "Log loss: ", log_loss(y_test, lr.predict(lda_train)))
