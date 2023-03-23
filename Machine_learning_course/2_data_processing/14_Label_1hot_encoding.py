import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

''' le label devono sempre corrispondere a numeri per essere lette dagli algoritmi
		ex. taglia magliette s=1, m=2...
		ex. colore --> assegno variabili boleane a seconda della disponibilità
			rosso disponibile per taglia s e basta: riga 1 = riga rosso --> True False False 
			(ordine colori R B G)'''

shirts = pd.read_csv("data/shirts.csv", index_col=0)
#print(shirts.head())
X = shirts.values #trasformazione in matrice

""" TRASFORMAZIONE TAGLIA IN NUMERO """
# s = 0, m= 1 etc creare dizionario

size_mapping = {"S": 0, "M": 1, "L": 2, "XL": 3}
shirts["taglia"] = shirts["taglia"].map(size_mapping)	# sostiuisce taglie a valori

fmap = np.vectorize(lambda t: size_mapping[t])
X[:,0] = fmap(X[:,0])							# manipolazione su numpy

""" TRASFORMAZIONE COLORI """

shirts = pd.get_dummies(shirts, columns= ["colore"])	# Genera booleane in automatico
print(shirts)

# per numpy usare sklearn.preprocessing

transf = ColumnTransformer([('ohe', OneHotEncoder(), [1])], remainder='passthrough')

X = transf.fit_transform(X)
print(X)
