import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Vehiculos Usados')

hist_button = st.button('Construir un Grafico') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    fig_A = px.histogram(car_data, x="odometer")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_A, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un Grafico')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Grafico De Dispersión')

    fig_B = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_B, use_container_width=True)