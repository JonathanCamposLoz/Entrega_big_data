
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

integrantes = [
    {"nombre": "Carlos Alberto Ceballos", "puesto": "Visualizacion"},
    {"nombre": "Otto Ramoz", "puesto": "Analisis Descriptivo"},
    {"nombre": "Nini Yohana Ruiz Rodriguez", "puesto": "Analisis Descriptivo"},
    {"nombre": "Jonathan Campos Lozano", "puesto": "Docker-AWSS"},
    # Agrega más integrantes según sea necesario
]


integrantes_cards = [
    dbc.Card(
        dbc.CardBody([
            html.H4(integrante["nombre"], className="card-title"),
            html.P(integrante["puesto"], className="card-text"),
        ])
    ) for integrante in integrantes
]

layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H1(['Integrantes']),
                dbc.Row(integrantes_cards),
            ], lg=12),
        ])
    ]
)