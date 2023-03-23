import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification
from sklearn.utils import shuffle

''' Per minibatch c'è .fit_partial ma devo creare i vettori di ogni batch perchè non esiste una classe dedicata in SGDClassifier'''
def minibatchGD(train_set, test_set, n_batches=1, epoches=10):

	x_train , y_train = train_set
	x_test, y_test = test_set

	batch_size = x_train.shape[0]/n_batches

	sgd = SGDClassifier(loss='log')

	sgd_loss = []

	for epoch in range(epoches):
		x_shuffled, y_shuffled = shuffle(x_train, y_train)
		for batch in range(n_batches):

			batch_start = int(batch*batch_size)
			batch_end = int((batch+1)*batch_size)

			x_batch = x_shuffled[batch_start:batch_end, :]
			y_batch = y_shuffled[batch_start:batch_end]

			sgd.partial_fit(x_batch, y_batch, classes=np.unique(y_train))

			loss = log_loss(y_test, sgd.predict_proba(x_test), labels=np.unique(y_train))
		sgd_loss.append(loss)
		print('Loss epoca', epoch+1, ":", loss)

	return (sgd, sgd_loss)



X, Y = make_classification(n_samples=1250, n_features=4, n_informative=2, random_state=0)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

''' Stochastic GD '''

sgd = SGDClassifier(loss="log", shuffle=True)
sgd.fit(x_train, y_train)

print("Loss:", log_loss(y_test, sgd.predict_proba(x_test)))


''' Full GD --> N_Batches = 1'''

full_gd, full_gd_loss = minibatchGD((x_train, y_train), (x_test, y_test), n_batches=1, epoches=200)

''' Stochastic GD usando la funzione che abbiamo scritto --> n_batches == numero esempi trainset'''
sgd, sgd_loss = minibatchGD((x_train, y_train), (x_test, y_test), n_batches=x_train.shape[0], epoches=5)

''' MiniBatche GD'''

mini_sgd, mini_sgd_loss = minibatchGD((x_train, y_train), (x_test, y_test), n_batches=10, epoches=500)

plt.rcParams['figure.figsize'] = (14, 10)
plt.plot(sgd_loss, label='Stochastic')
plt.plot(full_gd_loss, label='Full')
plt.plot(mini_sgd_loss, label='MiniBatch')
plt.grid()
plt.legend()
plt.xlim(0, 200)
plt.show()