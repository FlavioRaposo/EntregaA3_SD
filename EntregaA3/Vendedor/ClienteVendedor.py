import sys

def vendedor_menu_princ():
    print("==================================")
    print("   Bem-vindo(a) à loja Marabrás!  ")
    print("==================================")
    print("          Menu Vendedor           ")
    print("==================================")
    print("    Escolha a Opção desejada")
    print("==================================")
    print("1 - Emitir Pedido")
    print("2 - Meu controle de vendas")
    print("3 - Mensagem para o Gerente")
    print("4 - Voltar")

    Gprinc_escolha = int(input("Digite sua opção > \n"))
    valor = Gprinc_escolha
    if valor == 1:
        menu_emitir_pedidos()
    elif valor == 2:
        menu_consultas()
    elif valor == 3:
        print("Executando case 3")
    elif valor == 4:
        sys.exit()
    else:
        print("Executando caso padrão")


def controle_vendas(codigo_op):
   # Conectando ao banco de dados
    conexao = sqlite3.connect('emitir_nota.db')
    cursor = conexao.cursor()

    # Realizando a consulta na tabela


    cursor.execute("SELECT * FROM vendas WHERE codigo_op = ?", (codigo_op,))

    # Obtendo os resultados da consulta
    dados_vendas = cursor.fetchall()


    conexao.close()


    # Exibindo os resultados



    print("Codigo OP\t\tVendedor\t\tValor de vendas")
    print("-----------------------------------------")
    for venda in dados_vendas:
        resultado = venda
        tupla = (resultado[1],resultado[2],resultado[5])

        resultadof = f'{tupla[0]:<15} {tupla[1]:<15} {tupla[2]:<17}'

        print(resultadof)

        print("o resultado de suas venda é de ")


print("====================================")
print("     Meu Controle de Vendas         ")
print("====================================")
insert_cod = int(input("digite seu codigo operacional\n"))
controle_vendas(insert_cod)

