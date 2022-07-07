import pandas as pd
import numpy as np
import locale
import datetime
from pathlib import Path
import os

# Generar la constante del mes (en español) en el que estamos
locale.setlocale(locale.LC_TIME, '')
ANIO_MES = datetime.date.today().strftime('%Y-%B')

# Generar la constante del día en el que realizamos la descarga
FECHA_DESCARGA = datetime.date.today().strftime('%d-%m-%Y')

# Definir el directorio base para hacer la generación
BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).absolute()

# Archivos .csv de datos generales procesados
def datos_fuentes():
    """ Esta función toma los archivos de datos-fuente bajados y los 
    devuelve en data frames.    
    """
    archivos_dato_fuente = []
    for categoria in ['museos', 'cines', 'bibliotecas']:
        dir_cat = os.path.join(BASE_DIR,'data')
        dir_cat = os.path.join(dir_cat,f'{categoria}')
        dir_fecha = os.path.join(dir_cat,f'{ANIO_MES}')
        dir_file = os.path.join(dir_fecha,f'{categoria}-{FECHA_DESCARGA}')
        dato_fuente_cat = pd.read_csv(dir_file)
        archivos_dato_fuente.append(dato_fuente_cat)
    museos = archivos_dato_fuente[0]
    cines = archivos_dato_fuente[1]
    bibliotecas = archivos_dato_fuente[2]
    return museos, cines, bibliotecas
        
museos, cines, bibliotecas = datos_fuentes()

# Modificación de valores de columnas para poder acumular en la tabla de datos generales para cines
def analisis_datos_cines(cines: pd.DataFrame):
    """ Esta función permite realizar la tabla de análisis de cines así como el 
    recuento de las butacas, pantallas y los espacios INCAA.
    """
    raw_data = pd.DataFrame()
    raw_data['Pantallas'] = cines['Pantallas'].astype(int)
    raw_data['Butacas'] = cines['Butacas'].astype(int)
    if cines['espacio_INCAA'].empty:
        raw_data['espacio_INCAA'] = 0
    else:
        raw_data['espacio_INCAA'] = 1
    raw_data['espacio_INCAA'] = cines['espacio_INCAA'].astype(int)
    cines_tabla = raw_data.groupby(['Provincia']).agg({'Pantallas':[np.sum], 'Butacas':[np.sum], 'espacio_INCAA':[np.sum]})
    cines_tabla = pd.DataFrame(cines_tabla)
    return cines_tabla

tabla_cines = analisis_datos_cines(cines)

# Generación de tabla de registro de análisis por categoría
total_registro_cat = pd.DataFrame(tabla_general.categoria.value_counts())

# Gerenación de tabla de categoría y provincia
total_cat_prov = pd.DataFrame(tabla_general.groupby(['provincia', 'categoria']).count())
total_cat_prov = pd.DataFrame(total_cat_prov.iloc[:,0])
total_cat_prov.rename(columns={'cod_localidad':'por_cat_prov'}, inplace=True)
