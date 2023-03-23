import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_circles
from sklearn.metrics import accuracy_score, log_loss
from sklearn.decomposition import KernelPCA
import seaborn as sns
import viz
sns.set()

x, y = make_circles(n_samples=1000, noise=0.1, factor=0.2, random_state=1)
plt.scatter(x[:,0], x[:,1], c=y, cmap='viridis')
plt.show()

lr = LogisticRegression()
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)
lr.fit(x_train, y_train)
print("NO KERNEL")
print("TEST\nAccuracy:", accuracy_score(y_test, lr.predict(x_test)), "\nLog loss:", log_loss(y_test, lr.predict_proba(x_test)))
print("TRAIN\nAccuracy:", accuracy_score(y_train, lr.predict(x_train)), "\nLog loss:", log_loss(y_train, lr.predict_proba(x_train)))
print(x[:5,:])
viz.show_bounds(lr, x, y)
plt.show()

''' KernelPCA '''

kpca = KernelPCA(kernel='rbf', gamma=5)
kpc = kpca.fit_transform(x)

plt.subplot(2,1,1)
plt.scatter(kpc[:, 0], kpc[:, 1], c=y, cmap='viridis')
plt.subplot(2,1,2)
plt.scatter(kpc[:,0], np.zeros(len(kpc[:,0])), c=y, cmap='viridis')
plt.show()	# possiamo vedere come solo la prima componente fornisca abbastanza informazioni

kpc = kpc[:, 0].reshape(-1,1)

lr = LogisticRegression()
x_train, x_test, y_train, y_test = train_test_split(kpc, y, test_size=0.2, random_state=0)
lr.fit(x_train, y_train)
print("\nKERNEL RBF")
print("TEST\nAccuracy:", accuracy_score(y_test, lr.predict(x_test)), "\nLog loss:", log_loss(y_test, lr.predict_proba(x_test)))
print("TRAIN\nAccuracy:", accuracy_score(y_train, lr.predict(x_train)), "\nLog loss:", log_loss(y_train, lr.predict_proba(x_train)))
