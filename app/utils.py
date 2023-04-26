import pickle
import pandas as pd

def load_data(csv_path):
    return pd.read_csv(csv_path)

def load_model(pkl_path):
    with open(pkl_path, 'rb') as file:
        model = pickle.load(file)
    return model