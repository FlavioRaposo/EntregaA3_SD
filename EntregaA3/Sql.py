import sqlite3

# Conecta ao banco de dados SQLite (se o arquivo não existir, ele será criado)
conexao = sqlite3.connect('lojao.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela "vendas"
cursor.execute("CREATE TABLE vendas (id INTEGER PRIMARY KEY,codigo_op INTEGER,vendedor TEXT,polo_de_venda TEXT,data_de_venda DATE,valor_de_venda REAL)")

# Confirma as alterações no banco de dados
conexao.commit()

# Fecha a conexão
conexao.close()







