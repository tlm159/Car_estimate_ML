from fastapi import FastAPI
from schemas import CarFeatures
import pickle
import pandas as pd

app = FastAPI()

def load_model(filepath):
    """
    Fonction pour charger le modèle à partir d'un fichier pickle.

    Args:
        filepath (str): Le chemin du fichier pickle contenant le modèle.

    Returns:
        Le modèle chargé.
    """
    with open(filepath, 'rb') as file:
        model = pickle.load(file)
    return model

# Chargement du modèle
model = load_model('../models/random_forest.pkl')

@app.post("/predict")
async def predict_car_price(car_features: CarFeatures):
    """
    Fonction pour prédire le prix d'une voiture en utilisant le modèle chargé.

    Args:
        car_features (CarFeatures): Les caractéristiques de la voiture à prédire.

    Returns:
        Un dictionnaire contenant la prédiction du prix de la voiture.
    """
    car_features_dict = car_features.dict()
    
    # Ajout des nouvelles caractéristiques
    car_features_dict['rapport_poids_puissance'] = car_features_dict['poids_vehicule'] / car_features_dict['chevaux']
    car_features_dict['consommation_combinee'] = (car_features_dict['consommation_ville'] + car_features_dict['consommation_autoroute']) / 2
    car_features_df = pd.DataFrame([car_features_dict])
    predicted_price = model.predict(car_features_df)
    
    return {"predicted_price": predicted_price[0]}