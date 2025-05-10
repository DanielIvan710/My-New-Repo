import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title(" Análisis de vehículos usados")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir histograma
hist_button = st.button(' Mostrar histograma de kilometraje')

if hist_button:
    # Mensaje informativo
    st.info("Generando histograma interactivo de kilometraje (odometer)...")

    # Crear histograma personalizado
    fig = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del Kilometraje de Vehículos Usados",
        labels={"odometer": "Kilometraje (millas)"},
        color_discrete_sequence=["darkcyan"]
    )

    # Ajustar estilo del gráfico
    fig.update_layout(
        title_font_size=20,
        xaxis_title="Kilometraje en millas",
        yaxis_title="Cantidad de vehículos",
        bargap=0.1,
        template="plotly_white"
    )

    # Mostrar gráfico en la app
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar scatterplot
scatter_button = st.button(' Mostrar scatterplot de kilometraje vs precio')

if scatter_button:
    # Mensaje informativo
    st.info("Generando gráfico de dispersión de kilometraje vs precio...")

    # Crear scatterplot
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre Kilometraje y Precio",
        labels={"odometer": "Kilometraje (millas)", "price": "Precio (USD)"},
        color_discrete_sequence=["indianred"]
    )

    # Ajustar estilo del gráfico
    fig_scatter.update_layout(
        title_font_size=20,
        xaxis_title="Kilometraje en millas",
        yaxis_title="Precio en USD",
        template="plotly_white"
    )

    # Mostrar gráfico en la app
    st.plotly_chart(fig_scatter, use_container_width=True)
