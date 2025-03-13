import streamlit as st
from stl import mesh
import plotly.graph_objects as go

# Título de la aplicación
st.title("Visualizador de Modelos 3D para Cáncer de Cérvix")

# Descripción de la aplicación
st.markdown("""
Esta aplicación permite cargar y visualizar modelos 3D en formato STL para personalizar implantes en tratamientos de brachyterapia en cáncer de cérvix.
""")

# Subir archivo STL
uploaded_file = st.file_uploader("Sube tu archivo STL para visualizar", type="stl")

if uploaded_file:
    # Cargar el modelo STL
    stl_mesh = mesh.Mesh.from_file(uploaded_file)

    # Extraer datos del modelo para Plotly
    vertices = stl_mesh.vectors
    x, y, z = vertices[:, :, 0].flatten(), vertices[:, :, 1].flatten(), vertices[:, :, 2].flatten()

    # Crear la figura 3D con Plotly
    fig = go.Figure(data=[go.Mesh3d(
        x=x,
        y=y,
        z=z,
        color='blue',
        opacity=0.50
    )])

    # Ajustar el layout para mejor visualización
    fig.update_layout(scene=dict(aspectmode="data"))

    # Mostrar la figura 3D en la aplicación
    st.plotly_chart(fig)

    # Mensaje adicional
    st.success("Modelo cargado exitosamente. Usa el mouse para explorar el modelo 3D.")

else:
    # Mensaje cuando no se ha subido ningún archivo
    st.warning("Por favor, sube un archivo STL para visualizar el modelo 3D.")

# Información extra para el usuario
st.info("""
### Instrucciones para usar la aplicación:
1. Genera un modelo 3D en FreeCAD o cualquier software CAD compatible.
2. Exporta el modelo como archivo STL.
3. Sube el archivo a esta aplicación para visualizarlo en 3D.

### Funcionalidades:
- Interacción con el modelo 3D directamente desde el navegador.
- Adecuado para personalizar implantes en tratamientos médicos.
""")
