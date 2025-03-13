import streamlit as st
from stl import mesh
import plotly.graph_objects as go

# Título de la aplicación
st.title("Visualizador de Modelos 3D para Cáncer de Cérvix")

# Subir archivo STL
uploaded_file = st.file_uploader("Sube tu archivo STL para visualizar", type="stl")

if uploaded_file:
    # Cargar el modelo STL
    stl_mesh = mesh.Mesh.from_file(uploaded_file)

    # Extraer datos para Plotly
    vertices = stl_mesh.vectors
    x, y, z = vertices[:, :, 0].flatten(), vertices[:, :, 1].flatten(), vertices[:, :, 2].flatten()

    # Crear la figura 3D
    fig = go.Figure(data=[go.Mesh3d(
        x=x,
        y=y,
        z=z,
        color='blue',
        opacity=0.50
    )])

    # Ajustar el layout para mejor visualización
    fig.update_layout(scene=dict(aspectmode="data"))

    # Mostrar en Streamlit
    st.plotly_chart(fig)

# Información adicional
st.info("Sube un archivo STL generado para visualizar su modelo 3D.")
