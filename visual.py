import streamlit as st
from stl import mesh
import plotly.graph_objects as go

# Título de la aplicación
st.title("Planificador 3D para Braquiterapia en Cáncer de Cérvix")

# Descripción de la aplicación
st.markdown("""
Esta herramienta permite visualizar y personalizar modelos 3D utilizados en el tratamiento de braquiterapia para el cáncer de cuello uterino. 
Podrás analizar la ubicación del tumor, ajustar la posición de las agujas y definir su número para optimizar el tratamiento.
""")

# Subir archivo STL
uploaded_file = st.file_uploader("Sube el modelo 3D del tumor en formato STL", type="stl")

if uploaded_file:
    # Cargar el modelo STL
    stl_mesh = mesh.Mesh.from_file(uploaded_file)

    # Extraer datos del modelo para Plotly
    vertices = stl_mesh.vectors
    x, y, z = vertices[:, :, 0].flatten(), vertices[:, :, 1].flatten(), vertices[:, :, 2].flatten()

    # Crear la figura 3D del tumor con Plotly
    fig = go.Figure(data=[go.Mesh3d(
        x=x,
        y=y,
        z=z,
        color='red',
        opacity=0.6,
        name="Modelo Tumoral"
    )])

    # Configuración de la visualización de las agujas
    st.markdown("### Configuración de las Agujas de Braquiterapia")
    num_agujas = st.slider("Número de agujas a utilizar:", min_value=1, max_value=10, value=3)
    posiciones = []
    for i in range(num_agujas):
        st.markdown(f"**Posición de la aguja {i+1}:**")
        x_pos = st.number_input(f"Coordenada X de la aguja {i+1}:", value=0.0, step=0.1)
        y_pos = st.number_input(f"Coordenada Y de la aguja {i+1}:", value=0.0, step=0.1)
        z_pos = st.number_input(f"Coordenada Z de la aguja {i+1}:", value=0.0, step=0.1)
        posiciones.append((x_pos, y_pos, z_pos))
        fig.add_trace(go.Scatter3d(
            x=[x_pos], y=[y_pos], z=[z_pos],
            mode='markers',
            marker=dict(size=5, color='blue'),
            name=f"Aguja {i+1}"
        ))

    # Ajustar el layout para mejor visualización
    fig.update_layout(
        scene=dict(
            xaxis_title="Coordenada X",
            yaxis_title="Coordenada Y",
            zaxis_title="Coordenada Z",
            aspectmode="data"
        ),
        title="Modelo 3D del Tumor y Agujas de Braquiterapia"
    )

    # Mostrar la figura 3D en la aplicación
    st.plotly_chart(fig)

    # Mensaje adicional
    st.success(f"Modelo y configuración de {num_agujas} agujas cargados exitosamente. Usa el mouse para explorar el modelo 3D.")

else:
    # Mensaje cuando no se ha subido ningún archivo
    st.warning("Por favor, sube un archivo STL que represente el modelo tumoral.")

# Información extra para el usuario
st.info("""
### Instrucciones para usar la aplicación:
1. Genera un modelo 3D del tumor utilizando imágenes médicas o software compatible (ej. FreeCAD).
2. Exporta el modelo como archivo STL.
3. Sube el archivo a esta aplicación para visualizar el modelo y configurar las agujas.

### Funcionalidades:
- Interacción con el modelo tumoral en 3D directamente desde el navegador.
- Configuración personalizada de las agujas de braquiterapia.
- Visualización precisa para planificar procedimientos en cáncer de cuello uterino.
""")
