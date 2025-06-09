from utils import db_connect
engine = db_connect()

# your code here
import streamlit as st
import numpy as np
import pickle

# Cargar modelo
with open('modelo_iris.pkl', 'rb') as f:
    model = pickle.load(f)

# Título de la app
st.title("🌷 Predicción de tipo de flor Iris")

# Inputs del usuario
sepal_length = st.number_input('Sepal length (cm)', min_value=0.0, step=0.1, format="%.2f")
sepal_width = st.number_input('Sepal width (cm)', min_value=0.0, step=0.1, format="%.2f")
petal_length = st.number_input('Petal length (cm)', min_value=0.0, step=0.1, format="%.2f")
petal_width = st.number_input('Petal width (cm)', min_value=0.0, step=0.1, format="%.2f")

# Botón para predecir
if st.button('Predecir'):
    # Preparar datos
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    labels = ["Setosa", "Versicolor", "Virginica"]
    st.success(f'La flor es: {labels[prediction[0]]}')