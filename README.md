# Alkemy Data Analytics + Python Challenge

Este repo fue realizado para resolver el challenge adjunto: [Challenge_Data_Analytics_con_Python](https://github.com/manoloacademia/alkemy_data_challenge/blob/main/Challenge_Data_Analytics_con_Python.pdf).<br>
Primero hay que crear e iniciarse en el entorno virtual con el comando: `python -m venv venv`.<br>
Luego, es necesario instalar las dependencias para la ejecución correcta: `pip install -r requirements.txt`.<br>
Una vez ya instalado, para correr el programa es necesario ejecutar el **Main**: `python main.py`.<br>
El logueo está grabado en el [archivo datos_generados.log](https://github.com/manoloacademia/alkemy_data_challenge/blob/main/datos_generados.log).

## Módulos de alimentación a archivo main.py
El detalle de los módulos que alimentan al main se encuentra en los archivos presentes en la carpeta.

### El `main.py` realiza las siguientes acciones
- Descarga de los datos desde las 3 fuentes en archivos .csv.
- Genera los directorios específicos para cada archivo de los datos-fuente.
- Transforma los datos-fuente en las tablas generales con columnas normalizadas.
- Genera tabla general normalizada con los datos de las 3 fuentes.
- Envía estas tablas (pandas Data Frames) a los archivos correspondientes.
- Genera el motor y la conexión con la base de datos **PostgreSQL**.
- Genera tablas extras de análisis desde archivos de datos-fuente.
- Alimenta la base de datos.
- Genera archivo de logging y manejo de errores.
