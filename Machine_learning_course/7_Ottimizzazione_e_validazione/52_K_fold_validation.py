import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

iris = pd.read_csv(r"C:\Users\andre\PycharmProjects\Machine_learning_course\2_data_processing\data\iris.csv")
X = iris.drop("species",axis=1).values
Y = iris["species"].values
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

''' Opzione 1: Creare il modello '''
lr = LogisticRegression()
kfold = KFold(n_splits=10, random_state=1)
scores=[]	# vettore accuracy di ogni modello su ogni fold

for k, (train, test) in enumerate(kfold.split(x_train, y_train)):

	lr.fit(x_train[train], y_train[train])
	score = lr.score(x_train[test], y_train[test])
	scores.append(score)
	print("Fold", k, "Accuracy:", score)
print("Validation accuracy:", np.mean(scores))

''' Opzione 2: uso score cross_val_score'''

lr = LogisticRegression()
scores = cross_val_score(lr, x_train, y_train, cv=10)
print("Validation accuracy:", np.mean(scores))

''' Dopo aver validato il modello sempre eseguire l'addestramento sull'intero train set!! '''

lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

print("\n\nMODELLO\nAccuracy:", lr.score(x_train, y_train))