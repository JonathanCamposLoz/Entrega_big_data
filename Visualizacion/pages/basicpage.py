#libraries
import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

    
# dash register page
dash.register_page(__name__)

# Components
from components.maps.mapsample import mapsample

mapa_ejemplo = mapsample('This is my custom map', 'div_samplemap')

# specific layout for this page
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H1(['Page Title'],id="div_title_maps"),
                mapa_ejemplo.display()

            ], lg=12), 
        
        ]),
        ]
)  
