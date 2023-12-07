
# Utiliza una imagen base de PostgreSQL
FROM postgres:latest

# Establece las variables de entorno para la base de datos
ENV POSTGRES_DB data_bank
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password

# Copia los scripts SQL al contenedor
COPY ./scripts/ /docker-entrypoint-initdb.d/

# Configura la base de datos al iniciar el contenedor
