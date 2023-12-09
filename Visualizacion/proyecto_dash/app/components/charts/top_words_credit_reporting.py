
from app.data.data_contector import Conector_db
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os
import pandas as pd

class top_words_credit_reporting():

    def __init__(self,map_title:str,ID:str):
        self.con = Conector_db()
        self.map_title = map_title
        self.id = ID

    @staticmethod
    def chart():
        script_dir = os.path.dirname(__file__)  # Ruta del directorio del script actual
        file_path = os.path.join(script_dir, 'files/top_words_credit_reporting.csv')
        df = pd.read_csv(file_path)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(zip(df['word'], df['count'])))

        # Convertir la imagen de la nube de palabras a base64
        img_data = BytesIO()
        wordcloud.to_image().save(img_data, format='PNG')
        img_str = "data:image/png;base64," + base64.b64encode(img_data.getvalue()).decode()
        return img_str
    

    def display(self):    
        layout = html.Div(
                [
                    html.H4([self.map_title]),
                    html.Img(src=self.chart(), 
                            style={'width': '80%', 
                                   'height': '80%',
                                   'align-items': 'center',
                                   'text-aling': 'center',
                                   })
                ],id=self.id
            )
        return layout