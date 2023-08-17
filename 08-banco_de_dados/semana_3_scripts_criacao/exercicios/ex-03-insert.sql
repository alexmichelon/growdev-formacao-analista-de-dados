USE ex_3;

SHOW TABLES;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE acesso;
TRUNCATE TABLE acesso_midia_assistida;
TRUNCATE TABLE acesso_midia_assistindo;
TRUNCATE TABLE categoria;
TRUNCATE TABLE classificacao;
TRUNCATE TABLE conta;
TRUNCATE TABLE dispositivo;
TRUNCATE TABLE dispositivo_conta;
TRUNCATE TABLE elenco;
TRUNCATE TABLE enquadramento_midia;
TRUNCATE TABLE forma_pagamento;
TRUNCATE TABLE genero;
TRUNCATE TABLE midia;
TRUNCATE TABLE midia_assistida;
TRUNCATE TABLE midia_assistindo;
TRUNCATE TABLE orientacao_sexual;
TRUNCATE TABLE participante;
TRUNCATE TABLE perfil;
TRUNCATE TABLE plano;
TRUNCATE TABLE plataforma;
TRUNCATE TABLE plataforma_plano;
TRUNCATE TABLE raca;
TRUNCATE TABLE regiao;
TRUNCATE TABLE religiao;
TRUNCATE TABLE sexo;
TRUNCATE TABLE subcategoria;
TRUNCATE TABLE tipo_participante;
TRUNCATE TABLE usuario;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO forma_pagamento (descricao) VALUES ('Cartão de crédito');
INSERT INTO forma_pagamento (descricao) VALUES ('Cartão de débito');
INSERT INTO forma_pagamento (descricao) VALUES ('Boleto');

INSERT INTO plano (descricao, numero_telas, tipo_resolucao, valor) VALUES ('Básico', 1, 'SD', 19.90);
INSERT INTO plano (descricao, numero_telas, tipo_resolucao, valor) VALUES ('Intermediário', 2, 'HD', 29.90);
INSERT INTO plano (descricao, numero_telas, tipo_resolucao, valor) VALUES ('Avançado', 4, 'HD', 45.90);

INSERT INTO conta (data_inicio, status_conta, dia_vencimento, id_forma_pagamento, id_plano) VALUES ('2023-07-15', 'S', 10, 1, 2);
INSERT INTO conta (data_inicio, status_conta, dia_vencimento, id_forma_pagamento, id_plano) VALUES ('2023-07-16', 'S', 1, 3, 3);

INSERT INTO regiao (cidade, estado, pais) VALUES ('São Paulo', 'SP', 'Brasil');
INSERT INTO regiao (cidade, estado, pais) VALUES ('São Joaquim', 'SP', 'Brasil');

INSERT INTO sexo (descricao) VALUES ('Masculino');
INSERT INTO sexo (descricao) VALUES ('Feminino');

INSERT INTO religiao (descricao) VALUES ('Católica');
INSERT INTO religiao (descricao) VALUES ('Muçulmana');

INSERT INTO raca (descricao) VALUES ('Branca');
INSERT INTO raca (descricao) VALUES ('Negra');
INSERT INTO raca (descricao) VALUES ('Parda');

INSERT INTO orientacao_sexual (descricao) VALUES ('Heterossexual');
INSERT INTO orientacao_sexual (descricao) VALUES ('Homossexual');
INSERT INTO orientacao_sexual (descricao) VALUES ('Bissexual');

INSERT INTO usuario (nome, data_nascimento, nome_usuario, e_mail, senha, id_regiao, id_sexo, id_religiao, id_raca, id_orientacao_sexual) VALUES ('Alex Michelon', '1986-08-16', 'Alex', 'alexmichelonn@gmail.com', '123ABC', 2, 1, 1, 1, 1);
INSERT INTO usuario (nome, data_nascimento, nome_usuario, e_mail, senha, id_regiao, id_sexo, id_religiao, id_raca, id_orientacao_sexual) VALUES ('João Silveira', '1970-01-12', 'João', 'joao@gmail.com', 'ABCDFGRRT', 1, 1, 2, 2, 2);
INSERT INTO usuario (nome, data_nascimento, nome_usuario, e_mail, senha, id_regiao, id_sexo, id_religiao, id_raca, id_orientacao_sexual) VALUES ('Marina Nunes', '2005-11-02', 'Nina', 'marinanunes@gmail.com', '123ABCXDE', 2, 2, 1, 2, 3);

INSERT INTO plataforma (descricao) VALUES ('Chrome');
INSERT INTO plataforma (descricao) VALUES ('Android');
INSERT INTO plataforma (descricao) VALUES ('iOS');
INSERT INTO plataforma (descricao) VALUES ('Smart TV');

INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (2, 1);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (3, 1);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (1, 2);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (2, 2);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (3, 2);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (1, 3);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (2, 3);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (3, 3);
INSERT INTO plataforma_plano (id_plataforma, id_plano) VALUES (4, 3);

INSERT INTO dispositivo (descricao, endereco_mac, id_plataforma) VALUES ('Android Motorola XYZ', '00:1B:44:11:3A:B7', 2);
INSERT INTO dispositivo (descricao, endereco_mac, id_plataforma) VALUES ('Chrome PC Home', '00:1C:33:22:3A:C9', 1);
INSERT INTO dispositivo (descricao, endereco_mac, id_plataforma) VALUES ('Smart TV Sala Casa', '11:5B:65:00:9I:G1', 4);

INSERT INTO dispositivo_conta (id_conta, id_dispositivo) VALUES (1, 3);
INSERT INTO dispositivo_conta (id_conta, id_dispositivo) VALUES (1, 1);
INSERT INTO dispositivo_conta (id_conta, id_dispositivo) VALUES (2, 3);
INSERT INTO dispositivo_conta (id_conta, id_dispositivo) VALUES (2, 2);

INSERT INTO perfil (id_usuario, id_conta, descricao) VALUES (3, 1, 'Eu');
INSERT INTO perfil (id_usuario, id_conta, descricao) VALUES (1, 2, 'Alex');
INSERT INTO perfil (id_usuario, id_conta, descricao) VALUES (1, 2, 'Esposa');

INSERT INTO acesso (data_acesso, data_saida, id_dispositivo, id_perfil) VALUES ('2023-07-16 16:05:00', '2023-07-16 22:15:00', 1, 1);
INSERT INTO acesso (data_acesso, data_saida, id_dispositivo, id_perfil) VALUES ('2023-07-17 09:55:00', '2023-07-17 12:06:00', 3, 2);
INSERT INTO acesso (data_acesso, data_saida, id_dispositivo, id_perfil) VALUES ('2023-07-17 15:32:00', '2023-07-17 21:15:00', 3, 2);
INSERT INTO acesso (data_acesso, data_saida, id_dispositivo, id_perfil) VALUES ('2023-07-18 21:02:00', '2023-07-18 23:24:00', 2, 3);

INSERT INTO classificacao (descricao) VALUES ('18');
INSERT INTO classificacao (descricao) VALUES ('10');
INSERT INTO classificacao (descricao) VALUES ('Livre');

INSERT INTO midia (titulo, tempo_duracao, data_disponibilizacao, ativo, data_lancamento, resumo, id_classificacao) VALUES('Tropa de Elite', '02:23:00', '2010-05-12', 'S', '2016-05-25', 'Um filme brasileiro que retrata a violência das favelas do Rio de Janeiro.', 1);
INSERT INTO midia (titulo, tempo_duracao, data_disponibilizacao, ativo, data_lancamento, resumo, id_classificacao) VALUES('Tropa de Elite 2', '01:52:00', '2014-01-06', 'S', '2019-01-02', 'Um filme brasileiro que conta a ação do Capitão Nascimento agora na administração da polícia.', 1);
INSERT INTO midia (titulo, tempo_duracao, data_disponibilizacao, ativo, data_lancamento, resumo, id_classificacao) VALUES('Missão Impossível', '01:39:00', '2002-05-06', 'S', '2015-12-01', 'O melhor filme de ação já feito.', 3);
INSERT INTO midia (titulo, tempo_duracao, data_disponibilizacao, ativo, data_lancamento, resumo, id_classificacao) VALUES('Missão Impossível 2', '01:55:00', '2005-07-05', 'S', '2016-02-27', 'tom Cruise retorna a pela de Ethan Hunt.', 3);

INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-16', 'Gostei', 1);
INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-16', 'Gostei', 2);
INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-16', 'Gostei', 3);
INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-16', 'Gostei', 4);
INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-17', 'Gostei', 1);
INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-17', 'Não Gostei', 2);
INSERT INTO midia_assistida (data_assistida, satisfacao, id_midia) VALUES ('2023-07-18', 'Gostei', 1);

INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (1, 1);
INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (1, 2);
INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (1, 3);
INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (1, 4);
INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (2, 1);
INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (3, 2);
INSERT INTO acesso_midia_assistida (id_acesso, id_midia_assistida) VALUES (4, 7);

INSERT INTO midia_assistindo (data_assistindo, minuto_parada, id_midia) VALUES ('2023-07-17', '00:25:00', 2);
INSERT INTO midia_assistindo (data_assistindo, minuto_parada, id_midia) VALUES ('2023-07-17', '00:48:00', 1);
INSERT INTO midia_assistindo (data_assistindo, minuto_parada, id_midia) VALUES ('2023-07-17', '01:16:00', 4);

INSERT INTO acesso_midia_assistindo (id_acesso,  id_midia_assistindo) VALUES (2, 1);
INSERT INTO acesso_midia_assistindo (id_acesso,  id_midia_assistindo) VALUES (3, 2);
INSERT INTO acesso_midia_assistindo (id_acesso,  id_midia_assistindo) VALUES (3, 3);

INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Tom Cruise', 'Estados Unidos', '1968-02-12', 1);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Michael Bay', 'Estados Unidos', '1975-01-02', 1);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Jean Reno', 'França', '1960-12-25', 1);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Thandie Newton', 'Estados Unidos', '1979-05-01', 2);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Wagner Moura', 'Brasil', '1978-10-10', 1);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Milhem Cortaz', 'Brasil', '1970-05-10', 1);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Fernanda Machado', 'Brasil', '1989-01-29', 2);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('André Ramiro', 'Brasil', '1985-03-03', 1);
INSERT INTO participante (nome, nacionalidade, data_nascimento, id_sexo) VALUES ('Jose Padilha', 'Brasil', '1962-05-03', 1);

INSERT INTO tipo_participante (descricao) VALUES ('Ator');
INSERT INTO tipo_participante (descricao) VALUES ('Atriz');
INSERT INTO tipo_participante (descricao) VALUES ('Diretor');

INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 5, 1);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 6, 1);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (2, 7, 1);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 8, 1);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (3, 9, 1);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 5, 2);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 6, 2);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 8, 2);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (3, 9, 2);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 1, 3);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (3, 2, 3);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 3, 3);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (1, 1, 4);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (3, 2, 4);
INSERT INTO elenco (id_tipo_participante, id_participante, id_midia) VALUES (2, 4, 4);

INSERT INTO categoria (descricao) VALUES ('Filme');
INSERT INTO categoria (descricao) VALUES ('Documentário');
INSERT INTO categoria (descricao) VALUES ('Série');

INSERT INTO subcategoria (descricao) VALUES ('Policial');
INSERT INTO subcategoria (descricao) VALUES ('Ação');
INSERT INTO subcategoria (descricao) VALUES ('Comédia');
INSERT INTO subcategoria (descricao) VALUES ('Romance');
INSERT INTO subcategoria (descricao) VALUES ('Drama');

INSERT INTO genero (descricao) VALUES ('Violento');
INSERT INTO genero (descricao) VALUES ('De tirar o Folego');
INSERT INTO genero (descricao) VALUES ('Sentimental');
INSERT INTO genero (descricao) VALUES ('Religião');
INSERT INTO genero (descricao) VALUES ('Realidade Nua e Cruz');
INSERT INTO genero (descricao) VALUES ('Espião');

INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (1, 1, 1, 1);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (1, 1, 1, 5);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (1, 1, 2, 1);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (1, 1, 2, 5);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (2, 1, 1, 1);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (2, 1, 1, 5);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (2, 1, 2, 1);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (2, 1, 2, 5);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (3, 1, 2, 2);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (3, 1, 2, 6);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (4, 1, 2, 2);
INSERT INTO enquadramento_midia (id_midia, id_categoria, id_subcategoria, id_genero) VALUES (4, 1, 2, 6);