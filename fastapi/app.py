from fastapi import FastAPI
from schemas import CarFeatures
import pickle
import pandas as pd

app = FastAPI()

def load_model(filepath):
    with open(filepath, 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model('../models/random_forest.pkl')

@app.post("/predict")
async def predict_car_price(car_features: CarFeatures):
    car_features_df = pd.DataFrame([car_features.dict()])
    predicted_price = model.predict(car_features_df)
    return {"predicted_price": predicted_price[0]}
