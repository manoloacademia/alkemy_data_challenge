"""
En este archivo, se creará la función que permita crear los directorios.
El detalle de los directorios es: "categoría\año-mes\"
Si el archivo ya existe, debe reemplazarse.
Quedarán guardados en la carpeta "Data" del proyecto.
"""
# Importar liberías para comunicarnos con el sistema operativo y la librería datetime
import os
from pathlib import Path
import datetime
import locale

# Generar la constante del mes (en español) en el que estamos
locale.setlocale(locale.LC_TIME, '')
ANIO_MES = datetime.date.today().strftime('%Y-%B')

# Generar la constante del día en el que realizamos la descarga
FECHA_DESCARGA = datetime.date.today().strftime('%d-%m-%Y')

# Definir el directorio base para hacer la generación
BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).absolute()

# Definir la función de generación de los directorios
def crear_directorios(categoria:str):
    """
    Esta función, realiza la creación de los directorios en donde se 
    guardarán los archivos del análisis de los datos.
    """
    dir_cat = fr'data\{categoria}'
    os.mkdir(os.path.join(BASE_DIR, dir_cat))
    dir_fecha = fr'data\{categoria}\{ANIO_MES}'
    path_nuevo = os.path.join(BASE_DIR, dir_fecha)
    os.mkdir(path_nuevo)

categorias = ['cines', 'bibliotecas', 'museos']
for categoria in categorias:
    crear_directorios(categoria)


