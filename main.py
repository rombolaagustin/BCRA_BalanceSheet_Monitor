# BCRA Balance Sheet Monitor


# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tools.mapping import sheet_names
from tools.mapping import cols_names
from tools.functions import download_file

# Control Variables
hours_to_download = 3
url = 'https://www.bcra.gob.ar/Pdfs/PublicacionesEstadisticas/series.xlsm'
filename = 'series.xlsm'

# Download file from BCRA website 
download_file(url, filename, hours_to_download)

# Build DataFrames
data = dict()
for sheet_name in sheet_names:
    print(f'Processing {sheet_name} sheet ...')
    data[sheet_name] = pd.read_excel(
        io=filename,
        sheet_name=sheet_name,
        header=None,
        skiprows=9,
        names=cols_names[sheet_name])

    # Remove useless columns
    for col_name in cols_names[sheet_name]:
        if 'delete' in col_name:
            data[sheet_name] = data[sheet_name].drop(col_name, axis=1)
        elif 'date' in col_name or 'tipo_serie' in col_name:
            pass
        else:
            data[sheet_name][col_name] = data[sheet_name][col_name].replace(',', '', regex=True).astype(float)
    # Filter daily info
    data[sheet_name] = data[sheet_name][data[sheet_name]['tipo_serie']=='D']

    print(f'OK: {sheet_name} was processed successfully')

# Process DF
# df = pd.DataFrame()
# df['fecha'] = data['BASE MONETARIA']['fecha'][data['BASE MONETARIA']['tipo_serie']=='D']
# df['base monetaria'] = data['BASE MONETARIA']['total'][data['BASE MONETARIA']['tipo_serie']=='D']
# df['billetes publico'] = data['BASE MONETARIA']['billetes publico'][data['BASE MONETARIA']['tipo_serie']=='D']
# df['billetes entidades'] = data['BASE MONETARIA']['billetes entidades'][data['BASE MONETARIA']['tipo_serie']=='D']
# df['circulacion monetaria'] = df['billetes publico'] + df['billetes entidades']

# # Monthly df
# df_month = df.resample(rule='M', on='fecha').mean()
# df_month['fecha'] = df_month.index
# # Ratios
# df_ratios = pd.DataFrame()
# df_ratios['fecha'] = df['fecha']
# df_ratios['circulacion monetaria / BM'] = df['circulacion monetaria']/df['base monetaria']


# Main 
st.title('BCRA Balance Sheet Monitor')

st.subheader('Agregados Monetarios')

for sheet_name in sheet_names:
    st.write(sheet_name)
    st.dataframe(data=data[sheet_name])

fig = plt.figure(figsize=(12,8))
plt.plot(data['RESERVAS']['tipo de cambio'])
st.pyplot(fig)