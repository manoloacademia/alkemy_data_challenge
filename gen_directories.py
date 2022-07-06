""" En este archivo, se creará la función que permita crear los directorios.
El detalle de los directorios es: "categoría\año-mes\"
Si el archivo ya existe, debe reemplazarse.
Quedarán guardados en la carpeta "Data" del proyecto.
"""
# Importar liberías para comunicarnos con el sistema operativo y la librería datetime
import os
from pathlib import Path
import datetime
import locale
import logging

# Seteo de logging
logging.basicConfig(level=logging.DEBUG, filename='datos_generados.log', filemode='a', format='%(asctime)s:%(levelname)s:%(message)s')

# Generar la constante del mes (en español) en el que estamos
locale.setlocale(locale.LC_TIME, '')
ANIO_MES = datetime.date.today().strftime('%Y-%B')

# Generar la constante del día en el que realizamos la descarga
FECHA_DESCARGA = datetime.date.today().strftime('%d-%m-%Y')

# Definir el directorio base para hacer la generación
BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).absolute()

# Definir la función de generación de los directorios
def crear_directorios(categoria:str):
    """ Esta función, realiza la creación de los directorios en donde se 
    guardarán los archivos del análisis de los datos.
    """
    try:
        dir_cat = os.path.join('data', categoria)
        dir_cat = os.path.join(BASE_DIR, dir_cat) 
        os.mkdir(dir_cat)
        dir_fecha = os.path.join(dir_cat, f'{ANIO_MES}')
        path_nuevo = os.path.join(BASE_DIR, dir_fecha)
        os.mkdir(path_nuevo)
        logging.info("Se crean los directorios de categorías y los específicos al mes y año.")
    except:
        dir_fecha = os.path.join(dir_cat, f'{ANIO_MES}')
        path_nuevo = os.path.join(BASE_DIR, dir_fecha)
        os.mkdir(path_nuevo)
        logging.info("Se crean solamente los directorios de mes y año ya que los de categoría existen.")

if __name__ == '__main__':
    # Crear directorio data
    os.mkdir('data')
    logging.info("Se crea directorio data.")

    try: 
        categorias = ['cines', 'bibliotecas', 'museos']
        for categoria in categorias:
            crear_directorios(categoria)
        logging.info("Directorios generados.")
    except Exception as e:
        logging.warning(f'Los directorios ya se encuentran creados. El detalle de la excepcion es: {e}')