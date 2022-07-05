from sqlalchemy_conn import get_engine_from_settings
import pandas as pd

# Generar la tabla donde van a inyectarse los valores de la tabla general
data_tabla_general = pd.read_csv('tabla_general.csv')
data_tabla_general = data_tabla_general.drop('Unnamed: 0', axis=1)

engine = get_engine_from_settings()
data_tabla_general.to_sql('datos_generales', con=engine)

