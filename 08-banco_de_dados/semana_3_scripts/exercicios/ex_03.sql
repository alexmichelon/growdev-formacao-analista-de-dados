DROP SCHEMA IF EXISTS ex_3;

CREATE SCHEMA IF NOT EXISTS ex_3;

USE ex_3;

CREATE TABLE IF NOT EXISTS forma_pagamento (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE plano (
  id INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  numero_telas VARCHAR(45) NOT NULL,
  tipo_resolucao VARCHAR(45) NOT NULL,
  valor DOUBLE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE conta (
  id INT NOT NULL AUTO_INCREMENT,
  data_inicio DATE NOT NULL,
  status CHAR(1) BINARY NOT NULL,
  dia_vencimento CHAR(2) NOT NULL,
  id_forma_pagamento INT NOT NULL,
  id_plano INT NOT NULL,
  PRIMARY KEY (id, id_forma_pagamento, id_plano),
  FOREIGN KEY (id_forma_pagamento) REFERENCES forma_pagamento (id),
  FOREIGN KEY (id_plano) REFERENCES plano (id)
);

CREATE TABLE regiao (
  id INT NOT NULL,
  cidade VARCHAR(45) NOT NULL,
  estado VARCHAR(45) NOT NULL,
  pais VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE sexo (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE religiao (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE raca (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE orientacao_sexual (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE usuario (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  data_nascimento DATE NOT NULL,
  nome_usuario VARCHAR(20) NOT NULL,
  e_mail VARCHAR(20) NOT NULL,
  senha VARCHAR(45) NULL,
  usuariocol VARCHAR(45) NULL,
  id_regiao INT NOT NULL,
  id_sexo INT NOT NULL,
  id_religiao INT NOT NULL,
  id_raca INT NOT NULL,
  id_orientacao_sexual INT NOT NULL,
  PRIMARY KEY (id, id_regiao, id_sexo, id_religiao, id_raca, id_orientacao_sexual),
  FOREIGN KEY (id_regiao) REFERENCES regiao (id),
  FOREIGN KEY (id_sexo) REFERENCES sexo (id),
  FOREIGN KEY (id_religiao) REFERENCES religiao (id),
  FOREIGN KEY (id_raca) REFERENCES raca (id),
  FOREIGN KEY (id_orientacao_sexual) REFERENCES orientacao_sexual (id)
);

CREATE TABLE plataforma (
  id INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE plataforma_plano (
  id_plataforma INT NOT NULL,
  id_plano INT NOT NULL,
  PRIMARY KEY (id_plataforma, id_plano),
  FOREIGN KEY (id_plataforma) REFERENCES plataforma (id),
  FOREIGN KEY (id_plano) REFERENCES plano (id)
);

CREATE TABLE dispositivo (
  id INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  endereco_mac VARCHAR(17) NOT NULL,
  id_plataforma INT NOT NULL,
  PRIMARY KEY (id, id_plataforma),
  FOREIGN KEY (id_plataforma) REFERENCES plataforma (id)
);

CREATE TABLE dispositivo_conta (
  id_conta INT NOT NULL,
  id_dispositivo INT NOT NULL,
  PRIMARY KEY (id_conta, id_dispositivo),
  FOREIGN KEY (id_conta) REFERENCES conta (id),
  FOREIGN KEY (id_dispositivo) REFERENCES dispositivo (id)
);

CREATE TABLE perfil (
  id INT NOT NULL,
  id_usuario INT NOT NULL,
  id_conta INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id, id_usuario, id_conta),
  FOREIGN KEY (id_usuario) REFERENCES usuario (id),
  FOREIGN KEY (id_conta) REFERENCES conta (id)
);

CREATE TABLE acesso (
  id INT NOT NULL,
  data_acesso DATETIME(6) NOT NULL,
  data_saida DATETIME(6) NOT NULL,
  id_dispositivo INT NOT NULL,
  id_perfil INT NOT NULL,
  PRIMARY KEY (id, id_dispositivo, id_perfil),
  FOREIGN KEY (id_dispositivo) REFERENCES dispositivo (id),
  FOREIGN KEY (id_perfil) REFERENCES perfil (id)
);



CREATE TABLE classificacao (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE midia (
  id INT NOT NULL,
  titulo VARCHAR(100) NOT NULL,
  tempo_duracao TIME NOT NULL,
  data_disponibilizacao DATE NOT NULL,
  ativo CHAR(1) BINARY NOT NULL,
  classificacao VARCHAR(15) NOT NULL,
  data_lancamento DATE NOT NULL,
  resumo VARCHAR(2000) NOT NULL,
  id_classificacao INT NOT NULL,
  PRIMARY KEY (id, id_classificacao),
  FOREIGN KEY (id_classificacao) REFERENCES classificacao (id)
);

CREATE TABLE midia_assistida (
  id INT NOT NULL,
  data_assistida DATETIME(6) NOT NULL,
  satisfacao VARCHAR(15) NOT NULL,
  id_midia INT NOT NULL,
  PRIMARY KEY (id, id_midia),
  FOREIGN KEY (id_midia) REFERENCES midia (id)
);

CREATE TABLE midia_assistindo (
  id INT NOT NULL,
  data_assistindo DATETIME(6) NOT NULL,
  minuto_parada TIME NOT NULL,
  id_midia INT NOT NULL,
  PRIMARY KEY (id, id_midia),
  FOREIGN KEY (id_midia) REFERENCES midia (id)
);

CREATE TABLE acesso_midia_assistida (
  id_acesso INT NOT NULL,
  id_midia_assistida INT NOT NULL,
  PRIMARY KEY (id_acesso, id_midia_assistida),
  FOREIGN KEY (id_acesso) REFERENCES acesso (id),
  FOREIGN KEY (id_midia_assistida) REFERENCES midia_assistida (id)
);

CREATE TABLE acesso_midia_assistindo (
  id_acesso INT NOT NULL,
  id_midia_assistindo INT NOT NULL,
  PRIMARY KEY (id_acesso, id_midia_assistindo),
  FOREIGN KEY (id_acesso) REFERENCES acesso (id),
  FOREIGN KEY (id_midia_assistindo) REFERENCES midia_assistindo (id)
);

CREATE TABLE participante (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  nacionalidade VARCHAR(45) NOT NULL,
  data_nascimento DATE NOT NULL,
  id_sexo INT NOT NULL,
  PRIMARY KEY (id, id_sexo),
  FOREIGN KEY (id_sexo) REFERENCES sexo (id)
);

CREATE TABLE tipo_participante (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE elenco (
  id INT NOT NULL,
  id_tipo_participante INT NOT NULL,
  id_participante INT NOT NULL,
  id_midia INT NOT NULL,
  PRIMARY KEY (id, id_tipo_participante, id_participante, id_midia),
  FOREIGN KEY (id_tipo_participante) REFERENCES tipo_participante (id),
  FOREIGN KEY (id_participante) REFERENCES participante (id),
  FOREIGN KEY (id_midia) REFERENCES midia (id)
);

CREATE TABLE categoria (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE subcategoria (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE genero (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS enquadramento_midia (
  id_midia INT NOT NULL,
  id_categoria INT NOT NULL,
  id_subcategoria INT NOT NULL,
  id_genero INT NOT NULL,
  PRIMARY KEY (id_midia, id_categoria, id_subcategoria, id_genero),
  FOREIGN KEY (id_midia) REFERENCES midia (id),
  FOREIGN KEY (id_categoria) REFERENCES categoria (id),
  FOREIGN KEY (id_subcategoria) REFERENCES subcategoria (id),
  FOREIGN KEY (id_genero) REFERENCES genero(id)
);