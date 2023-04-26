import streamlit as st

def get_car_features(data):
    numerical_columns = ['empattement', 'longueur_voiture', 'largeur_voiture', 'poids_vehicule', 'taille_moteur', 'taux_alésage', 'chevaux', 'consommation_ville', 'consommation_autoroute']
    categorical_columns = ['etat_de_route', 'turbo', 'type_vehicule', 'roues_motrices', 'emplacement_moteur', 'marque']

    car_features = {}
    for col in categorical_columns:
        unique_values = data[col].unique()
        selected_value = st.sidebar.selectbox(col, unique_values)
        if selected_value is not None:
            car_features[col] = selected_value

    selected_marque = car_features.get('marque')
    if selected_marque is not None:
        model_options = data[data['marque'] == selected_marque]['modele'].unique()
        selected_modele = st.sidebar.selectbox("Modèle", model_options)
        if selected_modele is not None:
            car_features['modele'] = selected_modele

    for col in numerical_columns:
        car_features[col] = st.sidebar.slider(col, float(data[col].min()), float(data[col].max()), float(data[col].median()), 0.1)

    return car_features

def show_car_features(car_features_df):
    st.write(car_features_df)

def display_prediction(model, car_features_df):
    predicted_price = model.predict(car_features_df)
    st.write('Le prix de la voiture prédit est :', predicted_price, 'dollars')
    return predicted_price