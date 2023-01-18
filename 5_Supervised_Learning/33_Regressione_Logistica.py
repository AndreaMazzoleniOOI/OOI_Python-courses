import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss

def showBounds(model, X, Y, labels=["Negativo", "Positivo"]):
	h = .02

	x_min, x_max = X[:, 0].min(), X[:, 0].max()
	y_min, y_max = X[:, 1].min(), X[:, 1].max()

	xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
						 np.arange(y_min, y_max, h))

	Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

	Z = Z.reshape(xx.shape)
	plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

	X_m = X[Y == 1]
	X_b = X[Y == 0]
	plt.scatter(X_b[:, 0], X_b[:, 1], c="green", edgecolor='white', label=labels[0])
	plt.scatter(X_m[:, 0], X_m[:, 1], c="red", edgecolor='white', label=labels[1])
	plt.legend()



breast_cancer = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data",
                           names=["id","diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"])

# 569 esempi, 31 proprietà e 1 target (diagnosis: M o B (variabili categoriche)
# ottengo tutto sempre da breast_cancer.unique() e .info()
# usiamo radius_se e #concave points_worst

X = breast_cancer[["radius_se", "concave points_worst"]].values
Y = breast_cancer["diagnosis"]

le = LabelEncoder()			# label encoding
Y = le.fit_transform(Y)

std = StandardScaler()		# data standardization
X_std = std.fit_transform(X)

x_train, x_test, y_train, y_test = train_test_split(X_std, Y, test_size=0.3, random_state=0)

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_prob = lr.predict_proba(x_test)
print("ACCURACY: ", accuracy_score(y_test, y_pred))
print("LOG L(w): ", 1-log_loss(y_test, y_pred_prob))	# log_loss = 1 - log likelihood

fig = showBounds(lr, x_train, y_train, labels=["Benigno", "Maligno"])
plt.title("Train dataset")
fig = plt.show()


fig = showBounds(lr, x_test, y_test, labels=["Benigno", "Maligno"])
plt.title("Test dataset")
fig = plt.show()

''' Logistic regression con tutte le proprietà '''

X = breast_cancer.drop(["id", "diagnosis"], axis=1).values
Y = breast_cancer["diagnosis"].values

le = LabelEncoder()			# label encoding
Y = le.fit_transform(Y)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

std = StandardScaler()		# data standardization
x_train = std.fit_transform(x_train)
x_test = std.transform((x_test))

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_prob = lr.predict_proba(x_test)
print("ACCURACY: ", accuracy_score(y_test, y_pred))
print("LOG L(w): ", 1-log_loss(y_test, y_pred_prob))	# log_loss = 1 - log likelihood

# regolarizzazione: logistic regression ha come valori di regolarizzazione default L2 e C=1/lambda=1)
#possono essere cambiati come lr = LogisticRegression(penalty = l2, C=1)

