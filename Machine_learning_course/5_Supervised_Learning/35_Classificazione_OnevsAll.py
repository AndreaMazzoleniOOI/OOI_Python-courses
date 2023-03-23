import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, log_loss, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import  OneVsRestClassifier
from sklearn.datasets import load_digits

digits = load_digits()

X = digits.data
Y = digits.target
# le immagini sono già trasformate in pixel in tonalità di grigio
# le classi vanno da 0 a 9 (vettore Y)
# X ha dimensione 1797x64 (1797 immagini ognuna da 8x8 pixel in un unico vettore riga)
# per riconvertire ognuno dei vettori in X in immagine:
for cifra in range(0,10):
	plt.subplot(2,5,cifra+1)
	pic_matrix = X[Y==cifra][0].reshape([8,8])	# Y==cifra è la maschera (seleziona X tale per cui Y = cifra)
												# [0] seleziona solo il primo exempio degli n disponibili e reshape passiamo da vettore a matrice
	plt.imshow(pic_matrix, cmap='gray')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(test_size=0.3, random_state=0)

norm = MinMaxScaler()
x_train = norm.fit_transform(x_train)	# normalizzazione
x_test = norm.transform(x_test)

# LogisticRegression applica automaticamente OneVsAll

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred_prob = lr.predict_proba(x_test)

print("Accuracy=", accuracy_score(y_test, y_pred))
print("Log loss=", log_loss(y_test, y_pred_prob))

cm = confusion_matrix(y_test, y_pred)
fig = plt.figure()
fig = sns.heatmap(cm, cmap='Blues_r', annot=True, linewidth=5, square=True)
plt.xlabel("Prediction")
plt.ylabel("True")
plt.title("LogisticRegression")
plt.show()

''' In alternativa al OvsAll implementato in logisticregression c'è OnevsRestClassifier'''
''' Da gli stessi identici risultati. Per usarlo dichiarare la istanza e fornirgli che regressione vogliamo usare '''

ovr = OneVsRestClassifier(LogisticRegression())
ovr.fit(x_train, y_train)
y_pred = ovr.predict(x_test)
y_pred_prob = ovr.predict_proba(x_test)
print("Accuracy=", accuracy_score(y_test, y_pred))
print("Log loss=", log_loss(y_test, y_pred_prob))

cm = confusion_matrix(y_test, y_pred)
fig = plt.figure()
fig = sns.heatmap(cm, cmap='Blues_r', annot=True, linewidth=5, square=True)
plt.xlabel("Prediction")
plt.ylabel("True")
plt.title("OnevsRestClassifier")
plt.show()


