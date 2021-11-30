import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle

from MLData import BankNote

app = FastAPI()
pickle_in = open("MLData/classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.post("/predict/")
def predict_banknote(data: BankNote):
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] > 0.5:
        prediction = "Billete Falso"
    else:
        prediction = "Billete real"
    return {"Prediction": prediction}


if __name__ == "__main__":
    uvicorn.run("MachineLearningAPI:app")
