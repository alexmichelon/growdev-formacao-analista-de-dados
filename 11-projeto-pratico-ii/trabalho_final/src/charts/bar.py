from dash import Output, Input
from plotly import express as px
from database.data import Data
import charts.color as color

class LineChart:
    
    def create_chart(name, global_filter_1, global_filter_2, df_columns, function, data, app):
        @app.callback(
            Output(name, 'figure'), 
            Input(global_filter_1, 'value'),
            Input(global_filter_2, 'value'),
            Input(df_columns, 'value'),
            Input(function, 'value'),
        )
        def generate_chart(global_filter_1, global_filter_2, df_columns, function):
            #gera DataFrame com dados dos filtros globais
            df_filtered = data.query(f'{Data.global_column_1} == "{global_filter_1}" and {Data.global_column_2} == "{global_filter_2}"')            
            #verifica o tipo da função
            if function == 'sum': 
                df_filtered = df_filtered.groupby('name').sum().reset_index()
                func = 'Sum'
            elif function == 'idxmin':
                minvalue = df_filtered.groupby('name')[f"{df_columns}"].sum().idxmin()
                df_filtered = df_filtered[df_filtered['name'] == minvalue]
                func = 'Idx Min'
            elif function == 'idxmax':
                maxvalue = df_filtered.groupby('name')[f"{df_columns}"].sum().idxmax()
                df_filtered = df_filtered[df_filtered['name'] == maxvalue]
                func = 'Idx Max'
            elif function == 'mean':
                df_filtered = df_filtered.groupby('name')[f"{df_columns}"].mean().reset_index()
                func = 'Mean'            
            fig = px.bar( #cria o gráfico do tipo barras
                df_filtered, #DataFrame base de dados para gerar gráfico
                title = f'<b>{str(df_columns).replace("_", " ").title()} per {str(Data.reference_column).title()} ({func})</b>', #título do gráfico
                x=Data.reference_column, #coluna para determinar valor para o eixo X
                y=df_columns, #coluna para determinar valor para o eixo Y
                color=df_columns, #define a cor com base em valores da coluna
                color_discrete_sequence=color.color_discrete_Antique, #define cor discreta (int, float)
                color_continuous_scale=color.color_scale_cividis, #define cor para colorscale (str)
                text_auto=True #tipo do texto apresentado para x, y ou z
            )
            fig.update_layout(
                title_x=0.5,                 
                xaxis_title=f'<b>{Data.reference_column}</b>', #texto do eixo X
                yaxis_title=f'<b>{str(df_columns).replace("_", " ").title()}</b>') #texto do eixo Y
            fig.update_layout(coloraxis_colorbar=dict(title="")) #tira o título do colorbar
            fig.update_traces(textposition='outside', cliponaxis=False) #define o local onde o label irá aparecer dentro do gráfico e ignorar caso o label fique fora da área do gráfico
            fig.update_yaxes(showticklabels=False) #retira os valores dos índices do gráfico
            return fig