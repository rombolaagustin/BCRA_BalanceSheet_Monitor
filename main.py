# BCRA Balance Sheet Monitor


# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from tools.mapping import sheet_names
from tools.mapping import cols_names
from tools.mapping import list_aggregates, list_type_graph
from tools.functions import download_file
from tools.functions import preprocessing_data
from tools.functions import build_nominal_data

# Objects
from tools.objects import dataObj

# Control Variables
hours_to_download = 3
url = 'https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/series.xlsm'
filename = 'series.xlsm'

# Download file from BCRA website 
download_file(url, filename, hours_to_download)

# Preprocessing data
data = preprocessing_data(filename)

# Nominal data
nominal_data = build_nominal_data(data)


# Nominal Object
data = dataObj(nominal_data)
data.make_var_yearly()

# Main 
st.title(':flag-ar: BCRA Balance Sheet Monitor :flag-ar:')

st.subheader('Agregados Monetarios')

st.dataframe(data.nominal)

st.area_chart(data.yearly['Base Monetaria'])

''' PLOTS, TODO NEXT WEEK

aggregate_plot = st.selectbox('Selecciona un agregado monetario', list_aggregates, 0)
type_plot = st.selectbox('Tipo de gráfico', list_type_graph, 0)

if type_plot == 'Escala Logaritmica':
    log_type = True
else:
    log_type = False

if aggregate_plot == 'Base Monetaria':
    fig = px.line(
        nominal_data,
        x = 'date',
        y = 'base monetaria',
        title='Base Monetaria',
        log_y=log_type,
    )
    st.write(fig)
# elif aggregate_plot == 'Reservas':
#     fig = px.line(
#         data['RESERVAS'],
#         x = 'date',
#         y = 'total',
#         title='RESERVAS (Expresas en USD)',
#         log_y=log_type,
#     )
#     st.write(fig)
# elif aggregate_plot == 'Tipo de Cambio':
#     fig = px.line(
#         data['RESERVAS'],
#         x = 'date',
#         y = 'tipo de cambio',
#         title='Tipo de Cambio Oficial (Expresado como: pesos equivalentes a un USD)',
#         log_y=log_type,
#     )
#     st.write(fig)
elif aggregate_plot == 'M2':
    fig = px.line(
        nominal_data,
        x = 'date',
        y = 'M2',
        title='M2 = Billetes en poder del público + Cajas de Ahorro + Cuentas Corrientes',
        log_y=log_type,
    )
    st.write(fig)
else:
    st.write(':lightning: Agregado monetario aún no disponible!')



# # Create a function to generate the plot
# def generate_plot(x_axis, y_axis, plot_type):
#     if x_axis == 'Linear':
#         x = np.linspace(0, 10, 100)
#     elif x_axis == 'Random':
#         x = np.random.rand(100)

#     if y_axis == 'Sin':
#         y = np.sin(x)
#     elif y_axis == 'Cos':
#         y = np.cos(x)

#     if plot_type == 'Line':
#         plt.plot(x, y)
#     elif plot_type == 'Scatter':
#         plt.scatter(x, y)

#     plt.title('My Plot')
#     plt.xlabel(x_axis)
#     plt.ylabel(y_axis)

# # Create the Streamlit interface
# st.title('Plot Generator')

# x_axis = st.selectbox('X-Axis Type', ['Linear', 'Random'])
# y_axis = st.selectbox('Y-Axis Type', ['Sin', 'Cos'])
# plot_type = st.selectbox('Plot Type', ['Line', 'Scatter'])

# if st.button('Generate Plot'):
#     st.pyplot(generate_plot(x_axis, y_axis, plot_type))


'''