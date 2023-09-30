### Trabalho Prático II

* Este aplicativo é um visualizador de dados utilizando gráficos que carregam dados oriundos de base de dados do banco MySQL. Os gráficos são gerados utilizando a biblioteca Express do Plotly e utilizando a linguagem Python.

* O servidor é construido com a biblioteca Dash.

* Foram implementadas funções do tipo:
    * Ler endereço do computador em que existam arquivos de dados de determinada extensão;
    * Ler os dados destes arquivos e transformá-los em formato Pandas DataFrame;
    * Criar base de dados no banco MySQL a partir dos dados de um Pandas DataFrame;
    * Criar um Pandas DataFrame a partir de dados existentes em banco de dados MySQL;
    * Gerar scripts SQL (DDL (CREATE), DQL (SELECT) e DML (INSERT)) em formato .sql;
    * Criar/Salvar arquivo .sql;
    * Gerar Pandas DataFrame com dados de todas as tabelas do banco de dados MySQL;
    * Gerar gráficos interativos para visualização de dados utilizando a biblioteca Plotly.


#### Base teste

* Para teste, deverá ser executado o arquivo [`database.sql`](https://github.com/alexmichelon/growdev-formacao-analista-de-dados/blob/alex-michelon-trabalho-final-ii/11-projeto-pratico-ii/trabalho_final/src/database/file/database.sql) em conjunto ao banco de dados MySQL. A base de dados [NFL Statistics](https://www.kaggle.com/datasets/kendallgillies/nflstatistics/download?datasetVersionNumber=1) foi recuperada do sítio eletrônico [`Kaggle`](https://www.kaggle.com/), onde este DataSet encontra-se em formato csv.
    Obs.: poderá ser utilizada qualquer based de dados provindo do banco de dados MySQL.

* O endereço para acesso da aplicação é: http://127.0.0.1:8888/.

* Para executar a aplicação, basta executar o arquivo [`server.py`](https://github.com/alexmichelon/growdev-formacao-analista-de-dados/blob/alex-michelon-trabalho-final-ii/11-projeto-pratico-ii/trabalho_final/src/server.py) o qual está localizado na raíz da aplicação.

* Para criação do arquivo de dados [`database.sql`](https://github.com/alexmichelon/growdev-formacao-analista-de-dados/blob/alex-michelon-trabalho-final-ii/11-projeto-pratico-ii/trabalho_final/src/database/file/database.sql), deverá ser executado o arquivo de formato notebook [`create_database.ipynb`](https://github.com/alexmichelon/growdev-formacao-analista-de-dados/blob/alex-michelon-trabalho-final-ii/11-projeto-pratico-ii/trabalho_final/src/crate_database.ipynb).


#### Pré-requisitos

* MySQL ([Documentação](https://dev.mysql.com/doc/))

    > `https://dev.mysql.com/downloads/installer/`

    > `pip install mysql`


* Dash ([Documentação](https://dash.plotly.com/))

    > `pip install dash`


* Plotly ([Documentação](https://plotly.com/))

    > `pip install plotly`


* Pandas ([Documentação](https://pandas.pydata.org/))

    > `pip install pandas`


* SQLAlchemy ([Documentação](https://docs.sqlalchemy.org/))

    > `pip install sqlalchemy`    


* Pathlib ([Documentação](https://docs.python.org/3/library/pathlib.html))

    > `pip install pathlib`  


#### Rotas

* /
    * Rota que carrega a página inicial da aplicação, onde são apresentados os gráficos e as opções de filtragem globais e por gráfico individual:
        * visualização de gráfico em barras;
        * visualização de gráfico de dispersão (bolhas);
        * opções de filtragem de dados por gráfico e globais.


#### Sugestão de desenvolvimentos futuros (não implementados na versão atual)

* Criar opção em tela para informação de configurações de banco de dados para permitir que o usuário consiga carregar quaisquer base de dados;

* Criar opção em tela para informação de configurações de colunas para junção de tabelas na formação do Pandas DataFrame;

* Criar opção em tela para informação de configurações de colunas referência para geração dos gráficos;

* Permitir que a aplicação crie um Pandas DataFrame para cada tabela do banco de dados conforme as opções de filtragem escolhidas pelo usuário: na versão atual criou-se um DataFrame com todas as opções do banco de dados, o que pode tornar a aplicação mais lenta;

* Criar visualização de dados para outros tipos de gráficos, por exemplo: line, pie, etc.;

* Criar opção em tela para informação de qual tipo de gráfico o usuário deseja visualizar;

* Customizar o cabeçalho da aplicação: criar artes e figuras para disponibilizar na página inicial;

* Permitir exportar os gráficos em formato HTML.