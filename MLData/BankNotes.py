from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import pandas as pd
import joblib


class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float


"""
Entrenamiento del modelo:

import pandas as pd
import numpy as np

df = pd.read_csv('BankNote_Authentication.csv')
df #(Se deberían ver los valores)
X = df.iloc[:,:-1]
y = df.iloc[:,-1]
X.head() (Se deberían ver los valores sin la columna class)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=0)
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train) #Debería aparecer el tipo de clasificador

y_pred = classifier.predict(X_test)
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
score #Debería aparecer el porcentaje de éxito del modelo, valores objetivo cercanos a 1

import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

import numpy as np
classifier.predict([[2,3,4,1]]) #Posible alerta debido a que X no tiene nombres de características
"""
