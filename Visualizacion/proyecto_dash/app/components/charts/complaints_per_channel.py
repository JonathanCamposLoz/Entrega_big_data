import plotly.express as px
from dash import html , dcc

from app.data.data_contector import Conector_db

import pandas as pd

import os

class complaints_per_channel():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart():
        script_dir = os.path.dirname(__file__)  # Ruta del directorio del script actual
        file_path = os.path.join(script_dir, 'files/complaints_per_channel.csv')
        df = pd.read_csv(file_path)
        fig = px.pie(df, values='count', names='channel', title='Population of European continent')
        return fig

    def display(self):    
        layout = html.Div(
                [
                    html.H4([self.map_title]),
                    html.Div([
                        dcc.Graph(figure=self.chart())
                    ])
                    
                ],id=self.id
            )
        return layout