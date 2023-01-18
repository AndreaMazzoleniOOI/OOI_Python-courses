import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, accuracy_score
from sklearn.ensemble import RandomForestClassifier

titanic = pd.read_csv("http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")

# 7 proprietà pi target Survived, 887 esempi
# survived, Pclass Name (string), Sex(string), Age, Siblings/Spouse Aboard, Parents/Children Aboard,Fare

titanic = titanic.drop("Name", axis = 1)
titanic = pd.get_dummies(titanic)

X = titanic.drop("Survived", axis=1).values
Y = titanic["Survived"].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# il modello ha overfitting, quindi limitiamo a 8 la profondità e aumentiamo a 30 alberi
forest = RandomForestClassifier(random_state=False, max_depth=8, n_estimators=30)
forest.fit(x_train, y_train)
y_pred = forest.predict(x_test)
print("TEST \nAccuracy=", accuracy_score(y_test, y_pred),"\nLog loss=", log_loss(y_test, y_pred))
y_pred = forest.predict(x_train)
print("TRAIN \nAccuracy=", accuracy_score(y_train, y_pred),"\nLog loss=", log_loss(y_train, y_pred))
