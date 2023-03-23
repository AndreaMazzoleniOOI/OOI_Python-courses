import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
from sklearn.svm import SVC
import viz

X, Y = make_circles(noise=0.2, factor=0.5, random_state=0)		# un database random con due colonne per le proprietà e una come target (Y)

plt.scatter(X[:,0],X[:,1], c=Y)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

kernel = ["linear", "rbf", "sigmoid", "poly"]
for k in kernel:
	svc = SVC(kernel = k, probability=True)
	svc.fit(x_train, y_train)

	y_pred = svc.predict(x_test)

	print(k, "accuracy= Train=", svc.score(x_train, y_train), "Test=", svc.score(x_test, y_test))
	viz.plot_bounds((x_train, x_test), (y_train, y_test), svc)
