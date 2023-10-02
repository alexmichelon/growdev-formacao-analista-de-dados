from dash import Output, Input
from plotly import express as px
import charts.color as color
from database.data import Data

class ScatterChart:
    
    def create_chart(name, global_filter_1, global_filter_2, x_column, y_column, size, data, app):
        @app.callback(
            Output(name, 'figure'),
            Input(global_filter_1, 'value'),
            Input(global_filter_2, 'value'),
            Input(x_column, 'value'),
            Input(y_column, 'value'),
            Input(size, 'value'),
        )
        def generate_chart(global_filter_1, global_filter_2, x_column, y_column, size):
            df_filtered = data
            if global_filter_1 != None: #verifica se há algo informado no filtro
                df_filtered = df_filtered.query(f'{Data.global_column_1} == "{global_filter_1}"') #filtra o DataFrame conforme filtro global informado
            if global_filter_2 != None: #verifica se há algo informado no filtro
                df_filtered = df_filtered.query(f'{Data.global_column_2} == "{global_filter_2}"') #filtra o DataFrame conforme filtro global informado
            fig = px.scatter( #cria o gráfico do tipo dispersão
                df_filtered, #DataFrame base de dados para gerar gráfico
                x=x_column, #coluna para determinar valor para o eixo X
                y=y_column, #coluna para determinar valor para o eixo Y
                size=size, #coluna para determinar o tamanho das bolhas do gráfico
                title = f'<b>{str(x_column).replace("_", " ").title()} x {str(y_column).replace("_", " ").title()} <br> Bubble Size: {str(size).replace("_", " ").title()}</b>', #título do gráfico
                color=Data.reference_column, #coluna para determinar a cor das bolhas do gráfico
                color_discrete_sequence=color.color_cividis, #define cor discreta (int, float)
                color_continuous_scale=color.color_scale_cividis, #define cor discreta (str)
                opacity=0.75
            )
            fig.update_layout(
                title_x=0.5, 
                xaxis_title=f'<b>{str(x_column).replace("_", " ").title()}</b>', #texto do eixo X
                yaxis_title=f'<b>{str(y_column).replace("_", " ").title()}</b>', #texto do eixo Y
                #legend=dict(orientation='h', yanchor='bottom', xanchor='left', y=-0.35) #define a posição da legenda
            )
            fig.update_traces(
                marker=dict(line=dict(width=1,color='black')),
                selector=dict(mode='markers'))
            return fig