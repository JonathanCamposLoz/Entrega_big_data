import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

nombre_pagina = "Nubes de Palabras"

dash.register_page(__name__, url_base_pathname=f'/{nombre_pagina}/')

from app.components.charts.top_words_mortgage import top_words_mortgage
from app.components.charts.top_words_all_complaints import top_words_all_complaints
from app.components.charts.top_words_credit_reporting import top_words_credit_reporting
from app.components.charts.top_words_debt_collection import top_words_debt_collection

top_words_mortgage = top_words_mortgage('Top de palabras para quejas en Hipoteca','id_5')
top_words_all_complaints = top_words_all_complaints('Top de palabras quejas en general','id_6')
top_words_credit_reporting = top_words_credit_reporting('Top de palabras quejas de Credito','id_7')
top_words_debt_collection = top_words_debt_collection('Top de palabras quejas de Debito','id_8')


layout=  dbc.Container(
        [
            dbc.Row([
                dbc.Col([
                    top_words_all_complaints.display()  
                ], xs=6, className='card_words'),
                dbc.Col([
                    top_words_mortgage.display()  
                ], xs=6, className='card_words')
         
            ]),
            dbc.Row([
                dbc.Col([
                    top_words_credit_reporting.display()  
                ], xs=6, className='card_words'),
                dbc.Col([
                    top_words_debt_collection.display()  
                ], xs=6, className='card_words')
         
            ]),
            
            


        ]
    )   
