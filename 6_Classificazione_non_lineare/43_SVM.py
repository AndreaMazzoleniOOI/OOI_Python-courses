import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import LinearSVC
from viz import plot_bounds

iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
				   names=["sepal length","sepal width","petal length","petal width","class"])

X = iris.drop("class", axis=1).values
Y = iris["class"].values	# stringa

x_train, x_test, y_train, y_test= train_test_split(X,Y, test_size=0.3, random_state=0)
le = LabelEncoder()
Y = le.fit_transform(Y)

std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

''' modello su 2 proprietà '''

x2_train = x_train[:, :2]
x2_test = x_test[:, :2]

svc = LinearSVC()
svc.fit(x2_train, y_train)
y_pred = svc.predict(x2_test)
print("\nTEST\nAccuracy=", svc.score(x2_train, y_train))
y_pred = svc.predict(x2_train)
print("TEST\nAccuracy=", svc.score(x2_test,y_test))

# ha overfitting, provo con tutte le proprietà, oppure modifico C (prossime lezioni

''' tutte le proprietà'''

svc = LinearSVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
print("\nTEST\nAccuracy=", svc.score(x_train, y_train))
y_pred = svc.predict(x_train)
print("TEST\nAccuracy=", svc.score(x_test,y_test))
