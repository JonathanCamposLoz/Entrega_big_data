import dash
from dash import html , dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

from app.components.kpi.kpibadge import kpibadge
from app.components.charts.chats_infoAnio import charts_infAnio
from app.components.charts.table_productoIssu import charts_TableProduccIssu
from app.components.charts.map_complaints import map_complaints
from app.components.charts.complaints_per_channel import complaints_per_channel
from app.components.charts.complaints_per_product import complaints_per_product
from app.components.charts.top_words_mortgage import top_words_mortgage

kpi1 = kpibadge("1'471.766", 'Total Base', 'Approved')
kpi2 = kpibadge('18', 'Numero de Variables', 'Approved')
kpi3 = kpibadge('325', 'Total transacciones', 'Approved')
kpi4 = kpibadge('2122','Total User', 'Danger')


chart_anio = charts_infAnio('Quejas por Años','id_1')
charts_TableProduccIssu = charts_TableProduccIssu('Tabla productos - Issue','id_2')
map_complaints = map_complaints('Quejas por cada 1000 habitantes','id_3')
complaints_per_channel = complaints_per_channel('Quejas por canal','id_4')
complaints_per_product = complaints_per_product('Quejas por producto','id_5')
top_words_mortgage = top_words_mortgage('Nube de palabras','id_5')


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
                    map_complaints.display()
                ], xs=12, className='card'),            
            ]),   
            dbc.Row([
                dbc.Col([
                    chart_anio.display()
                ], xs=6, className='card'), 
                dbc.Col([
                    complaints_per_channel.display()                    
                ], xs=6, className='card'
                )           
            ]),
            dbc.Row([
                dbc.Col([
                    complaints_per_product.display()
                ], xs=12, className='card'),       
            ]),
            dbc.Row([
                dbc.Col([
                    charts_TableProduccIssu.display()                    
                ], xs=12, className='card'
                )           
            ]),
            dbc.Row([
                dbc.Col([
                    top_words_mortgage.display()  
                ], xs=12, className='card'
                )           
            ]),



        ]
    )   
