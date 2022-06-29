"""
Este archivo permite obtener la información de las 3 fuentes (bibliotecas, cines, museos)
y las guarda en Data Frames de la librería Pandas
"""

# Importar librerías

import pandas as pd
import requests
import csv
import numpy as np
#from decouple import config

# Columnas de información normalizadas para las fuentes
columnas = [
    'cod_localidad',
    'id_provincia',
    'id_departamento',
    'categoria',
    'provincia',
    'localidad',
    'nombre',
    'domicilio',
    'código postal',
    'número de teléfono',
    'mail',
    'web'
]

# Se define lista de conexión de las 3 fuentes en: categoría-url
LISTA_FUENTES = [
    {'categoria': 'museo', 'url': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'},
    {'categoria': 'cines', 'url': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'},
    {'categoria': 'bibliotecas', 'url': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'}
]

# Realizamos una lista en la cual se cargan los dataframes desde los .csv web
archivos_csv = []
for item in LISTA_FUENTES:
    r = requests.get(item['url'])
    download = r.content.decode('utf-8')
    csv_file = csv.reader(download.splitlines(), delimiter=',')
    csv_creator = list(csv_file)
    raw_data = pd.DataFrame(csv_creator[1:], columns=csv_creator[0])
    archivos_csv.append(raw_data)
    
# Definimos los data frames para cada categoría
df_museo = archivos_csv[0]
df_cines = archivos_csv[1]
df_bibliotecas = archivos_csv[2]