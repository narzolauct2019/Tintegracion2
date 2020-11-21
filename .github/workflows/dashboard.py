import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt


st.title('Dashboard: contagiados de COVID-19 en Chile')



st.text("informacion del programa")


st.title("Nombre de region")
st.subheader("Grafica de casos COVID-19 de la region" + " **region**")
st.text("Aqui se mostrara la descripcion de la situacion actual de la region")
st.markdown("Aqui se mostrará el grafico desde el filtrado de archivos csv")




st.sidebar.title("Seleccione una region de Chile")
select = st.sidebar.selectbox('Regiones de Chile:', ['I Región de Tarapacá','II Región de Antofagasta','III Región de Atacama','IV Región de Coquimbo','V Región de Valparaíso',
'VI Región del Libertador General Bernardo O’Higgins','VII Región del Maule','VIII Región del Biobío','IX Región de La Araucanía',
'X Región de Los Lagos','XI Región Aysén del General Carlos Ibáñez del Campo','XII Región de Magallanes y Antártica Chilena',
'Región Metropolitana de Santiago','XIV Región de Los Ríos','XV Región de Arica y Parinacota','XVI Región de Ñuble',
    ], key='1')






x = [1, 2, 3, 4, 5, 6, 8]
y = [6, 7, 2, 4, 5]

p = figure(
title='Alza de contagios COVID-19',
x_axis_label='Dias',
y_axis_label='Contagiados')

p.line(x, y, legend='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
