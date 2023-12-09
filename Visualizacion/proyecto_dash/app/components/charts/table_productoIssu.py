import plotly.graph_objects as go
from dash import html , dcc

from app.data.data_contector import Conector_db
import pandas as pd

import os

class charts_TableProduccIssu():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart():
        script_dir = os.path.dirname(__file__)  # Ruta del directorio del script actual
        file_path = os.path.join(script_dir, 'files/complaints_max_per_product_issue.csv')
        df = pd.read_csv(file_path)
        columns = df.columns
        values = [df[col].tolist() for col in columns]

        # Crea la tabla con las columnas y valores
        fig = go.Figure(data=[go.Table(header=dict(values=columns),
                        cells=dict(values=values))
                            ])
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