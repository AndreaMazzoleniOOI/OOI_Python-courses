''' Training dataset != test dataset in genere 70-30
tanti dati nel training è meglio. con 10e6 dati posso usare anche 98-2'''

import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


boston = load_boston()	# bulid-in function per richiamare questo dataset

''' sèlitting su numpy '''
X = boston.data		# 506 samples
Y = boston.target

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
''' splitting su pandas'''

boston_df = pd.DataFrame(data= np.c_[boston['data'], boston['target']], columns= np.append(boston['feature_names'], 'TARGET'))
# importare boston in un dataframe
print(boston_df.head())

boston_test_df = boston_df.sample(frac=0.3)
boston_train_df = boston_df.drop(boston_test_df.index) 	# drop tutte le righe con indici uguali ai test

