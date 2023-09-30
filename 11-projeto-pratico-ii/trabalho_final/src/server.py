from dash import Dash
from database.data import Data
from components.body import Body
from charts.bar import LineChart
from charts.scatter import ScatterChart

app = Dash(__name__)

#chamada dos objetos do tipo gráfico
LineChart.create_chart('chart1', 'global_filter_1', 'global_filter_2', 'df_columns', 'function', Data.df, app)
ScatterChart.create_chart('chart2', 'global_filter_1', 'global_filter_2', 'x_column', 'y_column', 'size', Data.df, app)

body = Body() #cria objeto da classe Body()

app.layout = body.get() #instancia a página

if __name__ == "__main__":
    app.run_server(
        debug = True, #reinicia o servidor caso seja alterado algum arquivo
        port = 8888 #definição da porta 
    ) 