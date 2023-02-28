import os
import pandas as pd
from urllib import request
from datetime import datetime
from .mapping import sheet_names
from .mapping import cols_names

# DOWNLOAD FILE
def download_file(url: str, filename: str, hours: float):
    try: 
        creation_date = os.path.getctime(filename)
        now = datetime.now().timestamp()
        if hours*60*60 < now-creation_date:
            print(f'Downloading {filename} ...')
            response = request.urlretrieve(url, filename)
        else:
            print('OK: File is up to date')
    except:
        print(f'{filename} does not exist. Downloading...')
        response = request.urlretrieve(url, filename)

# PREPROCESSING
def preprocessing_data(filename):
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

        # Filling data
        data[sheet_name].index = data[sheet_name]['date']
        del data[sheet_name]['date']
        del data[sheet_name]['tipo_serie']
        data[sheet_name] = data[sheet_name].resample('1D').interpolate()
        print(f'OK: {sheet_name} was filled')
        print(f'OK: {sheet_name} was processed successfully')
    return data

# BUILD NOMINAL DATAFRAME
def build_nominal_data(data):
    bm_rename = {
        'billetes publico': 'Billetes en poder del publico',
        'billetes entidades': 'Billetes en entidades',
        'cheques': 'Cheques',
        'cuenta corriente': 'Cuenta corriente del BCRA',
        'semitotal': 'Base Monetaria (sin cuasimonedas)',
        'cuasimonedas': 'Cuasimonedas',
        'total': 'Base Monetaria'
    }
    # Use BM's date like parameter to compare
    nominal_data = data['BASE MONETARIA'][list(bm_rename.keys())]  

    # New data
    nominal_data['Circulacion Monetaria'] = nominal_data['billetes publico'] + nominal_data['billetes entidades']

    nominal_data = nominal_data.rename(columns=bm_rename)
    
    # nominal_data['cajas de ahorro'] = data['DEPOSITOS']['TOTAL ca'].values
    # nominal_data['cuenta corriente'] = data['DEPOSITOS']['TOTAL cc'].values
    # nominal_data['M2'] =  nominal_data['billetes publico'] + nominal_data['cajas de ahorro'] + nominal_data['cajas de ahorro']
    #nominal_data.reindex()
    print(nominal_data.info())
    return nominal_data

    