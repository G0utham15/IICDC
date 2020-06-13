import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import request



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', "assets\main.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1("Health SCADA", style={'textAlign': 'center'}),
    html.Div([
            html.Div([
            html.Button("Bed-1", className='bed'),
            html.Button('Bed-2', className='bed'),
            html.Button('Bed-3', className='bed'),
            html.Button('Bed-3', className='bed')
            ],
            className='room',
            style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center','height': 250, "border":"2px black solid"},),
            html.Div([
                html.Button("Bed-4", className='bed'),
                html.Button("Bed-4", className='bed'),
                html.Button("Bed-4", className='bed'),
                html.Button('Bed-3', className='bed')
            ],
            className='room',
            style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center','height': 250,"border":"2px black solid"},),
            ], 
            className='column',
            ),
        ])
        




if __name__ == '__main__':
    app.run_server()
