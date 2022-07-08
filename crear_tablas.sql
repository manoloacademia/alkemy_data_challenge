-- Database: alkemy_data_analytics
DROP DATABASE IF EXISTS alkemy_data_analytics;

CREATE DATABASE alkemy_data_analytics
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE alkemy_data_analytics
    IS 'Se crea base de datos para Alkemy Challenge Data Analytics con Python';

-- Se crea la tabla que contenga la información normalizada de Museos, Salas de Cine y Bibliotecas
CREATE TABLE tabla_general (
    index bigint,
    cod_localidad text,
    id_departamento text,
    categoria text,
    provincia text,
    localidad text,
    nombre text,
    domicilio text,
    código_postal text,
    número_de_teléfono text,
    mail text,
    web text,
    fecha_descarga text
);

-- Se crea tabla por categoria
CREATE TABLE tabla_por_categoria (
    index bigint,
    categoria text,
    cuenta bigint,
    fecha_descarga text
);

-- Se crea tabla por fuente
CREATE TABLE tabla_por_fuente (
    index bigint,
    fuente text,
    cuenta bigint,
    fecha_descarga text
);

-- Se crea tabla por provincia y categoria
CREATE TABLE tabla_por_provincia_categoria (
    index bigint,
    provincia text,
    categoria text,
    cuenta bigint,
    fecha_descarga text
);

-- Se crea tabla de cines
CREATE TABLE tabla_cines (
    index bigint,
    ('Provincia', '') text,
    ('Pantallas', 'sum') int,
    ('Butacas', 'sum') int,
    ('espacio_INCAA', 'sum') int,
    ('fecha_descarga', '') text
);

