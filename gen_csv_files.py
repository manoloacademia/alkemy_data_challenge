"""
Este archivo permite obtener la información de las 3 fuentes (bibliotecas, cines, museos)
y las guarda en Data Frames de la librería Pandas
"""

# Importar librerías
import pandas as pd
import requests
import csv
import locale
import datetime
#from decouple import config

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
museos = archivos_csv[0]
cines = archivos_csv[1]
bibliotecas = archivos_csv[2]

# Revisamos las columnas que tienen los data frames
# print(df_museos.columns)
# print(df_cines.columns)
# print(df_bibliotecas.columns)
# existen diferencias en las columnas

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

# Definir funciones para que extraigan los datos y completen los archivos csv con las columnas finales
def datos_museos(df_museos: pd.DataFrame):
    df_museos_csv = pd.DataFrame(columns=columnas)
    df_museos_csv['cod_localidad'] = df_museos['Cod_Loc']
    df_museos_csv['id_provincia'] = df_museos['IdProvincia']
    df_museos_csv['id_departamento'] = df_museos['IdDepartamento']
    df_museos_csv['categoria'] = df_museos['categoria']
    df_museos_csv['provincia'] = df_museos['provincia']
    df_museos_csv['localidad'] = df_museos['localidad']
    df_museos_csv['nombre'] = df_museos['nombre']
    df_museos_csv['domicilio'] = df_museos['direccion']
    df_museos_csv['código postal'] = df_museos['CP']
    df_museos_csv['número de teléfono'] = df_museos['cod_area'] + df_museos['telefono']
    df_museos_csv['mail'] = df_museos['Mail']
    df_museos_csv['web'] = df_museos['Web']
    return df_museos_csv

def datos_cines(df_cines: pd.DataFrame):
    df_cines_csv = pd.DataFrame(columns=columnas)
    df_cines_csv['cod_localidad'] = df_cines['Cod_Loc']
    df_cines_csv['id_provincia'] = df_cines['IdProvincia']
    df_cines_csv['id_departamento'] = df_cines['IdDepartamento']
    df_cines_csv['categoria'] = df_cines['Categoría']
    df_cines_csv['provincia'] = df_cines['Provincia']
    df_cines_csv['localidad'] = df_cines['Localidad']
    df_cines_csv['nombre'] = df_cines['Nombre']
    df_cines_csv['domicilio'] = df_cines['Dirección']
    df_cines_csv['código postal'] = df_cines['CP']
    df_cines_csv['número de teléfono'] = df_cines['cod_area'] + df_cines['Teléfono']
    df_cines_csv['mail'] = df_cines['Mail']
    df_cines_csv['web'] = df_cines['Web']
    return df_cines_csv

def datos_bibliotecas(df_bibliotecas: pd.DataFrame):
    df_bibliotecas_csv = pd.DataFrame(columns=columnas)
    df_bibliotecas_csv['cod_localidad'] = df_bibliotecas['Cod_Loc']
    df_bibliotecas_csv['id_provincia'] = df_bibliotecas['IdProvincia']
    df_bibliotecas_csv['id_departamento'] = df_bibliotecas['IdDepartamento']
    df_bibliotecas_csv['categoria'] = df_bibliotecas['Categoría']
    df_bibliotecas_csv['provincia'] = df_bibliotecas['Provincia']
    df_bibliotecas_csv['localidad'] = df_bibliotecas['Localidad']
    df_bibliotecas_csv['nombre'] = df_bibliotecas['Nombre']
    df_bibliotecas_csv['domicilio'] = df_bibliotecas['Domicilio']
    df_bibliotecas_csv['código postal'] = df_bibliotecas['CP']
    df_bibliotecas_csv['número de teléfono'] = df_bibliotecas['Cod_tel'] + df_bibliotecas['Teléfono']
    df_bibliotecas_csv['mail'] = df_bibliotecas['Mail']
    df_bibliotecas_csv['web'] = df_bibliotecas['Web']
    return df_bibliotecas_csv

# Generar la constante del mes (en español) en el que estamos
locale.setlocale(locale.LC_TIME, '')
ANIO_MES = datetime.date.today().strftime('%Y-%B')

# Generar la constante del día en el que realizamos la descarga
FECHA_DESCARGA = datetime.date.today().strftime('%d-%m-%Y')

# Se generan los archivos .csv en las carpetas correspondientes desde los data frames de datos
def generar_csv(categoria: str):
    if categoria == 'museos':
        df = datos_museos(museos)
    if categoria == 'cines':
        df = datos_cines(cines)
    if categoria == 'bibliotecas':
        df = datos_bibliotecas(bibliotecas)
    csv_to_file = df.to_csv(f'data\{categoria}\{ANIO_MES}\{categoria}-{FECHA_DESCARGA}.csv')
    return csv_to_file

# Se prueban los archivos generados
generar_csv('museos')
generar_csv('cines')
generar_csv('bibliotecas')