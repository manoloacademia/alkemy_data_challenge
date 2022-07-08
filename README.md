# Alkemy Data Analytics + Python Challenge

Se realiza este repo para resolver el Challenge adjuntado de nombre Challenge_Data_Analytics_con_Python.pdf.

Primero hay que crear y realizar el entorno virtual en la terminal realizando: python -m venv venv.

Luego, es necesario instalar las dependencias para la ejecución: pip -r install requirements.txt.

Para correr el programa, es necesario ejecuta: python main.py.

El logueo está grabado en el archivo datos_generados.log.

## Módulos de alimentación a archivo main.py
El detalle de los módulos que alimentan al main, puede encontrarlos en los archivos presentes en la carpeta.

En main.py:
- Descarga de los datos desde las 3 fuentes en archivos .csv.
- Generación de directorios específicos para cada archivo de datos-fuente.
- Transformación de datos-fuente en las tablas generales con columnas normalizadas.
- Envío de estas tablas (pandas Data Frames) a los archivos correspondientes.
- Generación de tabla general normalizada con los datos de las 3 fuentes.
- Generación de motor y conexión con base de datos Postgres.
- Generación de tablas extras de análisis desde archivos de datos-fuente.
- Alimentación de datos a la base de datos.
- Generación de archivo de logging y manejo de errores.
