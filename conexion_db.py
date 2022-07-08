from sqlalchemy_conn import get_engine_from_settings
import pandas as pd
import logging

# Seteo de logging
logging.basicConfig(level=logging.DEBUG, filename='datos_generados.log', filemode='a', format='%(asctime)s:%(levelname)s:%(message)s')

# Importar los módulos de los archivos correspondientes
from gen_csv_files import gen_tabla_normalizada
from otras_tablas import analisis_datos_cines, tabla_categoria, tabla_fuente, tabla_prov_cat

# Generar tabla donde se inyectarán los valores de los data frames
def alimentar_db(tabla: pd.DataFrame, tabla_sql: str):
    """ Esta función genera una tabla en la base de datos PostgreSQL
    y la alimenta con el data frame que se ingresa como argumento.
    """
    engine = get_engine_from_settings()
    tabla.to_sql(f'{tabla_sql}', con=engine, if_exists='replace')

if __name__ == '__main__':
    
    try:
        alimentar_db(gen_tabla_normalizada(), 'tabla_general')
        alimentar_db(analisis_datos_cines(), 'tabla_cines')
        alimentar_db(tabla_categoria(), 'tabla_por_categoria')
        alimentar_db(tabla_fuente(), 'tabla_por_fuente')
        alimentar_db(tabla_prov_cat(), 'tabla_por_provincia_categoria')
        logging.info('Se crean las tablas correspondientes en la base de datos.')
    except:
        logging.warning('Revisar los datos de conexión.')
