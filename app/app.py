import streamlit as st
import pandas as pd
from utils import load_model, load_data
from components import get_car_features, show_car_features, display_prediction

data = load_data('../data/voiture_model.csv')
model = load_model('../models/random_forest.pkl')

car_features = get_car_features(data)
car_features_df = pd.DataFrame(car_features, index=[0])

show_car_features(car_features_df)

predicted_price = display_prediction(model, car_features_df)