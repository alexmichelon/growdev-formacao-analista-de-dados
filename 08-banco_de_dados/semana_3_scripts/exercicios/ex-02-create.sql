DROP SCHEMA IF EXISTS ex_2;

CREATE SCHEMA IF NOT EXISTS ex_2;

USE ex_2;

CREATE TABLE IF NOT EXISTS pessoa (
  id INT NOT NULL AUTO_INCREMENT,
  cpf VARCHAR(11) NOT NULL,
  nome VARCHAR(45) NOT NULL,
  data_nascimento DATE NOT NULL,
  PRIMARY KEY (id)
 );

CREATE TABLE usuario (
  id INT NOT NULL AUTO_INCREMENT,
  nome_usuario VARCHAR(45) NOT NULL,
  senha VARCHAR(15) NOT NULL,
  e_mail VARCHAR(45) NOT NULL,
  id_pessoa INT NOT NULL,
  PRIMARY KEY (id, id_pessoa),
  FOREIGN KEY (id_pessoa) REFERENCES pessoa (id)
);

CREATE TABLE local(
  id INT NOT NULL AUTO_INCREMENT,
  nome_ginasio VARCHAR(45) NOT NULL,
  rua VARCHAR(45) NOT NULL,
  numero CHAR(5) NOT NULL,
  bairro VARCHAR(45) NOT NULL,
  cidade VARCHAR(45) NOT NULL,
  uf CHAR(2) NOT NULL,
  PRIMARY KEY (id)
 );

CREATE TABLE equipe (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  data_fundacao DATE NOT NULL,
  escudo BLOB,
  id_local INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_local) REFERENCES local (id)
 );

CREATE TABLE participante (
  id INT NOT NULL AUTO_INCREMENT,
  altura DOUBLE NOT NULL,
  peso DOUBLE NOT NULL,
  numero SMALLINT NOT NULL,
  id_pessoa INT NOT NULL,
  id_equipe INT NOT NULL,
  PRIMARY KEY (id, id_pessoa, id_equipe),
  FOREIGN KEY (id_pessoa) REFERENCES pessoa (id),
  FOREIGN KEY (id_equipe) REFERENCES equipe (id)
);

CREATE TABLE posicao (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE partida (
  id INT NOT NULL AUTO_INCREMENT,
  data_inicio DATETIME(6) NOT NULL,
  id_equipe_casa INT NOT NULL,
  id_equipe_visitante INT NOT NULL,
  id_local INT NOT NULL,
  PRIMARY KEY (id, id_equipe_casa, id_equipe_visitante, id_local),
  FOREIGN KEY (id_equipe_casa) REFERENCES equipe (id),
  FOREIGN KEY (id_equipe_visitante) REFERENCES equipe (id),
  FOREIGN KEY (id_local) REFERENCES local (id)
);

CREATE TABLE posicao_participante (
  id_participante INT NOT NULL,
  id_posicao INT NOT NULL,
  PRIMARY KEY (id_participante, id_posicao),
  FOREIGN KEY (id_participante) REFERENCES participante (id),
  FOREIGN KEY (id_posicao) REFERENCES posicao (id)
);

CREATE TABLE tipo_jogada (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  pontuacao INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE jogada (
  id INT NOT NULL AUTO_INCREMENT,
  id_partida INT NOT NULL,
  id_tipo_jogada INT NOT NULL,
  minuto TIME NOT NULL,
  id_participante INT NOT NULL,
  id_equipe_participante INT NOT NULL,
  PRIMARY KEY (id, id_partida, id_tipo_jogada, id_participante, id_equipe_participante),
  FOREIGN KEY (id_partida) REFERENCES partida (id),
  FOREIGN KEY (id_tipo_jogada) REFERENCES tipo_jogada (id),
  FOREIGN KEY (id_participante) REFERENCES participante (id),
  FOREIGN KEY (id_equipe_participante) REFERENCES participante (id_equipe)
);