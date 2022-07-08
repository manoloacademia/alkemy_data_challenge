from sqlalchemy_conn import get_engine
import pandas as pd
import logging
import datetime
from decouple import config

user = config('DB_USER')
passwd = config('DB_PASSWORD')
host = config('DB_HOST')
port = config('DB_PORT')
db = config('DB_NAME')

# Seteo de logging
logging.basicConfig(level=logging.DEBUG, filename='datos_generados.log', filemode='a', format='%(asctime)s:%(levelname)s:%(message)s')

# Importar los módulos de los archivos correspondientes
from gen_csv_files import gen_tabla_normalizada
from otras_tablas import analisis_datos_cines, tabla_categoria, tabla_fuente, tabla_prov_cat

# Generar la constante del día en el que realizamos la descarga
FECHA_DESCARGA = datetime.date.today().strftime('%d-%m-%Y')

# Generar tabla donde se inyectarán los valores de los data frames
def alimentar_db(tabla: pd.DataFrame, tabla_sql: str, user, passwd, host, port, db):
    """ Esta función genera una tabla en la base de datos PostgreSQL
    y la alimenta con el data frame que se ingresa como argumento.
    """
    engine = get_engine(user, passwd, host, port, db)
    tabla['fecha_descarga'] = FECHA_DESCARGA
    tabla.to_sql(f'{tabla_sql}', con=engine, if_exists='replace')

if __name__ == '__main__':
    
    try:
        alimentar_db(gen_tabla_normalizada(), 'tabla_general', user, passwd, host, port, db)
        alimentar_db(analisis_datos_cines(), 'tabla_cines', user, passwd, host, port, db)
        alimentar_db(tabla_categoria(), 'tabla_por_categoria', user, passwd, host, port, db)
        alimentar_db(tabla_fuente(), 'tabla_por_fuente', user, passwd, host, port, db)
        alimentar_db(tabla_prov_cat(), 'tabla_por_provincia_categoria', user, passwd, host, port, db)
        logging.info('Se crean las tablas correspondientes en la base de datos.')
    except Exception as e:
        logging.warning(f'Revisar los datos de conexión: {e}.')
