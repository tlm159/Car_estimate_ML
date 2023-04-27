import streamlit as st
import pandas as pd
from utils import load_model, load_data
from components import display_car_features_form, display_main_page

# Charger les données et le modèle
data = load_data('../data/voiture_model.csv')
model = load_model('../models/random_forest.pkl')

def main():
    """
    Fonction principale pour l'application Streamlit.
    Affiche un formulaire pour sélectionner les caractéristiques de la voiture et prédit le prix en fonction des caractéristiques sélectionnées.
    """
    # Afficher le formulaire pour sélectionner les caractéristiques de la voiture
    car_features = display_car_features_form(data)
    
    # Créer un DataFrame avec les caractéristiques de la voiture sélectionnées
    car_features_df = pd.DataFrame(car_features, index=[0])

    # Prédire le prix de la voiture en fonction des caractéristiques sélectionnées
    predicted_price = model.predict(car_features_df)

    # Afficher les caractéristiques de la voiture et la prédiction du prix
    display_main_page(car_features_df, predicted_price)

if __name__ == "__main__":
    main()