import plotly.express as px
from dash import html , dcc

from app.data.data_contector import Conector_db


class complaints_per_product():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart():
        con = Conector_db()
        df = con.complaints_per_product()
        fig = px.bar(df, y='product', x='count', orientation='h', title='Horizontal Bar Chart',
                    labels={'count': 'Count', 'product': 'Product'})
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