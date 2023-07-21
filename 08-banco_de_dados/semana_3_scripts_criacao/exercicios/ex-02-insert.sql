USE ex_2;

SHOW TABLES;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE equipe;
TRUNCATE TABLE jogada;
TRUNCATE TABLE local;
TRUNCATE TABLE participante;
TRUNCATE TABLE partida;
TRUNCATE TABLE pessoa;
TRUNCATE TABLE posicao;
TRUNCATE TABLE posicao_participante;
TRUNCATE TABLE tipo_jogada;
TRUNCATE TABLE usuario;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('12345678989', 'Alex Michelon',       '1986-01-01');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('33345678989', 'Jose Dias',           '1980-03-05');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('33344477788', 'Carlos Martins Dias', '1991-06-06');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('00155579988', 'João Castro',         '1982-10-01');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('10100574400', 'Rubens Cardoso',      '1988-11-12');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('10100247152', 'Luiz Carlos Silva',   '1999-03-01');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('86920185298', 'Gustavo Pontes',      '1980-11-01');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('65760385491', 'Messias Barbosa',     '1995-08-22');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('23566663257', 'Mario Gomes',         '2000-12-30');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('77778900200', 'Cezário Cordova',     '1965-08-20');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('77778900200', 'Giovani Souza',       '1979-01-19');
INSERT INTO pessoa (cpf, nome, data_nascimento) VALUES ('77778900200', 'Marcos Jesus',        '1991-01-18');

INSERT INTO usuario (nome_usuario, senha, e_mail, id_pessoa) VALUES ('Alex Michelon', '123ABC123', 'alexmichelonn@gmail.com', 1);
INSERT INTO usuario (nome_usuario, senha, e_mail, id_pessoa) VALUES ('Marcos Jesus', 'ABCDFE', 'marcosjesus@gmail.com', 12);

INSERT INTO local (nome_ginasio, rua, numero, bairro, cidade, uf) VALUES ('Juraci Santos', 'Rua Ismael Nunes', '12', 'Centro', 'São Joaquim', 'SC');
INSERT INTO local (nome_ginasio, rua, numero, bairro, cidade, uf) VALUES ('Educandário Santa Izabel', 'Rua Vicente Cantizani', 'SN', 'Martorano', 'São Joaquim', 'SC');

INSERT INTO equipe (nome, data_fundacao, escudo, id_local) VALUES ('Caixaria', '2005-11-25', NULL, 1);
INSERT INTO equipe (nome, data_fundacao, escudo, id_local) VALUES ('Atlético', '2012-02-10', NULL, 2);

INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (1.91, 95, 8, 1, 1);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (1.93, 99, 8, 2, 1);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.02, 120, 8, 3, 1);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.05, 110, 8, 4, 1);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.11, 90, 8, 5, 1);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (1.90, 100, 8, 6, 2);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.00, 100, 8, 7, 2);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.08, 101, 8, 8, 2);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.21, 115, 8, 9, 2);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (2.12, 110, 8, 10, 2);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (1.78, 102, 8, 11, 1);
INSERT INTO participante (altura, peso, numero, id_pessoa, id_equipe) VALUES (1.85, 95, 8, 12, 2);

INSERT INTO posicao (descricao) VALUES ('Armador');
INSERT INTO posicao (descricao) VALUES ('Ala');
INSERT INTO posicao (descricao) VALUES ('Pivo');
INSERT INTO posicao (descricao) VALUES ('Treinador');

INSERT INTO partida (data_inicio, id_equipe_casa, id_equipe_visitante, id_local) VALUES ('2023-07-19 20:00:00', 1, 2, 1);

INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (1, 1);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (2, 1);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (3, 2);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (4, 2);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (5, 3);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (11, 4);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (6, 1);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (7, 1);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (8, 2);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (9, 2);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (10, 3);
INSERT INTO posicao_participante (id_participante, id_posicao) VALUES (12, 4);

INSERT INTO tipo_jogada (descricao, pontuacao) VALUES ('Lance Livre', 1);
INSERT INTO tipo_jogada (descricao, pontuacao) VALUES ('Cesta Garrafão', 2);
INSERT INTO tipo_jogada (descricao, pontuacao) VALUES ('Cesta Três Pontos', 3);
INSERT INTO tipo_jogada (descricao, pontuacao) VALUES ('Falta', 0);
INSERT INTO tipo_jogada (descricao, pontuacao) VALUES ('Pedido de Tempo', 0);

INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 2, '00:01:00', 1, 1);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 3, '00:02:00', 7, 2);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 1, '00:03:00', 10, 2);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 1, '00:03:00', 10, 2);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 4, '00:05:00', 1, 1);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 3, '00:06:00', 4, 1);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 2, '00:12:00', 1, 1);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 4, '00:14:00', 8, 2);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 3, '00:15:00', 7, 2);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 3, '00:18:00', 4, 2);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 2, '00:18:00', 1, 1);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 3, '00:19:00', 1, 1);
INSERT INTO jogada (id_partida, id_tipo_jogada, minuto, id_participante, id_equipe_participante) VALUES (1, 5, '00:20:00', 11, 1);