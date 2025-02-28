PRAGMA foreign_keys = ON;

-- RELACIONAL
CREATE TABLE tb_cliente(
	idCliente INTEGER PRIMARY KEY,
	nomeCliente VARCHAR(100)
);


CREATE TABLE tb_cliente_endereco(
	idCliente INTEGER PRIMARY KEY REFERENCES tb_cliente(idCliente) ON DELETE CASCADE,
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR(40),
	paisCliente VARCHAR(40)

);


CREATE TABLE tb_vendedor(
	idVendedor INTEGER PRIMARY KEY,
	nomeVendedor VARCHAR(15),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(40)
);

CREATE TABLE tb_combustivel(
	idcombustivel INTEGER PRIMARY KEY,
	tipoCombustivel VARCHAR(20)
);

CREATE TABLE tb_carro(
	idCarro INTEGER PRIMARY KEY,
	kmCarro VARCHAR(45),
	chassiCarro VARCHAR(50),
	marcaCarro VARCHAR(80),
	modeloCarro VARCHAR(80),
	anoCarro INTEGER,
	idcombustivel INTEGER,
	FOREIGN KEY (idcombustivel) REFERENCES tb_combustivel(idcombustivel)
);

CREATE TABLE tb_locacaoR(
	idLocacao INTEGER PRIMARY KEY,
	idCarro INTEGER NOT NULL,
	idVendedor INTEGER NOT NULL,
	idCliente INTEGER NOT NULL,
	qtdDiaria INTEGER,
	vlrDiaria DECIMAL,
	dataLocacao DATE,
	horaLocacao TIME,
	dataEntrega DATE,
	horaEntrega TIME
);

INSERT INTO tb_cliente(idCliente,nomeCliente)
SELECT DISTINCT idCliente, nomeCliente FROM tb_locacao tl ;

INSERT INTO tb_combustivel(idcombustivel,tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel from tb_locacao tl;

INSERT INTO tb_carro(idCarro,kmCarro,chassiCarro,marcaCarro,modeloCarro,anoCarro,idcombustivel)
SELECT idCarro,kmCarro,classiCarro ,marcaCarro,modeloCarro,anoCarro,idcombustivel from tb_locacao tl GROUP BY idCarro;

INSERT INTO tb_vendedor(idVendedor,nomeVendedor,sexoVendedor ,estadoVendedor)
SELECT idVendedor,nomeVendedor,sexoVendedor,estadoVendedor FROM tb_locacao GROUP BY idVendedor;

INSERT INTO tb_cliente_endereco(idCliente,cidadeCliente,estadoCliente,paisCliente)
SELECT idCliente,cidadeCliente,estadoCliente ,paisCliente FROM tb_locacao GROUP BY idCliente,cidadeCliente,estadoCliente ;

INSERT INTO tb_locacaoR(idLocacao,idCarro,idVendedor,qtdDiaria,vlrDiaria,idCliente,dataEntrega,horaEntrega,dataLocacao,horaLocacao)
SELECT idLocacao,idCarro,idVendedor,qtdDiaria,vlrDiaria,idCliente,DATE(
    SUBSTR(CAST(dataLocacao as TEXT), 1, 4) || '-' ||  -- Ano
    SUBSTR(CAST(dataLocacao as TEXT) , 5, 2) || '-' ||  -- Mês
    SUBSTR(CAST(dataLocacao as TEXT), 7, 2)            -- Dia
) as dataLocacao,horaLocacao ,DATE(
    SUBSTR(CAST(dataEntrega as TEXT), 1, 4) || '-' ||  -- Ano
    SUBSTR(CAST(dataEntrega as TEXT) , 5, 2) || '-' ||  -- Mês
    SUBSTR(CAST(dataEntrega as TEXT), 7, 2)            -- Dia
) as dataEntrega ,horaEntrega FROM tb_locacao;


-- DIMENSIONAL
CREATE VIEW dim_carro AS
SELECT tca.*,tc.tipoCombustivel FROM tb_carro tca LEFT JOIN tb_combustivel tc ON tca.idcombustivel = tc.idcombustivel;

CREATE VIEW dim_tempo AS
SELECT * FROM tb_data_evento tde;

CREATE VIEW dim_vendedor AS
SELECT * FROM tb_vendedor tv ;

CREATE VIEW tf_locacao AS
SELECT idLocacao,idCarro,idVendedor,qtdDiaria,vlrDiaria FROM tb_locacaoR;

CREATE VIEW dim_cliente AS
SELECT * FROM tb_cliente tc LEFT JOIN tb_cliente_endereco tce ON tce.idCliente = tc.idCliente;


