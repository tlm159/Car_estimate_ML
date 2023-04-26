import streamlit as st
import pickle
import pandas as pd

data = pd.read_csv('../data/voiture_model.csv')

# Charger le modèle sauvegardé avec pickle
with open('../models/random_forest.pkl', 'rb') as file:
    model = pickle.load(file)

# Identifiez les colonnes numériques et catégorielles
numerical_columns = ['empattement', 'longueur_voiture', 'largeur_voiture', 'poids_vehicule', 'taille_moteur', 'taux_alésage', 'chevaux', 'consommation_ville', 'consommation_autoroute']
categorical_columns = ['etat_de_route', 'turbo', 'type_vehicule', 'roues_motrices', 'emplacement_moteur']

# Définir les caractéristiques de la voiture
car_features = {}
for col in numerical_columns:
    car_features[col] = st.sidebar.slider(col, float(data[col].min()), float(data[col].max()), float(data[col].median()), 0.1)

selected_marque = st.sidebar.selectbox("Marque", data['marque'].unique())

# Filtrer les modèles en fonction de la marque sélectionnée
model_options = data[data['marque'] == selected_marque]['modele'].unique()
selected_modele = st.sidebar.selectbox("Modèle", model_options)

car_features['marque'] = selected_marque
car_features['modele'] = selected_modele

for col in numerical_columns:
    widget_key = col + '_slider'
    car_features[col] = st.sidebar.slider(widget_key, float(data[col].min()), float(data[col].max()), float(data[col].median()), 0.1)

for col in categorical_columns:
    unique_values = data[col].unique()
    selected_value = st.sidebar.selectbox(col, unique_values)
    if selected_value is not None:
        car_features[col] = selected_value

# Créer un DataFrame avec les caractéristiques de la voiture
car_features_df = pd.DataFrame(car_features, index=[0])

# Réorganiser les colonnes dans l'ordre souhaité
car_features_df = car_features_df.reindex(columns=['etat_de_route', 'turbo', 'type_vehicule', 'roues_motrices', 'emplacement_moteur', 'marque', 'modele', 'empattement', 'longueur_voiture', 'largeur_voiture', 'poids_vehicule', 'taille_moteur', 'taux_alésage', 'chevaux', 'consommation_ville', 'consommation_autoroute'])

# Afficher les caractéristiques de la voiture sélectionnée
st.write(car_features_df)

# Faire une prédiction avec le modèle
predicted_price = model.predict(car_features_df)[0]
predicted_price = round(predicted_price, 2)

# Afficher le résultat de la prédiction
st.write('Le prix de la voiture prédit est :', predicted_price, 'dollars')
