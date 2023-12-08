import plotly.express as px
from dash import html , dcc

from app.data.data_contector import Conector_db


class complaints_per_channel():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart():
        con = Conector_db()
        df = con.chart_complaints_per_channel()
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