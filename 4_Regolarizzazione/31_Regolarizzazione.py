import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge, Lasso, ElasticNet
import matplotlib.pyplot as plt

''' Qui non andiamo a creare delle regressioni ma applichiamo due modelli ML che hanno regolarizzazioni implementate
 L2 --> Ridge, L1 --> Lasso, L1 e L2 ElasticNet
 IMPORANTE--> sempre standardizzare o normalizzare i dati prima di regolarizzare'''

boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
					 sep='\s+', names=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PRATIO","B","LSTAT","MEDV"])

X = boston.drop("MEDV", axis=1).values
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X,Y, train_size=0.7, random_state=0)

polyf = PolynomialFeatures(degree=2)
x_train_poly = polyf.fit_transform(x_train)
x_test_poly = polyf.transform(x_test)

ss = StandardScaler()
x_train_poly = ss.fit_transform(x_train_poly)
x_test_poly = ss.transform(x_test_poly)

''' Regolarizzazione L2 (Ridge) '''

alphas = [0.0001, 0.001, 0.01, 0.1, 1., 10.]	# iperparametro Ridge
f, (ax1, ax2) = plt.subplots(1, 2)
for alpha in alphas:

	model = Ridge(alpha=alpha)
	model.fit(x_train_poly, y_train)

	y_pred_test = model.predict(x_test_poly)
	y_pred_train = model.predict(x_train_poly)

	ax1.scatter(alpha, mean_squared_error(y_test, y_pred_test), c='blue')
	ax1.scatter(alpha, mean_squared_error(y_train, y_pred_train), c='green')
	ax1.set_xscale('log')
	ax2.scatter(alpha, r2_score(y_test, y_pred_test), c='blue')
	ax2.scatter(alpha, r2_score(y_train, y_pred_train), c='green')
	ax2.set_xscale('log')

ax1.scatter(None, None, c='blue', label='Test')
ax1.scatter(None, None, c='green', label='Train')
ax2.scatter(None, None, c='blue', label='Test')
ax2.scatter(None, None, c='green', label='Train')
ax1.grid()
ax1.legend()
ax2.grid()
ax2.legend()
ax1.title.set_text("MSE con Ridge")
ax2.title.set_text("R2 con Ridge")
fig1 = plt.show()
# il miglior risultato è dato da alpha = 10

''' Regolarizzazione L1 (Lasso) '''

alphas = [0.0001, 0.001, 0.01, 0.1, 1., 10.]	# iperparametro Ridge
f, (ax1, ax2) = plt.subplots(1, 2)
for alpha in alphas:

	model = Lasso(alpha=alpha)
	model.fit(x_train_poly, y_train)

	y_pred_test = model.predict(x_test_poly)
	y_pred_train = model.predict(x_train_poly)

	ax1.scatter(alpha, mean_squared_error(y_test, y_pred_test), c='blue')
	ax1.scatter(alpha, mean_squared_error(y_train, y_pred_train), c='green')
	ax1.set_xscale('log')
	ax2.scatter(alpha, r2_score(y_test, y_pred_test), c='blue')
	ax2.scatter(alpha, r2_score(y_train, y_pred_train), c='green')
	ax2.set_xscale('log')

ax1.scatter(None, None, c='blue', label='Test')
ax1.scatter(None, None, c='green', label='Train')
ax2.scatter(None, None, c='blue', label='Test')
ax2.scatter(None, None, c='green', label='Train')
ax1.grid()
ax1.legend()
ax2.grid()
ax2.legend()
ax1.title.set_text("MSE con Lasso")
ax2.title.set_text("R2 con Lasso")
fig1 = plt.show()	# miglior risultato per alpha = 0.1 ma R2 è più basso che per il caso precedente in cui usa L2

''' Regolarizzazione L1-L2 insieme (Elastic_Net) '''

alphas = [0.0001, 0.001, 0.01, 0.1, 1., 10.]	# iperparametro Ridge
f, (ax1, ax2) = plt.subplots(1, 2)
for alpha in alphas:

	model = ElasticNet(alpha=alpha, l1_ratio=0.5) # l1_ratio dice a quale tra l1 e l2 dare piu importanza, 0.5 uguale
	model.fit(x_train_poly, y_train)

	y_pred_test = model.predict(x_test_poly)
	y_pred_train = model.predict(x_train_poly)

	ax1.scatter(alpha, mean_squared_error(y_test, y_pred_test), c='blue')
	ax1.scatter(alpha, mean_squared_error(y_train, y_pred_train), c='green')
	ax1.set_xscale('log')
	ax2.scatter(alpha, r2_score(y_test, y_pred_test), c='blue')
	ax2.scatter(alpha, r2_score(y_train, y_pred_train), c='green')
	ax2.set_xscale('log')

ax1.scatter(None, None, c='blue', label='Test')
ax1.scatter(None, None, c='green', label='Train')
ax2.scatter(None, None, c='blue', label='Test')
ax2.scatter(None, None, c='green', label='Train')
ax1.grid()
ax1.legend()
ax2.grid()
ax2.legend()
ax1.title.set_text("MSE con ElasticNet")
ax2.title.set_text("R2 con ElasticNet")
fig1 = plt.show()	# miglior risultato per alpha = 0.01 con miglior R2 e MSE che negli altri casi


