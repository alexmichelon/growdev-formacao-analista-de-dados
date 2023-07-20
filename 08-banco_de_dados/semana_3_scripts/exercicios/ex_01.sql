DROP SCHEMA IF EXISTS ex_1;

CREATE SCHEMA IF NOT EXISTS ex_1;

USE ex_1;

CREATE TABLE login (
  id INT NOT NULL AUTO_INCREMENT,
  usuario VARCHAR(45) NOT NULL,
  senha VARCHAR(30) NOT NULL,
  e_mail VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE cliente (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  sexo CHAR(1) NOT NULL,
  data_nascimento DATE NOT NULL,
  telefone_celular VARCHAR(14) NOT NULL,
  telefone_fixo VARCHAR(12) NULL,
  id_login INT NOT NULL,
  PRIMARY KEY (id, id_login),
  FOREIGN KEY (id_login) REFERENCES login (id)
);

CREATE TABLE endereco (
  id INT NOT NULL AUTO_INCREMENT,
  rua VARCHAR(100) NOT NULL,
  numero VARCHAR(5) NOT NULL,
  complemento VARCHAR(15) NULL,
  bairro VARCHAR(20) NOT NULL,
  cep VARCHAR(8) NOT NULL,
  cidade VARCHAR(25) NOT NULL,
  uf CHAR(2) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE tipo_endereco (
  id_endereco INT NOT NULL,
  id_cliente INT NOT NULL,
  descricao VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_endereco, id_cliente),
  FOREIGN KEY (id_endereco) REFERENCES endereco (id),
  FOREIGN KEY (id_cliente) REFERENCES cliente (id)
);

CREATE TABLE marca (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE categoria (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE produto (
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(45) NOT NULL,
  valor_custo DOUBLE NOT NULL,
  valor_imposto VARCHAR(45) NOT NULL,
  quantidade_estoque DOUBLE NOT NULL,
  id_marca INT NOT NULL,
  id_categoria INT NOT NULL,
  PRIMARY KEY (id, id_marca, id_categoria),
  FOREIGN KEY (id_marca) REFERENCES marca (id),
  FOREIGN KEY (id_categoria) REFERENCES categoria (id)
);

CREATE TABLE brinde (
  id INT NOT NULL AUTO_INCREMENT,
  valido VARCHAR(45) BINARY NOT NULL,
  id_produto INT NOT NULL,
  PRIMARY KEY (id, id_produto),
  FOREIGN KEY (id_produto) REFERENCES produto (id)
);

CREATE TABLE compra (
  id INT NOT NULL AUTO_INCREMENT,
  data DATETIME(6) NOT NULL,
  valor_imposto DOUBLE NOT NULL,
  valor_desconto DOUBLE NOT NULL,
  valor_total DOUBLE NOT NULL,
  id_cliente INT NOT NULL,
  PRIMARY KEY (id, id_cliente),
  FOREIGN KEY (id_cliente) REFERENCES cliente (id)
);

CREATE TABLE compra_brinde_cliente (
  id_brinde INT NOT NULL,
  id_cliente INT NOT NULL,
  id_compra INT NOT NULL,
  PRIMARY KEY (id_brinde, id_cliente, id_compra),
  FOREIGN KEY (id_brinde) REFERENCES brinde (id),
  FOREIGN KEY (id_cliente) REFERENCES cliente (id),  
  FOREIGN KEY (id_compra) REFERENCES compra (id)
);

CREATE TABLE entrega (
  id INT NOT NULL AUTO_INCREMENT,
  status VARCHAR(45) BINARY NOT NULL,
  data DATETIME(6) NOT NULL,
  nome_entregador VARCHAR(45) NOT NULL,
  nome_recebedor VARCHAR(45) NULL,
  cpf_recebedor VARCHAR(11) NULL,
  id_compra INT NOT NULL,
  PRIMARY KEY (id, id_compra),
  FOREIGN KEY (id_compra) REFERENCES compra (id)
);

CREATE TABLE item (
  id_produto INT NOT NULL,
  id_compra INT NOT NULL,
  quantidade DOUBLE NOT NULL,
  valor FLOAT NOT NULL,
  is_brinde CHAR(1) BINARY NOT NULL,
  PRIMARY KEY (id_produto, id_compra),
  FOREIGN KEY (id_produto) REFERENCES produto (id),
  FOREIGN KEY (id_compra) REFERENCES compra (id)
);