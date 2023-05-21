## criar tabela de log para registros de entrada no sistema, caso ele escolha
## uma opçao o na tela de boas vinda vai enviar codigo do vendedor e data de acesso

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

def consultar_dados():
    # Conectando ao banco de dados
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    # Realizando a consulta na tabela
    cursor.execute('SELECT * FROM vendas')

    # Obtendo os resultados da consulta
    dados_vendas = cursor.fetchall()

    # Exibindo os resultados
    print("ID\tVendedor\tTotal de Vendas")
    print("--------------------------------")
    for venda in dados_vendas:
        print(f"{venda[0]}\t{venda[1]}\t\t{venda[2]}")

    # Fechando a conexão com o banco de dados
    conn.close()

def apagar_dados():
    # Conectando ao banco de dados
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    # Solicitando o ID do item a ser removido
    id_item = int(input("Digite o ID do item a ser removido: "))

    # Executando a consulta para apagar o item
    cursor.execute('DELETE FROM vendas WHERE id = ?', (id_item,))

    # Verificando se algum item foi removido
    if cursor.rowcount > 0:
        print("Item removido com sucesso.")
    else:
        print("Nenhum item encontrado com o ID informado.")

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

def consultar_tables():
    # Conectando ao banco de dados
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()

    # Executando a consulta para obter a lista de tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

    # Recuperando os resultados da consulta
    tabelas = cursor.fetchall()

    # Exibindo o nome das tabelas
    print("Tabelas existentes:")
    for tabela in tabelas:
        print(tabela[0])

    # Fechando a conexão com o banco de dados
    conn.close()

def soma_tabela():
    # Conectando ao banco de dados
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    # Executando a consulta para somar os valores
    cursor.execute('SELECT SUM(valor) FROM tabela')

    # Recuperando o resultado da consulta
    total = cursor.fetchone()[0]

    # Exibindo o resultado
    print("Total:", total)

    # Fechando a conexão com o banco de dados
    conn.close()













