import streamlit as st
import pandas as pd

data= pd.read_csv('historico_resultados_pruebas_saber_11.csv')
data
st.header("filtro 1")
st.write("Mostrar puntajes de institucion  santa teresa")
filtro1 = data[(data['establecimiento'] =='inst educ santa teresa')] 
st.dataframe(filtro1)

st.header("Filtro 2")
st.write ("Mostrar todos los puntajes de matematicas")
filtro2 = data["puntaje_matematicas"]
st.dataframe(filtro2)

st.header("filtro3")
st.write("Mostrar todos los puntajes de lenguaje de medellin")
filtro3= data["punt_lectura_med"]
st.dataframe(filtro3)

st.header("filtro4")
st.write("Mostrar prestacion de servicio tipo oficial")
filtro4 = data[(data['prestacion_servicio'] =='oficial')] 
st.dataframe(filtro4)

st.header("Filtro5")
st.write("Resultados con valores menores a 50000:")
filtro_resultado = data[data['punt_naturales_med'] < 53.9999]
st.write(filtro_resultado)


