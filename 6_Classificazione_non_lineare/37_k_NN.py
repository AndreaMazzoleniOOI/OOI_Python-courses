import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, log_loss
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
digits = load_digits()

X = digits.data
Y = digits.target

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

mms = MinMaxScaler()	# normalizzazione immagini
x_train = mms.fit_transform(x_train)
x_test = mms.transform(x_test)

''' test overfitting 
TEST RESULT
Accuracy= 0.9833333333333333
Log loss= 0.16290776370868254
TRAIN RESULT
Accuracy= 0.9896579156722355
Log loss= 0.029634635700360172

Non c'è overfitting ma proviamo a varire il valore di K'''

K = [1,2,3,4,5, 7, 10, 12, 15, 20]
f, (ax1, ax2) = plt.subplots(1, 2)
for k in K:
	knn = KNeighborsClassifier(n_neighbors=k)
	knn.fit(x_train, y_train)
	y_pred = knn.predict(x_train)
	y_pred_prob = knn.predict_proba(x_train)
	ax1.plot(k, accuracy_score(y_train, y_pred), c='Blue', marker='+')
	ax2.plot(k, log_loss(y_train, y_pred_prob), c='Blue', marker='+')

	y_pred = knn.predict(x_test)
	y_pred_prob = knn.predict_proba(x_test)
	ax1.plot(k, accuracy_score(y_test, y_pred), c='Green', marker='o')
	ax2.plot(k, log_loss(y_test, y_pred_prob), c='Green', marker='o')

ax1.scatter(None,None, c='Blue', label='Train')
ax2.scatter(None,None, c='Blue', label='Train')
ax1.scatter(None,None, c='Green', label='Test')
ax2.scatter(None,None, c='Green', label='Test')
ax1.title.set_text("Accuracy")
ax2.title.set_text("Log Loss")
ax1.legend()
ax2.legend()
ax1.grid()
ax2.grid()
plt.show()

# risultati migliore per k = 3 (o k=10) proviamo a stampare le immagini non classificate correttamente con k = 3

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

for i in range(0, len(x_test)):
	if(y_pred[i]!=y_test[i]):
		print("Numero", y_test[i]," classificato",  y_pred[i])
		plt.imshow(x_test[i].reshape([8,8]), cmap ='gray')
		plt.show()