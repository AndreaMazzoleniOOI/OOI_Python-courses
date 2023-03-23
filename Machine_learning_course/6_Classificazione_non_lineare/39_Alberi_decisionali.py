import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz

''' obietticvo creare albero decisionale per capire se una persona sul titanic è morta o no a seconda dei suoi dati'''
''' alberi decisionali non necessitano di normalizzazione o standardizzazione'''

titanic = pd.read_csv("http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")

# 7 proprietà pi target Survived, 887 esempi
# survived, Pclass Name (string), Sex(string), Age, Siblings/Spouse Aboard, Parents/Children Aboard,Fare

titanic = titanic.drop("Name", axis = 1)
titanic = pd.get_dummies(titanic)

X = titanic.drop("Survived", axis=1).values
Y = titanic["Survived"].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

tree = DecisionTreeClassifier(criterion="gini")
tree.fit(x_train, y_train)
y_pred = tree.predict(x_test)
print("TEST \nAccuracy=", accuracy_score(y_test, y_pred),"\nLog loss=", log_loss(y_test, y_pred))
y_pred = tree.predict(x_train)
print("TRAIN \nAccuracy=", accuracy_score(y_train, y_pred),"\nLog loss=", log_loss(y_train, y_pred))

'''errore train molto basso rispetto a test --> overfitting = albero troppo complesso
 si può limitare la profondità con max_depth'''

tree = DecisionTreeClassifier(criterion="gini", max_depth=6)
tree.fit(x_train, y_train)
y_pred = tree.predict(x_test)
print("\nTEST \nAccuracy=", accuracy_score(y_test, y_pred),"\nLog loss=", log_loss(y_test, y_pred))
y_pred = tree.predict(x_train)
print("TRAIN \nAccuracy=", accuracy_score(y_train, y_pred),"\nLog loss=", log_loss(y_train, y_pred))

''' visualizzazione albero '''

dotfile = open("tree.dot", 'w')
export_graphviz(tree, out_file = dotfile, feature_names=titanic.columns.drop("Survived"))
dotfile.close()
