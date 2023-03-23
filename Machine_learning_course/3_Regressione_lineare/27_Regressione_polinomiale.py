import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
					 sep='\s+', names=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PRATIO","B","LSTAT","MEDV"])

cols = ["RM", "LSTAT", "DIS", "RAD", "MEDV"]	# da valutazioni lez 25 sono quelle più influenti, LSTAT ha relazione non lineare

""" REGRESSIONE POLINOMIALE SINGOLA PROPRIETA' """
X = boston[["LSTAT"]].values	# vettore colonna
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

for grado in range(1,11):
	polyfeats = PolynomialFeatures(degree=grado)	# crea proprietà per polinomiale
	x_train_poly = polyfeats.fit_transform(x_train)
	x_test_poly = polyfeats.transform(x_test)
	''' questa procedura crea una matrice di grado+1 colonne ognuna contenente il valore dell'elemento di X elevato rispettivamente a 0, 1, 2
	ex. grado = 2 x_test = [1 2 3] --> x_test_poly= [[1 1 1], [1 2 4], [1 3 9]]'''
	# con il ciclo for stiamo andando semplicemente a confrontare i risultati, in reltà sta a noi
	# scegliere il grado del polinomio

	ll = LinearRegression()
	ll.fit(x_train_poly, y_train)
	y_pred = ll.predict(x_test_poly)

	print("Degree", grado,
		  ": MSE=", mean_squared_error(y_test, y_pred),
		  "R2=", r2_score(y_test, y_pred))
# migliora fino a grado 6, poi peggiora ( = overfitting)
print("\n")

""" REGRESSIONE POLINOMIALE TUTTE PROPRIETA' """
X = boston.drop("MEDV", axis=1).values	# vettore colonna
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

for grado in range(1,5):
	polyfeats = PolynomialFeatures(degree=grado)	# crea proprietà per polinomiale
	x_train_poly = polyfeats.fit_transform(x_train)
	x_test_poly = polyfeats.transform(x_test)
	''' questa procedura crea una matrice di grado+1 colonne ognuna contenente il valore dell'elemento di X elevato rispettivamente a 0, 1, 2
	ex. grado = 2 x_test = [1 2 3] --> x_test_poly= [[1 1 1], [1 2 4], [1 3 9]]'''
	# con il ciclo for stiamo andando semplicemente a confrontare i risultati, in reltà sta a noi
	# scegliere il grado del polinomio

	ll = LinearRegression()
	ll.fit(x_train_poly, y_train)
	y_pred = ll.predict(x_test_poly)

	print("Degree", grado,
		  ": MSE=", mean_squared_error(y_test, y_pred),
		  "R2=", r2_score(y_test, y_pred))
# va bene fino a grado 2 poi peggiora tantissimo perchè i parametri sono troppi
# per descrivere il problema --> R2 va a -inf