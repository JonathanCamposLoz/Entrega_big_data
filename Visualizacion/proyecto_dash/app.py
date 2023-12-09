#libraries
import dash
from flask import Flask
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import os

#from callbacks import register_callbacks
server = Flask(__name__)

request_path_prefix = None
#app = dash.Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.FLATLY],)
    
# Dash instance declaration

app = Dash(
    __name__,
    server=server,
    pages_folder="app/pages",
    use_pages=True,
    external_stylesheets=[dbc.themes.FLATLY]
)

script_dir = os.path.dirname(__file__)  # Ruta del directorio del script actual
img_rute = os.path.join(script_dir, 'app/assets/Unisabana.png')


#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink( "Inicio", href=request_path_prefix)),
    dbc.DropdownMenu(
        [
            
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="Data Science",
    ),
    ],

    brand=[
    html.Img(src='./app/assets/Unisabana.png', height="30px"),
    "Presentación Trabajo Final - Big Data"], 
    color="primary",
    dark=True,
    className="mb-2",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
	    dash.page_container
    ],
    className="dbc",
    fluid=True,
)


# This call will be used with Gunicorn server
server = app.server
app.scripts.config.serve_locally = True
# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=True)
