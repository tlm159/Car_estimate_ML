import pandas as pd
import pickle

def load_data(filepath):
    """
    Charge les données à partir d'un fichier CSV et retourne un DataFrame Pandas.

    Args:
    filepath (str): Chemin du fichier CSV.

    Returns:
    pd.DataFrame: DataFrame Pandas contenant les données du fichier CSV.
    """
    return pd.read_csv(filepath)

def load_model(filepath):
    """
    Charge un modèle à partir d'un fichier pickle et retourne l'objet modèle.

    Args:
    filepath (str): Chemin du fichier pickle.

    Returns:
    model: Objet modèle chargé à partir du fichier pickle.
    """
    with open(filepath, 'rb') as file:
        model = pickle.load(file)
    return model