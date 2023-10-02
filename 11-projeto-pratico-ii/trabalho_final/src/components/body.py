from dash.html import Div, H4
from dash.dcc import Graph, Dropdown
from database.data import Data
from components.header import header

class Body:
    def __init__(self):
        self.body = Div(
            children=[
                header,
                Div(
                    className='container',
                    children=[
                        #Filtros Globais
                        Div(
                            className='div-filtros',
                            children=[
                                #Global Filter 1
                                Div(
                                    className='div-filtros-item',
                                    children = [
                                        Div(
                                            children=[
                                                #Label Global Filter 1
                                                H4(
                                                    Data.global_column_1_label,
                                                    style={'color': 'black'},
                                                    className='div-filtros-item-label',
                                                ),
                                                Dropdown(
                                                    id = 'global_filter_1',
                                                    options=Data.get_column_values('current_team'),
                                                    value=Data.get_column_values('current_team')[0],
                                                    clearable=False,
                                                    searchable=False,
                                                )   
                                            ],
                                        ),
                                    ]
                                ),
                                #Global Filter 2
                                Div(
                                    className='div-filtros-item',
                                    children=[
                                        Div(
                                            children=[
                                                #Label Global Filter 2
                                                H4(
                                                    Data.global_column_2_label,
                                                    style={'color': 'black'},
                                                    className='div-filtros-item-label',
                                                ),
                                                Dropdown(
                                                    id = 'global_filter_2',
                                                    options=Data.get_column_values('position'),
                                                    value=Data.get_column_values('position')[0],
                                                    clearable=False,
                                                    searchable=False,
                                                )   
                                            ]
                                        ),    
                                    ]
                                ),                                                               
                            ]
                        ),
                        # Charts
                        Div(
                            className='col',
                            children=[
                                #Chart 1
                                Div(
                                    className='div-grafico',
                                    children=[  
                                        #Chart 1 Filters
                                        Div(
                                            className='div-subfiltros',
                                            children = [
                                                #Chart 1 Filter 1
                                                Div(
                                                    className='div-subfiltros-item',
                                                    children = [
                                                        #Chart 1 Label Filter 1
                                                        H4(
                                                            'Columns',                                                            
                                                            className='div-subfiltros-item-label',
                                                        ),
                                                        Dropdown(
                                                            id="df_columns",
                                                            options=Data.get_numeric_column(),
                                                            value=Data.get_numeric_column()[0],
                                                            clearable=False,
                                                            searchable=False,
                                                        ),
                                                    ]
                                                ),
                                                #Chart 1 Filter 2
                                                Div(
                                                    className='div-subfiltros-item',
                                                    children = [
                                                        #Chart 1 Label Filter 1
                                                        H4(
                                                            'Function',
                                                            className='div-subfiltros-item-label',
                                                        ),
                                                        Dropdown(
                                                            id="function",
                                                            options=[
                                                                {'label': 'Soma', 'value': 'sum'},
                                                                {'label': 'Mínimo', 'value': 'idxmin'},
                                                                {'label': 'Máximo', 'value': 'idxmax'},
                                                                {'label': 'Média', 'value': 'mean'},
                                                            ],
                                                            value="sum",                                                            
                                                            clearable=False,
                                                            searchable=False,
                                                        ),
                                                    ]
                                                )
                                            ]
                                        ),
                                        #Chart 1                                      
                                        Graph(
                                            id='chart1',
                                            className='grafico',
                                        )
                                    ]
                                ),
                                #Chart 2
                                Div(
                                    className='div-grafico',
                                    children=[
                                        #Chart 2 Filters
                                        Div(
                                            className='div-subfiltros',
                                            children=[
                                                #Chart 2 Filter 1
                                                Div(
                                                    className='div-subfiltros-item',
                                                    children = [
                                                        #Chart 2 Filter 1 Label
                                                        H4(
                                                            'X Axis',
                                                            className='div-subfiltros-item-label',
                                                        ),
                                                        Dropdown(
                                                            id="x_column",
                                                            options=Data.get_numeric_column(),
                                                            value=Data.get_numeric_column()[0],
                                                            clearable=False,
                                                            searchable=False,
                                                        ),
                                                    ]
                                                ),
                                                #Chart 2 Filter 2
                                                Div(
                                                    className='div-subfiltros-item',
                                                    children = [
                                                        #Chart 2 Filter 2 Label
                                                        H4(
                                                            'Y Axis',
                                                            className='div-subfiltros-item-label',
                                                        ),
                                                        Dropdown(
                                                            id="y_column",
                                                            options=Data.get_numeric_column(),
                                                            value=Data.get_numeric_column()[0],
                                                            clearable=False,
                                                            searchable=False,
                                                        ),
                                                    ]
                                                ),
                                                #Chart 2 Filter 3
                                                Div(
                                                    className='div-subfiltros-item',
                                                    children = [
                                                        #Chart 2 Filter 3 Label
                                                        H4(
                                                            'Bubble Size',
                                                            className='div-subfiltros-item-label',
                                                        ),
                                                        Dropdown(
                                                            id="size",
                                                            options=Data.get_numeric_column(),
                                                            value=Data.get_numeric_column()[0],
                                                            clearable=False,
                                                            searchable=False,
                                                        ),
                                                    ]
                                                )
                                            ]    
                                        ),
                                        #Chart 2
                                        Graph(
                                            id='chart2',
                                            className='grafico',
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    #método para recuperar objeto página
    def get(self):
        return self.body    