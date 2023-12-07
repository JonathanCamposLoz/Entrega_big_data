import pandas as pd
import numpy as np

from prefect import task, flow

from src.aws_conector import *


@task
def consulta_local():
    # recuerde definir los parámetros de conexión a su servidor local implementado con Docker
    host = "localhost"
    port = '5432'
    user = 'user'
    password = 'password'
    database = 'data_bank'

    #conexión a la base de datos local (contenedor de docker)
    connDockerLocal = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}', echo=False)

    df_anio = pd.read_sql_query("select * from public.num_anio;", con=connDockerLocal)
    df_issue = pd.read_sql_query("select * from public.num_issue;", con=connDockerLocal)
    df_producto = pd.read_sql_query("select * from public.num_producto;", con=connDockerLocal)
    df_submitted =  pd.read_sql_query("select * from public.num_submitted;", con=connDockerLocal)

    return df_anio,df_issue, df_producto, df_submitted


@task
def carga_aws_information(**kwargs):
    c = carga_data()
    
    c.infoAnio(kwargs['df_anio'])
    c.infoIssue(kwargs['df_issue'])
    c.infoProducto(kwargs['df_producto'])
    c.infoSubmitted(kwargs['df_submitted'])
 
@flow
def flujo_analitica():
    print('consulta_servidor_local')
    
    df_anio,df_issue, df_producto, df_submitted = consulta_local()
    carga_aws_information(
        df_anio = df_anio,
        df_issue = df_issue, 
        df_producto = df_producto, 
        df_submitted = df_submitted)
    

if __name__ == "__main__":
    flujo_analitica()