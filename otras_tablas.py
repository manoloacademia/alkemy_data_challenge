import pandas as pd
import numpy as np
import requests
import csv

# Archivos .csv de datos generales procesados
cines = pd.read_csv('data/cines/2022-junio/cines-29-06-2022.csv')
museos = pd.read_csv('data/museos/2022-junio/museos-29-06-2022.csv')
bibliotecas = pd.read_csv('data/bibliotecas/2022-junio/bibliotecas-29-06-2022.csv')

# Generación de tabla de datos generales
tabla_general = pd.concat([cines, museos, bibliotecas], axis=0, ignore_index=True)
tabla_general = tabla_general.drop('Unnamed: 0', axis=1)
tabla_general.to_csv('tabla_general.csv')

# Generación de tabla de registro de análisis por categoría
total_registro_cat = pd.DataFrame(tabla_general.categoria.value_counts())

# Gerenación de tabla de categoría y provincia
total_cat_prov = pd.DataFrame(tabla_general.groupby(['provincia', 'categoria']).count())
total_cat_prov = pd.DataFrame(total_cat_prov.iloc[:,0])
total_cat_prov.rename(columns={'cod_localidad':'por_cat_prov'}, inplace=True)

# Generación de tabla de cines desde raw_data de url
r = requests.get('https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv')
download = r.content.decode('utf-8')
csv_file = csv.reader(download.splitlines(), delimiter=',')
csv_creator = list(csv_file)
raw_data = pd.DataFrame(csv_creator[1:], columns=csv_creator[0])

# Modificación de valores de columnas para poder acumular
raw_data['Pantallas'] = raw_data['Pantallas'].astype(int)
raw_data['Butacas'] = raw_data['Butacas'].astype(int)
if raw_data['espacio_INCAA'].empty:
    raw_data['espacio_INCAA'] = 0
else:
     raw_data['espacio_INCAA'] = 1
raw_data['espacio_INCAA'] = raw_data['espacio_INCAA'].astype(int)

# Generación de tabla como data frame
cines_tabla = raw_data.groupby(['Provincia']).agg({'Pantallas':[np.sum], 'Butacas':[np.sum], 'espacio_INCAA':[np.sum]})
cines_tabla = pd.DataFrame(cines_tabla)