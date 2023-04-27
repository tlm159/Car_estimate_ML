import streamlit as st

def display_car_features_form(data):
    """
    Affiche un formulaire pour saisir les caractéristiques de la voiture et retourne les caractéristiques sélectionnées.

    Args:
    data (pd.DataFrame): DataFrame contenant les données de voiture.

    Returns:
    dict: Dictionnaire contenant les caractéristiques sélectionnées.
    """
    st.header("Sélectionnez les caractéristiques de la voiture")
    
    car_features = get_car_features(data)
    
    # Ajout des nouvelles caractéristiques
    car_features['rapport_poids_puissance'] = car_features['poids_vehicule'] / car_features['chevaux']
    car_features['consommation_combinee'] = (car_features['consommation_ville'] + car_features['consommation_autoroute']) / 2
    
    print(car_features)
    
    st.markdown("---")
    
    return car_features


def get_car_features(data):
    """
    Récupère les caractéristiques de la voiture à partir du formulaire et retourne un dictionnaire avec les valeurs sélectionnées.

    Args:
    data (pd.DataFrame): DataFrame contenant les données de voiture.

    Returns:
    dict: Dictionnaire contenant les caractéristiques sélectionnées.
    """
    numerical_columns = ['empattement', 'longueur_voiture', 'largeur_voiture', 'poids_vehicule', 'taille_moteur', 'taux_alésage', 'chevaux', 'consommation_ville', 'consommation_autoroute']
    categorical_columns = ['type_vehicule', 'roues_motrices', 'marque']

    # Récupère les caractéristiques catégorielles de la voiture à partir du formulaire.
    car_features = get_categorical_features(data, categorical_columns)
    # Met à jour le dictionnaire des caractéristiques avec les caractéristiques numériques récupérées à partir du formulaire.
    car_features.update(get_numerical_features(data, numerical_columns))

    return car_features

def get_categorical_features(data, columns):
    """
    Récupère les caractéristiques catégorielles de la voiture à partir du formulaire.

    Args:
    data (pd.DataFrame): DataFrame contenant les données de voiture.
    columns (list): Liste des colonnes catégorielles à récupérer.

    Returns:
    dict: Dictionnaire contenant les caractéristiques catégorielles sélectionnées.
    """
    car_features = {}
    
    # Parcours chaque colonne catégorielle pour obtenir la valeur sélectionnée
    for col in columns:
        unique_values = data[col].unique()
        selected_value = st.sidebar.selectbox(col, unique_values)
        
        # Ajoute la valeur sélectionnée au dictionnaire des caractéristiques
        if selected_value is not None:
            car_features[col] = selected_value
    
    # Récupère le modèle de voiture en fonction de la marque sélectionnée
    selected_marque = car_features.get('marque')
    if selected_marque is not None:
        model_options = data[data['marque'] == selected_marque]['modele'].unique()
        selected_modele = st.sidebar.selectbox("Modèle", model_options)
        
        # Ajoute le modèle sélectionné au dictionnaire des caractéristiques
        if selected_modele is not None:
            car_features['modele'] = selected_modele
    
    return car_features

def get_numerical_features(data, columns):
    """
    Récupère les caractéristiques numériques de la voiture à partir du formulaire.

    Args:
    data (pd.DataFrame): DataFrame contenant les données de voiture.
    columns (list): Liste des colonnes numériques à récupérer.

    Returns:
    dict: Dictionnaire contenant les caractéristiques numériques sélectionnées.
    """
    car_features = {}
    
    # Parcours chaque colonne numérique pour obtenir la valeur sélectionnée
    for col in columns:
        # Récupère la valeur numérique sélectionnée à l'aide d'un slider
        # en définissant les valeurs minimale, maximale et médiane pour le slider
        car_features[col] = st.sidebar.slider(col, float(data[col].min()), float(data[col].max()), float(data[col].median()), 0.1)
    
    return car_features

def display_main_page(car_features_df, predicted_price):
    """
    Affiche les caractéristiques de la voiture et la prédiction du prix.

    Args:
    car_features_df (pd.DataFrame): DataFrame contenant les caractéristiques de la voiture.
    predicted_price (float): Prix prédit pour la voiture.
    """
    st.title("Estimation du prix des voitures")

    st.header("Caractéristiques de la voiture")
    st.write(car_features_df)

    st.header("Prédiction du prix")
    st.write(f'Le prix de la voiture prédit est : {predicted_price[0]:,.2f} dollars')
