
import pandas as pd
import plotly.graph_objects as go

from sqlalchemy import create_engine


class Conector_db():

    def __init__(self):
            self.__database="data_bank"
            self.__user="user"
            self.__password="password"
            self.__host="localhost"
            self.__port="5432"
            self.__text = f'postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}'

    def info_anio(self):
        connDockerLocal = create_engine(self.__text, echo=False)
        df = pd.read_sql_query("SELECT * FROM num_anio;", con=connDockerLocal)
        return df
    

    def table_productIssu(self):
        connDockerLocal = create_engine(self.__text, echo=False)
        df = pd.read_sql_query("SELECT * FROM complaints_max_per_product_issue;", con=connDockerLocal)
        return df
    

    def map_complaints(self):
        connDockerLocal = create_engine(self.__text, echo=False)
        df = pd.read_sql_query("SELECT * FROM complaints_per_100k_state;", con=connDockerLocal)
        return df
    
    def chart_complaints_per_channel(self):
        connDockerLocal = create_engine(self.__text, echo=False)
        df = pd.read_sql_query("SELECT * FROM complaints_per_channel;", con=connDockerLocal)
        return df
    
    def complaints_per_product(self):
        connDockerLocal = create_engine(self.__text, echo=False)
        df = pd.read_sql_query("SELECT * FROM complaints_per_product;", con=connDockerLocal)
        return df
    
    def top_words_mortgage(self):
        connDockerLocal = create_engine(self.__text, echo=False)
        df = pd.read_sql_query("SELECT * FROM top_words_mortgage;", con=connDockerLocal)
        return df


