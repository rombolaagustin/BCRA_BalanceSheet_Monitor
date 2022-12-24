# BCRA Balance Sheet Monitor


# Libraries
import streamlit as st
import pandas as pd
import numpy as np
from tools.mapping import sheet_names
from tools.mapping import cols_names
from tools.functions import download_file

# Control Variables
hours_to_download = 1
url = 'https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/series.xlsm'
filename = 'series.xlsm'

# Download file from BCRA website 
download_file(url, filename, hours_to_download)

# Make df
data = dict()
for sheet_name in sheet_names:
    data[sheet_name] = pd.read_excel(
        io=filename,
        sheet_name=sheet_name,
        header=8,
        names=cols_names[sheet_name])

# Main 
st.title('BCRA Balance Sheet Monitor')

st.subheader('Agregados Monetarios')
st.dataframe(data['BASE MONETARIA'])