import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

''' Per decidere quali parametri considerare uso .corr(), ciò che tende a 1 è correlato '''
''' .corr()fornisce la correlazione tra i vari parametriu, seaborn.heatmap per visualizzarlo'''

boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
					 sep='\s+', names=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PRATIO","B","LSTAT","MEDV"])
fig = sns.heatmap(boston.corr(), xticklabels=boston.columns, yticklabels=boston.columns)
fig = plt.show()	# siamo interessati solo al valore come output y della regressione
plt.close()

# RM e LSTAT hanno corr =+1 e -1 rispettivamente
cols = ["RM", "LSTAT", "PRATIO", "TAX", "INDUS", "MEDV"]
fig = sns.heatmap(boston[cols].corr(), xticklabels=boston[cols].columns, yticklabels=boston[cols].columns,
			annot=True, annot_kws={'size':12})
fig = plt.show()
plt.close()

fig = sns.pairplot(boston[cols])	# incrocia tutti i dati e fa vedere la loro distribuzione
fig = plt.show()

''' modello per la regressione usiamo MEDV = f (RM; LSTAT) '''

X = boston[["RM", "LSTAT"]].values
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=0)

ll = LinearRegression()
ll.fit(x_train, y_train)
y_prediction = ll.predict(x_test)

print("MSE: ", mean_squared_error(y_test, y_prediction))
print("R2: ", r2_score(y_test, y_prediction))

''' Modello per la regressione MEDV = f(tutto) '''

X = boston.drop("MEDV", axis = 1).values
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.3, random_state=0)

# tanti dati --> normalizzazione. Creiamo il modello standardizzato sul train set (fit_transform) e
# mentre per il test set usiamo lo stesso modello quindi usiamo solo x_test

ss = StandardScaler()
x_train_std = ss.fit_transform(x_train)
x_test_std = ss.transform(x_test)

ll = LinearRegression()
ll.fit(x_train_std, y_train)
y_prediction = ll.predict(x_test_std)
print("MSE: ", mean_squared_error(y_test, y_prediction))
print("R2: ", r2_score(y_test, y_prediction))

print(zip(boston.columns, ll.coef_))	# per vedere quanto ogni parametro contribuisce alla determinazione dell'output
