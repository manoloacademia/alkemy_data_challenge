import pandas as pd
import numpy as np
import locale
import datetime
from pathlib import Path
import os

from gen_csv_files import csv_datos_fuente

# Generar la constante del mes (en español) en el que estamos
locale.setlocale(locale.LC_TIME, '')
ANIO_MES = datetime.date.today().strftime('%Y-%B')

# Generar la constante del día en el que realizamos la descarga
FECHA_DESCARGA = datetime.date.today().strftime('%d-%m-%Y')

# Definir el directorio base para hacer la generación
BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).absolute()

# Archivos .csv de datos generales procesados
museos, cines, bibliotecas = csv_datos_fuente()

# Modificación de valores de columnas para poder acumular en la tabla de datos generales para cines
def analisis_datos_cines(cines: pd.DataFrame):
    """ Esta función permite realizar la tabla de análisis de cines así como el 
    recuento de las butacas, pantallas y los espacios INCAA.
    """
    cines['Pantallas'] = cines['Pantallas'].astype(int)
    cines['Butacas'] = cines['Butacas'].astype(int)
    if cines['espacio_INCAA'].empty:
        cines['espacio_INCAA'] = 0
    else:
        cines['espacio_INCAA'] = 1
    cines_tabla = cines.groupby(['Provincia']).agg({'Pantallas':[np.sum], 'Butacas':[np.sum], 'espacio_INCAA':[np.sum]})
    cines_tabla = pd.DataFrame(cines_tabla)
    
    return cines_tabla

tabla_cines = analisis_datos_cines(cines)

# Definir tabla por categoría
def tabla_categoria():
    """ Esta función realiza un Data Frame con la tabla de Cantidad
    de registros totales por Categoría.
    """
    lista = []
    lista.append((museos.categoria.unique()[0], museos.categoria.count()))
    lista.append((cines.Categoría.unique()[0], cines.Categoría.count()))
    lista.append((bibliotecas.Categoría.unique()[0], bibliotecas.Categoría.count()))
    df_cat = pd.DataFrame(lista, columns=['categoria', 'cuenta'])
    
    return df_cat

# Definir tabla por fuente
def tabla_fuente():
    """ Esta función realiza un Data Frame con la tabla de Cantidad
    de registros totales por Categoría.
    """
    lista = []
    lista.append((museos.fuente.unique()[0], museos.fuente.count()))
    lista.append((cines.Fuente.unique()[0], cines.Fuente.count()))
    lista.append((bibliotecas.Fuente.unique()[0], bibliotecas.Fuente.count()))
    df_fuente = pd.DataFrame(lista, columns=['fuente', 'cuenta'])
    
    return df_fuente

# Definir tabla por provincia y por categoría
def tabla_prov_cat():
    """ Esta función realiza un Data Frame con la cuenta de registros
    por provincia y por categoría.
    """
    museos_df = museos.groupby(['provincia', 'categoria'])['IdProvincia'].count().reset_index()
    cines_df = cines.groupby(['Provincia', 'Categoría'])['IdProvincia'].count().reset_index()
    bibliotecas_df = bibliotecas.groupby(['Provincia', 'Categoría'])['IdProvincia'].count().reset_index()
    
    museos_df['cuenta'] = museos_df['IdProvincia']
    museos_df = museos_df.drop('IdProvincia', axis=1)
    cines_df['cuenta'] = cines_df['IdProvincia']
    cines_df = cines_df.drop('IdProvincia', axis=1)
    bibliotecas_df['cuenta'] = bibliotecas_df['IdProvincia']
    bibliotecas_df = bibliotecas_df.drop('IdProvincia', axis=1)
    cines_df['provincia'] = cines_df['Provincia']
    bibliotecas_df['provincia'] = bibliotecas_df['Provincia']
    cines_df['categoria'] = cines_df['Categoría']
    bibliotecas_df['categoria'] = bibliotecas_df['Categoría']
    cines_df = cines_df.drop('Provincia', axis=1)
    bibliotecas_df = bibliotecas_df.drop('Provincia', axis=1)
    cines_df = cines_df.drop('Categoría', axis=1)
    bibliotecas_df = bibliotecas_df.drop('Categoría', axis=1)
    tabla_prov_cat = pd.concat([museos_df, cines_df, bibliotecas_df], axis=0)
    
    return tabla_prov_cat

if __name__ == '__main__':
    tabla_cines = analisis_datos_cines(cines)
    por_categoria = tabla_categoria()
    por_fuente = tabla_fuente()
    tabla_provincia_categoría = tabla_prov_cat()
    