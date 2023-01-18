import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import log_loss, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from mnist_functions import load_mnist

x_train, x_test, y_train, y_test = load_mnist(path=r"mnist")
# 784 pixel (28*28) per foto con 70k righe (60k train, 10k test)

mms = MinMaxScaler()
x_train = mms.fit_transform(x_train)
x_test = mms.transform(x_test)

# le rete neurali non sempre possono essere usate perchè hanno mille iperparametri
# partire da modelli più semplici e.g. RL

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_proba = lr.predict_proba(x_test)
print("TEST\nAccuracy=", accuracy_score(y_test, y_pred))
print("Log loss=", log_loss(y_test, y_pred_proba))

y_pred = lr.predict(x_train)
y_pred_proba = lr.predict_proba(x_train)
print("\nTRAIN\nAccuracy=", accuracy_score(y_train, y_pred))
print("Log loss=", log_loss(y_train, y_pred_proba))

# log loss 0.31 e 0.34 --> scartare modello

iper_parameters = [[100, 1], [512, 2]]	#number of nodes, number of layers
for parameter in iper_parameters:
	mlp = MLPClassifier(hidden_layer_sizes=(parameter[0], parameter[1]), verbose = True)
	mlp.fit(x_train, y_train)
	y_pred = mlp.predict(x_test)
	y_pred_proba = mlp.predict_proba(x_test)
	print("TEST\nAccuracy=", accuracy_score(y_test, y_pred))
	print("Log loss=", log_loss(y_test, y_pred_proba))

	y_pred = mlp.predict(x_train)
	y_pred_proba = mlp.predict_proba(x_train)
	print("\nTRAIN\nAccuracy=", accuracy_score(y_train, y_pred))
	print("Log loss=", log_loss(y_train, y_pred_proba))

for i in range(0, len(x_test)):
	if y_pred[i] != y_test[i]:
		print("Predizione:", y_pred[i], "Reale:", y_test[i])
		plt.imshow(x_test[i].reshape([28,28]), cmap='gray')
		plt.show()

