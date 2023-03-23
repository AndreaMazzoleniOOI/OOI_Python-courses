import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
					 sep='\s+', names=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PRATIO","B","LSTAT","MEDV"])

X = boston.drop("MEDV", axis=1).values
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X,Y, train_size=0.7, random_state=0)

polyfeats = PolynomialFeatures(degree=2)
x_train_poly = polyfeats.fit_transform(x_train)
x_test_poly = polyfeats.transform(x_test)

ss = StandardScaler()
x_train_poly = ss.fit_transform(x_train_poly)
x_test_poly = ss.transform(x_test_poly)

ll = LinearRegression()
ll.fit(x_train_poly, y_train)
y_pred_test = ll.predict(x_test_poly)
y_pred_train = ll.predict(x_train_poly)
print("TEST: MSE=", mean_squared_error(y_test, y_pred_test), "R2=", r2_score(y_test, y_pred_test))
print("TRAIN: MSE=", mean_squared_error(y_train, y_pred_train), "R2=", r2_score(y_train, y_pred_train))
# errore train = 4, errore test = 29 ---> overfitting
# r2 train = 0.95 , r2 test = 0.64 --> altro indicatore

