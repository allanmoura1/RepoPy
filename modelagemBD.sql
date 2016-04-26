CREATE TABLE chamados (
			id_chamado INT (5) PRIMARY KEY,
			classe_chamado VARCHAR(40),
			usuario_solicitante VARCHAR(40),
			func_alocado VARCHAR(40),
			setor_solicitante VARCHAR(80),
			desc_chamado VARCHAR(180),
			data_solicitacao VARCHAR(30)
)
