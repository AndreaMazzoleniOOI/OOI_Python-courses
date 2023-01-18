import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
iris = pd.read_csv("data\iris.csv")


X = iris["species"]		# crea una series con la colonna species
Y = iris[["sepal_length", "sepal_width"]]	# richiama solo due colonne di interesse
Z = iris.drop("species", axis=1)	# exlude la colonna species. axis = 1 per riga, axis = 0 per colonna

print(X)
print(Y)
print(Z)

""" SLICING """

iris_sampled = iris.copy()
iris_sampled = iris.sample(frac=1)	# random ordine righe
print(iris_sampled.iloc[3])		# iloc lavora sugli indici, stampa il quarto elemento
print(iris_sampled.loc[100])	# lavora sulla label del dataframe
print(iris_sampled.loc[3, "species"])	# riga 4 elemento species
print(iris_sampled.iloc[3, 4])			# con iloc indice colonna integer

""" STATISTICS and MASKS """

print(iris['sepal_length'].max())
print(iris["sepal_length"].var())		# varianza colonna sepal_length
length_petal_mask = iris["petal_length"] > iris["petal_length"].mean()	#	crea un vettore True False dove la condizione è verificata
iris_long = iris[length_petal_mask]		# df con solo quelli che rispettano la condizione di sopra
print(iris_long.head())

iris_copy = iris.copy()
iris_copy[iris_copy["species"] == "setosa"] = "undefined"	# sostituisce tutti i "setosa" con "undifined

X = iris.drop("species", axis = 1)
x_norm = (X-X.min())/(X.max()-X.min())	# normalizzazione dataframe
print(x_norm.head())

grouped_species = iris.groupby("species")	# raggruppa tutti i dataframe con la setssa label "species"
print(grouped_species.mean().head())

print(iris.sort_values("petal_length").head())		# ordina in ordine crescente

print(iris.apply(np.count_nonzero, axis=0))	# .apply permette di usare funzioni di librerie diverse sul dataframe

X = iris.drop("species", axis=1)
X = X.applymap(lambda val : int(round(val, 0)))	# applymap agisce valore per valore, lamda è una funzione usa e getta che viene definita per essere utilizzata solo in questa linea di codice
												# arrotonda a successivo

""" NaN detection """
iris_nan = iris.copy()
samples = np.random.randint(iris.shape[0], size=10)	# vettore random con idici in cui inserire i NaN
iris_nan.loc[samples, 'petal_length'] = None 		# creare alcuni vettori Nan, nel documento originale non ci sono
print(iris_nan['petal_length'].isnull().sum())						# conta numero di NaN nel dataframe

mean = iris_nan['petal_length'].mean()
iris_nan['petal_length'].fillna(mean, inplace=True)		# sostituisce i NaN con il valore medio della serie

print(iris_nan['petal_length'].isnull().sum())						# conta numero di NaN nel dataframe

""" PLOT WITH DF """

plt.scatter(iris['sepal_length'], iris['sepal_width'])
plt.show()