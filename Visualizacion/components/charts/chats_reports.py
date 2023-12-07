import plotly.express as px
from dash import html , dcc

from data.data_contector import Conector_db


class charts_bank():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart_anio():
        con = Conector_db()
        df = con.info_anio()
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