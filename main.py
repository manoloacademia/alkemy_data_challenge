""" Este archivo permite satisfacer los requerimientos del Alkemy Data Analytics + Python Challenge.
En el mismo se busca la conexión con 3 fuentes de datos públicos argentinos y se generan archivos .csv 
para analizar más en detalle la información.
Este archivo también alimenta tablas de ese análisis a una base de datos PostgreSQL.
"""
# Importar las librerías necesarias
import os
import logging
from decouple import config

# Seteo de logging
logging.basicConfig(level=logging.DEBUG, filename='datos_generados.log', filemode='a', format='%(asctime)s:%(levelname)s:%(message)s')

# Importar los modulos correspondientes
from gen_directories import crear_directorios
from gen_csv_files import generar_csv, gen_tabla_normalizada
from otras_tablas import analisis_datos_cines, tabla_categoria, tabla_fuente, tabla_prov_cat
from conexion_db import alimentar_db

# Importar los datos necesarios para la conexión a la base de datos
user = config('DB_USER')
passwd = config('DB_PASSWORD')
host = config('DB_HOST')
port = config('DB_PORT')
db = config('DB_NAME')

if __name__ == '__main__':
  # Crear directorio data
    os.mkdir('data')
    logging.info("Se crea directorio data.")

    # Generar los directorios correspondientes
    try: 
        categorias = ['cines', 'bibliotecas', 'museos']
        for categoria in categorias:
            crear_directorios(categoria)
        logging.info("Directorios generados.")
    except Exception as e:
        logging.warning(f'Los directorios ya se encuentran creados. El detalle de la excepcion es: {e}')

    # Generar los archivos .csv    
    try:
        gen_tabla_normalizada()
        generar_csv('museos')
        generar_csv('cines')
        generar_csv('bibliotecas')
        logging.info('Archivos csv generados correctamente.')
    except:
        logging.warning('Los archivos ya se encuentran generados.')

    # Generar las otras tablas
    try:
        analisis_datos_cines()
        tabla_categoria()
        tabla_fuente()
        tabla_prov_cat()
        logging.info("Se crean correctamente las tablas de análisis.")
    except:
        logging.warning("Chequear que se hayan importado correctamente los archivos csv.")
    
    # Generar conexión a base de datos y alimentar las tablas
    try:
        alimentar_db(gen_tabla_normalizada(), 'tabla_general', user, passwd, host, port, db)
        alimentar_db(analisis_datos_cines(), 'tabla_cines', user, passwd, host, port, db)
        alimentar_db(tabla_categoria(), 'tabla_por_categoria', user, passwd, host, port, db)
        alimentar_db(tabla_fuente(), 'tabla_por_fuente', user, passwd, host, port, db)
        alimentar_db(tabla_prov_cat(), 'tabla_por_provincia_categoria', user, passwd, host, port, db)
        logging.info('Se crean las tablas correspondientes en la base de datos.')
    except Exception as e:
        logging.warning(f'Revisar los datos de conexión a los archivos anteriores. Revisar excepción: {e}.')