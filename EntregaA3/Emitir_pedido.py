## input de Vendedor
import sqlite3

def input_emitir_pedido(codigo_vendedor,vendedor,polo_de_venda,data_de_venda,valor_de_venda):
    try:
        conexao = sqlite3.connect('emitir_nota.db')
        cursor = conexao.cursor()
        # Inserir dados na tabela
        cursor.execute(
        "INSERT INTO vendas (codigo_op, vendedor, polo_de_venda, data_de_venda, valor_de_venda) VALUES (?, ?, ?, ?, ?)",
        (codigo_vendedor, vendedor, polo_de_venda, data_de_venda, valor_de_venda))

        # Confirma as alterações no banco de dados
        conexao.commit()
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as error:
        print("Erro ao inserir dados:", error)

    finally:
        if conexao:
            conexao.close()

print("==================================")
print("    Emitir pedido de Venda")
print("==================================")
codigo_vendedor = input("Digite o código do vendedor: ")
vendedor = input("Digite o nome do vendedor: ")
polo_de_venda = input("Digite o polo de venda: ")
data_de_venda = input("Digite a data de venda (dd/mm/aaaa): ")
valor_de_venda = float(input("Digite o valor de venda: "))
print("#########################################################")

input_emitir_pedido(codigo_vendedor,vendedor,polo_de_venda,data_de_venda,valor_de_venda)

