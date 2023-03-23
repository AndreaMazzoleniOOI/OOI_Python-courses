import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


boston = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
					 sep='\s+', usecols=[5,13], names=["RM", "MEDV"])	# \s+ perchè i dati sono suddivisi da un numero irregolare di spazi
X = boston.drop("MEDV", axis=1).values
Y = boston["MEDV"].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

ll = LinearRegression()
ll.fit(x_train, y_train)
y_pred = ll.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
print("MSE: ", mse)
r2 = r2_score(y_test, y_pred)
print("R2: ", r2 )

w, b = ll.coef_[0], ll.intercept_ # se dovessero servire i coefficienti

plt.scatter(x_train, y_train, c="green", edgecolors='white', label="Train dataset")
plt.scatter(x_test, y_test, c='blue',edgecolors='white', label="Test dataset")
plt.xlabel("N medio stanze [RM]")
plt.ylabel("Prezzo in 1000$ [MEDV]")
plt.legend(loc="upper left")

plt.plot(x_test, y_pred, color="red", linewidth=3)
plt.show()

''' se ho errori troppo alti vado a fare regressione multipla '''