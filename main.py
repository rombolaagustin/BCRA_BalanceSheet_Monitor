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
data.make_var_yearly(base100=True)

# Main 
st.title(':flag-ar: BCRA Balance Sheet Monitor :flag-ar:')

st.subheader('Agregados Monetarios')

st.dataframe(data.nominal)

st.dataframe(data.yearly)

st.area_chart(data.yearly['Base Monetaria'])

print(data.yearly.info())