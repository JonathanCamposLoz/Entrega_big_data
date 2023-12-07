
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

