import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

iris_nan = pd.read_csv("data/iris_nan.csv")		# il dataframe contiene alcuni NaN che vanno gestiti
print(iris_nan.head())
# creo vettori np
Y = iris_nan["class"].values
X = iris_nan.drop("class", axis=1).values

''' rimuovere righe o colonne che contengono NaN (da evitare) '''

iris_drop = iris_nan.dropna()	# rimuove righe
iris_drop = iris_nan.dropna(axis=1)	# rimuove colonne

''' imputazione dati mancanti == sostituzione con una stima '''

replace1 = iris_nan.dropna().mean() #media
replace2 = iris_nan.dropna().median()	#mediana
replace3 = iris_nan.dropna().mode().iloc[0]	# moda: restituisce un datframe oridnato per frequenza --> seleziona solo primo elemento
iris_imp = iris_nan.fillna(replace1) # ho sostituito la media, vale anche per gli altri
print(iris_imp.head())

''' imputazione su numpy '''

imp = SimpleImputer(missing_values=np.nan, strategy='mean')	# most_frequent, median etc.
X_imp = imp.fit_transform(X)
n_nan = np.count_nonzero(np.isnan(X))
print(n_nan)
n_nan = np.count_nonzero(np.isnan(X_imp))
print(n_nan)
print(X_imp)