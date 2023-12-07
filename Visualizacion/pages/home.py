import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

from components.kpi.kpibadge import kpibadge
from components.maps.mapsample import mapsample
from components.charts.chats_reports import charts_bank



kpi1 = kpibadge("1'471.766", 'Total Base', 'Approved')
kpi2 = kpibadge('18', 'Numero de Variables', 'Approved')
kpi3 = kpibadge('325', 'Total transacciones', 'Approved')
kpi4 = kpibadge('2122','Total User', 'Danger')

mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

chart_anio = charts_bank('Quejas por Años','id_1')


layout=  dbc.Container(
        [
            dbc.Row([
                dbc.Col([
                    kpi1.display()
                ], className='card'),
                dbc.Col([
                    kpi2.display()
                ], className='card'),
                dbc.Col([
                    kpi3.display()
                ], className='card'),
                dbc.Col([
                    kpi4.display()
                ], className='card')
            ]),
            dbc.Row([
                dbc.Col([
                    chart_anio.display()
                ], xs=12, className='card'),            
            ]),   
        ]
    )   
