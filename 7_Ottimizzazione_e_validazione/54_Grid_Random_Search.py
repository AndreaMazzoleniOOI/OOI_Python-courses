import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

iris = pd.read_csv(r"C:\Users\andre\PycharmProjects\Machine_learning_course\2_data_processing\data\iris.csv")
X = iris.drop("species",axis=1).values
Y = iris["species"].values
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

''' Grid Search '''

svc = SVC()
params = {"kernel": ["gamma", "rbf", "sigmoid", "poly"],
		  "gamma": [0.1, 1, "auto"],
		  "C":[1, 10, 100, 1000]}

gs = GridSearchCV(svc, params, cv=10)

gs.fit(x_train, y_train)
print("PARAMETR GS:", gs.best_params_, "Accuracy:", gs.best_score_)

svc = gs.best_estimator_
print("Accuracy prediction:", svc.score(x_test, y_test))

''' Random Search '''


svc = SVC()
params = {"kernel": ["gamma", "rbf", "sigmoid", "poly"],
		  "gamma": [0.1, 1, "auto"],
		  "C":[1, 10, 100, 1000,10000]}

rs = RandomizedSearchCV(svc, params, cv=10)

rs.fit(x_train, y_train)
print("PARAMETR RS:", rs.best_params_, "Accuracy:", rs.best_score_)

svc = rs.best_estimator_
print("Accuracy prediction:", svc.score(x_test, y_test))
