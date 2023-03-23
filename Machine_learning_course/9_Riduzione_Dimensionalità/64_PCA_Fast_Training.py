import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, log_loss
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from time import time
import mnist

sns.set()
''' quando minst funzionerà sostituire tutto quello qui in mezzo con la linea di codice sotto per cambiare DS'''
#x_train, x_test, y_train, y_test = mnist.load_mnist(path="mnist")

cols = ["label","alcol","acido malico","cenere","alcalinità della cenere","magnesio",
        "fenoli totali","flavonoidi","fenoli non-flavonoidi","proantocianidine",
        "intensità del colore","tonalità", "OD280/OD315 dei vini diluiti","prolina"]


wines = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                 names=cols)

x = wines.drop("label", axis=1).values
y = wines["label"].values
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=0)
'''----------------------------------------------------------------------------------------------'''

print("Numero totale proprietà:", x_train.shape[1])
print("Esempi di training:", x_train.shape[0])
print("Esempi di test:", x_test.shape[0])


mms = MinMaxScaler()
x_train = mms.fit_transform(x_train)
x_test = mms.transform(x_test)

''' Addestramento con tutte le proprietà '''
lr = LogisticRegression()
start_time = time()
lr.fit(x_train, y_train)
end_time = time()
print("Tempo addestramento:", end_time-start_time)
print("TEST\nAccuracy:", accuracy_score(y_test, lr.predict(x_test)), "\nLog loss:", log_loss(y_test, lr.predict_proba(x_test)))
print("TRAIN\nAccuracy:", accuracy_score(y_train, lr.predict(x_train)), "\nLog loss:", log_loss(y_train, lr.predict_proba(x_train)))

''' PCA '''

lr = LogisticRegression()
alphas = np.arange(0.05, 1, 0.05)
accuracy_test = []
accuracy_train = []
log_loss_test = []
log_loss_train = []
times = []
n_prop = []

for alpha in alphas:
	pca = PCA(alpha)
	start_time = time()
	x_train_pca = pca.fit_transform(x_train)
	x_test_pca = pca.transform(x_test)
	lr.fit(x_train_pca, y_train)
	end_time = time()

	print("\nVarianza mantenuta:", alpha)
	print("Numero proprietà:", x_train_pca.shape[1])
	print("Tempo addestramento:", end_time-start_time)
	print("TEST\nAccuracy:", accuracy_score(y_test, lr.predict(x_test_pca)), "\nLog loss:", log_loss(y_test, lr.predict_proba(x_test_pca)))
	print("TRAIN\nAccuracy:", accuracy_score(y_train, lr.predict(x_train_pca)), "\nLog loss:", log_loss(y_train, lr.predict_proba(x_train_pca)))
	accuracy_train.append(accuracy_score(y_train, lr.predict(x_train_pca)))
	accuracy_test.append(accuracy_score(y_test, lr.predict(x_test_pca)))
	log_loss_test.append(log_loss(y_test, lr.predict_proba(x_test_pca)))
	log_loss_train.append(log_loss(y_train, lr.predict_proba(x_train_pca)))
	times.append(end_time-start_time)
	n_prop.append(x_train_pca.shape[1])

plt.subplot(221)
plt.plot(alphas, accuracy_train, color='green', label='Train', marker='.')
plt.plot(alphas, accuracy_test, color='red', label='Test', marker='.')
plt.xlim(0, np.max(alphas))
plt.legend()
plt.title("Accuracy")

plt.subplot(222)
plt.xlim(0, np.max(alphas))
plt.plot(alphas, log_loss_train, color='green', label='Train', marker='.')
plt.plot(alphas, log_loss_test, color='red', label='Test', marker='.')
plt.legend()
plt.title("Log loss")

plt.subplot(223)
plt.xlim(0, np.max(alphas))
plt.plot(alphas, times, color='blue', marker='.')
plt.title("Time")

plt.subplot(224)
plt.xlim(0, np.max(alphas))
plt.plot(alphas, n_prop, color='blue', marker='.')
plt.title("Numero proprietà")

plt.show()
