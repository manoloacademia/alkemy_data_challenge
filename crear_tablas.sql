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
CREATE TABLE datos_generales (
    id serial,
    cod_localidad double precision,
    id_departamento int,
    categoria varchar(128),
    provincia varchar(128),
    localidad varchar(128),
    nombre varchar(128),
    domicilio varchar(128),
    código_postal int,
    número_de_teléfono double precision,
    mail varchar(128),
    web varchar(128)
);

-- Se crea tabla de datos conjuntos
CREATE TABLE datos_conjuntos (
    id serial,
    total_categorias int,
    total_registro_fuente int,
    total_registro_provincia int
);

-- Se crea tabla de cines
CREATE TABLE cines (
    id serial,
    provincia varchar(128),
    pantallas int,
    butacas int,
    catidad_INCAA int
);

