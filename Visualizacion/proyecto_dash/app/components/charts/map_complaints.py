import plotly.express as px
from dash import html , dcc

from app.data.data_contector import Conector_db

import pandas as pd

import os

class map_complaints():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart():
        script_dir = os.path.dirname(__file__)  # Ruta del directorio del script actual
        file_path = os.path.join(script_dir, 'files/complaints_per_100k_state.csv')
        df = pd.read_csv(file_path)
        fig = px.choropleth(df, 
                            locations='state',  # Columna que contiene los códigos de los estados
                            locationmode='USA-states',  # Modo de ubicación para estados de EE. UU.
                            color='complaint_count',  # Columna que determina el color de los estados
                            hover_name='full_name',  # Información que se muestra al pasar el ratón sobre los estados
                            title='Complaint Count by State',
                            color_continuous_scale='viridis')

        # Mostrar el gráfico

        # Configurar el diseño del mapa para enfocarse en los Estados Unidos
        fig.update_geos(
            scope='usa',
            visible=False,
            center={'lat': 37.0902, 'lon': -95.7129}  # Coordenadas del centro del mapa (centrado en Estados Unidos)
        )
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