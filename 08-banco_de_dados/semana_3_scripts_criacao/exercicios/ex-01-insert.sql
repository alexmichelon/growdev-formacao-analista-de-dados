USE ex_1;

SHOW TABLES;

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE login;
TRUNCATE TABLE cliente;
TRUNCATE TABLE endereco;
TRUNCATE TABLE tipo_endereco;
TRUNCATE TABLE marca;
TRUNCATE TABLE categoria;
TRUNCATE TABLE produto;
TRUNCATE TABLE brinde;
TRUNCATE TABLE compra;
TRUNCATE TABLE compra_brinde_cliente;
TRUNCATE TABLE entrega;
TRUNCATE TABLE item;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO login (usuario, senha, e_mail) VALUES ('alex', 'ABC123', 'alexmichelonn@gmail.com');
INSERT INTO login (usuario, senha, e_mail) VALUES ('josé', '123ABC123', 'jose@gmail.com');
INSERT INTO login (usuario, senha, e_mail) VALUES ('maria', '123456', 'maria@gmail.com');

INSERT INTO cliente (nome, cpf, sexo, data_nascimento, telefone_celular, telefone_fixo, id_login) VALUES ('Alex Michelon', '12345678912', 'M', '1986-08-16', '49999999999', NULL, 1);
INSERT INTO cliente (nome, cpf, sexo, data_nascimento, telefone_celular, telefone_fixo, id_login) VALUES ('Jose da Silva', '32165478999', 'M', '1970-01-02', '49999999998', NULL, 2);
INSERT INTO cliente (nome, cpf, sexo, data_nascimento, telefone_celular, telefone_fixo, id_login) VALUES ('Maria Silva Santos', '11122233399', 'F', '1992-11-15', '49999999789', '1132325645', 3);

INSERT INTO endereco (rua, numero, complemento, bairro, cep, cidade, uf) VALUES ('Rua Getúlio Vargas', '10', 'Casa', 'Centro', '88600000', 'São Joaquim', 'SC');
INSERT INTO endereco (rua, numero, complemento, bairro, cep, cidade, uf) VALUES ('Rua Expedicionário', '568', 'Apto', 'Santana', '89160000', 'Rio do Sul', 'SC');
INSERT INTO endereco (rua, numero, complemento, bairro, cep, cidade, uf) VALUES ('Rua Presidente Castelo', 'SN', 'Casa', 'Centro', '99000123', 'Porto Alegre', 'RS');

INSERT INTO tipo_endereco (id_endereco, id_cliente, descricao) VALUES (1, 1, 'Residencial');
INSERT INTO tipo_endereco (id_endereco, id_cliente, descricao) VALUES (2, 3, 'Residencial');
INSERT INTO tipo_endereco (id_endereco, id_cliente, descricao) VALUES (3, 2, 'Comercial');

INSERT INTO marca (descricao) VALUES ('IBM');
INSERT INTO marca (descricao) VALUES ('Dell');
INSERT INTO marca (descricao) VALUES ('JBL');
INSERT INTO marca (descricao) VALUES ('Microsoft');
INSERT INTO marca (descricao) VALUES ('Fortrek');
INSERT INTO marca (descricao) VALUES ('Bic');
INSERT INTO marca (descricao) VALUES ('Intelbras');

INSERT INTO categoria (descricao) VALUES ('Computador de Mesa');
INSERT INTO categoria (descricao) VALUES ('Notebook');
INSERT INTO categoria (descricao) VALUES ('Utensílios de Escritório');
INSERT INTO categoria (descricao) VALUES ('Mobiliário');
INSERT INTO categoria (descricao) VALUES ('Comunicação');

INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Telefone de mesa', 35, 3.50, 10, 7, 5);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Caneta', 0.75, 0.05, 1500, 6, 3);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Cadeira Gamer', 1200.00, 175, 5, 5, 4);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Fone de Ouvido', 245, 26, 10, 3, 5);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Computer', 5000, 250, 10, 1, 1);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('OptFlex', 7500, 300, 5, 2, 2);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Mouse sem Fio', 80, 25, 15, 4, 3);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Interfone', 350, 55, 10, 7, 5);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('Borracha', 3.50, 0.60, 100, 6, 3);
INSERT INTO produto (descricao, valor_custo, valor_imposto, quantidade_estoque, id_marca, id_categoria) VALUES ('BoomBox', 2500, 650, 3, 3, 5);

INSERT INTO brinde (valido, id_produto) VALUES ('S', 2);
INSERT INTO brinde (valido, id_produto) VALUES ('S', 9);
INSERT INTO brinde (valido, id_produto) VALUES ('N', 1);
INSERT INTO brinde (valido, id_produto) VALUES ('N', 7);

INSERT INTO compra (data, valor_imposto, valor_desconto, valor_total, id_cliente) VALUES ('2022-07-01 11:15:00', 0, 0, 1375, 1);
INSERT INTO compra (data, valor_imposto, valor_desconto, valor_total, id_cliente) VALUES ('2022-09-12 09:32:00', 0, 0, 8, 2);
INSERT INTO compra (data, valor_imposto, valor_desconto, valor_total, id_cliente) VALUES ('2023-01-01 22:36:00', 0, 0, 3150, 1);
INSERT INTO compra (data, valor_imposto, valor_desconto, valor_total, id_cliente) VALUES ('2023-01-05 22:36:00', 0, 0, 41, 1);

INSERT INTO compra_brinde_cliente (id_brinde, id_cliente, id_compra) VALUES (2, 1, 4);

INSERT INTO entrega (status, data, nome_entregador, nome_recebedor, cpf_recebedor, id_compra) VALUES ('S', '2022-07-02 13:30:00', 'Josias Cavalcante', 'Alex Michelon', '12345678912', 1);
INSERT INTO entrega (status, data, nome_entregador, nome_recebedor, cpf_recebedor, id_compra) VALUES ('S', '2022-09-22 17:23:00', 'Josias Cavalcante', NULL, NULL, 2);
INSERT INTO entrega (status, data, nome_entregador, nome_recebedor, cpf_recebedor, id_compra) VALUES ('S', '2023-01-03 09:05:00', 'Josias Cavalcante', 'Esposa', NULL, 3);
INSERT INTO entrega (status, data, nome_entregador, nome_recebedor, cpf_recebedor, id_compra) VALUES ('S', '2023-01-08 15:09:00', 'Josias Cavalcante', 'Alex Michelon', '12345678912', 4);

INSERT INTO item (id_produto, id_compra, quantidade, valor, is_brinde) VALUES (3, 1, 1, 1375, 'N');
INSERT INTO item (id_produto, id_compra, quantidade, valor, is_brinde) VALUES (2, 2, 10, 8, 'N');
INSERT INTO item (id_produto, id_compra, quantidade, valor, is_brinde) VALUES (10, 3, 1, 3150, 'N');
INSERT INTO item (id_produto, id_compra, quantidade, valor, is_brinde) VALUES (9, 4, 10, 41, 'S');