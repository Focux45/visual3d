import streamlit as st
from stl_viewer import stl_viewer

# Título
st.title("Visualización del Modelo 3D")

# Subir archivo STL
st.header("Sube tu archivo STL")
uploaded_file = st.file_uploader("Selecciona un archivo STL para visualizar", type="stl")

# Mostrar el modelo 3D
if uploaded_file:
    stl_viewer(uploaded_file)
