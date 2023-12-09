import plotly.express as px
from dash import html , dcc

from app.data.data_contector import Conector_db
import pandas as pd

import os

class charts_infAnio():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart_anio():
        script_dir = os.path.dirname(__file__)  # Ruta del directorio del script actual
        file_path = os.path.join(script_dir, 'files/num_anio.csv')
        df = pd.read_csv(file_path)
        fig = px.bar(df, x='anio', y='cantidad')
        return fig

    def display(self):    
        layout = html.Div(
                [
                    html.H4([self.map_title]),
                    html.Div([
                        dcc.Graph(figure=self.chart_anio())
                    ])
                    
                ],id=self.id
            )
        return layout