### API de Dados

* O aplicativo `Análise de Dados` é uma API servidor backend em Python que permite carregar arquivos csv (um por vez), verificar informações estatísticas da base de dados e possibilita manipulações básicas nos dados carregados como consulta e agrupamento.

* O servidor é construido com Flask.


#### Base teste

* Para teste, pode ser utilizada a base ([tabela-fipe-historico-precos.csv](https://www.kaggle.com/datasets/franckepeixoto/tabela-fipe?resource=download)).
    * Obs.: poderá ser utilizada qualquer base de dados concisa em formato csv.


#### Pré-requisitos

* Flask ([Documentação](https://flask.palletsprojects.com/en/2.3.x/))

    > `pip install Flask`

* Pandas ([Documentação](https://pandas.pydata.org/))

    > `pip install pandas`


#### Rotas

* /
    * Rota que carrega a página inicial da aplicação, fornecendo links para as funcionalidades da API:
        * Nome da base setada;
        * Informações descritivas da base de dados;
        * Filtrar dados da base;
        * Agrupar dados da base;
        * Filtrar/Agrupar dados da base.

* /database/describe_info
    * Rota que carrega opção de descrição da base de dados setada:
     * Quantidade de registros existentes;
     * Quantidade, nomes e tipos de dado das colunas;
     * Quantidade de registros nulos por coluna;
     * Informações estatísticas da base carregada (função describe()).

* /database/search
    * Rota que carrega opção de consulta da base  disponibilizando filtros para seleção de dados conforme as colunas. 
    * Disponibiliza também opção em tela com os filtros aplicados na consulta anterior.

* /database/group_by
    * Rota que carrega opção para agrupamento de dados por uma ou várias colunas da base, permitindo aplicar funções (soma, média, maior valor, índice do maior valor, menor valor, índice do menor valor e desvio padrão) sobre os campos selecionados.
    * Disponibiliza também opção em tela para acompanhar os filtros aplicados bem como o comando "groupby" do DataFrame formado pelos filtros selecionados.

* /database/search_group_by
    * Rota que permite aplicar consultas de filtragem e de agrupamento de dados na mesma opção.
    * Disponibiliza também as opções de visualização das opções setadas e comandos formados pelos filtros.


#### Sugestão de desenvolvimentos futuros (não implementados na versão atual)

* Criar opção para carregamento de arquivos: versão atual carrega fixa a base "tabela-fipe-historico-precos.csv";

* Criar opção para permitir renomear colunas;

* Permitir escolher manter filtros setados;

* Controle de filtros de comparação por tipo de dado da coluna setada nas páginas da aplicação;

* Permitir a geração de gráficos com base nos agrupamentos;

* Permitir salvar dados manipulados e gráficos gerados.