''' I dati devono essere comparabili come grandezza altrimenti gli algoritmi tendono a
considerare solo i dati più grandi

Normalizzazione xnorm = (xi - xmin)/(xmax-xmin)
Standardizzazione xstd = (xi - media)/dev.std

Nomalizzazione --> NN rchiedono dati tra 0 e 1, immagini vanno normalizzate
Standardizzazione --> Mantengono info su outliers'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

wines = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
					usecols= [0,1,7],
					names = ['classe', 'alcool', 'flav'])
x = wines.drop('classe', axis=1).values

print(wines.head())
print(wines.describe())	# fornisce indici statistici

''' normalizzazione in pandas '''
wines_norm = wines.copy()
features = ["alcool", "flav"]	# colonne da normalizzare
to_norm = wines[features]		# sottovettore per normalizzazione

wines_norm[features] = (to_norm-to_norm.min())/(to_norm.max()-to_norm.min())
print(wines_norm.head())

''' normalizzazione in numpy '''

mms = MinMaxScaler()
x_norm = x.copy()
x_norm = mms.fit_transform(x)
print(x_norm[:5])

''' standardizzazione in pandas '''
wines_std = wines.copy()	# posso riusare i sottovettori di sopra altrimenti sono da ricalcorare
wines_std = (to_norm-to_norm.mean())/to_norm.std()
print(wines_std.head())

''' standardizzazione in numoy '''

std = StandardScaler()
x_std = x.copy()
x_std = std.fit_transform(x_std)
print(x_std[:5])