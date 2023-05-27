import sqlite3
from Emitir_pedido import input_emitir_pedido
import sys

def geren_principal():

        print("==================================")
        print("   Bem-vindo(a) à loja Marabrás!  ")
        print("==================================")
        print("          Menu Gerente            ")
        print("==================================")
        print("    Escolha a Opção desejada")
        print("==================================")
        print("1 - Emitir Pedido")
        print("2 - Fazer Consultas")
        print("3 - Mensagem para o vendedor")
        print("4 - Sair")

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


geren_principal()

def menu_emitir_pedidos():
    input_emitir_pedido()
    respostasn = ""

    while respostasn.lower() != "sim" and respostasn.lower() != "não":

        respostasn = input("Deseja emitir outro pedido?")

        if respostasn.lower() == "sim":
            menu_emitir_pedidos()
        elif respostasn.lower() == "não":
            print("resposta do servidor aperte enter para voltar")

        else:
            print("Por favor, responda com 'sim' ou 'não'.")


def menu_consultas():
    print("==================================")
    print("    Escolha a consulta desejada")
    print("==================================")
    print("1 - Total de vendas por vendedor")
    print("2 - Total de vendas por filial")
    print("3 - Total de vendas por período")
    print("4 - Melhor loja acumulada")
    print("5 - Melhor Vendedor acumulado")
    print("6 - Voltar")

    Mconsu_escolha = int(input("Digite sua opção abaixo\n"))
    valor = Mconsu_escolha
    if valor == 1:
        tot_venda_vendedor()
    elif valor == 2:
        tot_venda_filial()
    elif valor == 3:
        tot_venda_periodo()
    elif valor == 4:
        tot_melhor_loja()
    elif valor == 5:
        pass
    elif valor == 6:
        geren_principal()
    else:
        print("Executando caso padrão")


def tot_venda_vendedor(vendedor):
    conexao = sqlite3.connect('emitir_nota.db')
    cursor = conexao.cursor()

        # Executar consulta SQL para somar as vendas do vendedor especificado
    cursor.execute("SELECT SUM(valor_de_venda) FROM vendas WHERE vendedor = ?", (vendedor,))

    total_vendas = cursor.fetchone()[0]

    conexao.close()

    return total_vendas

    # Chamar a soma das vendas de um vendedor específico
print("======================================")
print("     Total de vendas por vendedor     ")
print("======================================")
vendedor = input("Digite o nome do vendedor: \n")
total_vendas = tot_venda_vendedor(vendedor)

print("===================================+++++===")
print("Total de vendas do ", vendedor, " é de: R$", "%.2f"%total_vendas)
print("====================================+++++==")


def tot_venda_filial(polo_de_venda):
    conexao = sqlite3.connect('emitir_nota.db')
    cursor = conexao.cursor()

        # Executar consulta SQL para somar as vendas do vendedor especificado
    cursor.execute("SELECT SUM(valor_de_venda) FROM vendas WHERE polo_de_venda = ?", (polo_de_venda,))

    total_vendas_filial = cursor.fetchone()[0]

    conexao.close()

    return total_vendas_filial

# Chamar a soma das vendas de um vendedor específico
print("======================================")
print("     Total de vendas por filial       ")
print("======================================")
print("Salvador - Lauro de Freitas - Camaçari")
print("======================================")

polo_de_venda = input("Digite o nome do Polo de venda: \n")
total_vendas_filial = tot_venda_filial(polo_de_venda)

print("===================================+++++===")
print(f"Total de vendas da filial", polo_de_venda , " é de: R$","%.2f"%total_vendas)
print("====================================+++++==")



### CORRIGIR FUNCAO
def tot_venda_periodo(data_inicial,data_final):
    conexao = sqlite3.connect('emitir_nota.db')
    cursor = conexao.cursor()

        # Executar consulta SQL para somar as vendas do vendedor especificado
    cursor.execute("SELECT * FROM vendas WHERE data_de_venda BETWEEN ? AND  ?", (data_inicial, data_final))

    vendas_periodo = cursor.fetchone()

    for linha in vendas_periodo:
        print(linha)

    conexao.close()
# Chamar a soma das vendas de um vendedor específico
    print("======================================")
    print("     Total de vendas por Periodo       ")
    print("======================================")

    data_inicial = input("Digite a data inicial: \n")
    data_final = input("Digite a data final: \n")

    tot_venda_periodo(data_inicial,data_final)

    print("===================================+++++===")
    print(f"Total de vendas da data de ",data_inicial," até ",data_final," é de: R$")
    print("====================================+++++==")


def tot_melhor_loja():
    def loja_sal():
        conexao = sqlite3.connect('emitir_nota.db')
        cursor = conexao.cursor()
        loja_um = 'salvador'
        # Executar consulta SQL para somar as vendas do vendedor especificado
        cursor.execute("SELECT SUM(valor_de_venda) FROM vendas WHERE polo_de_venda = ?",(loja_um,))
        salvador_soma = cursor.fetchone()[0]
        return salvador_soma
        conexao.close()

    def loja_lau():
        conexao = sqlite3.connect('emitir_nota.db')
        cursor = conexao.cursor()
        loja_dois = 'lauro de freitas'
        cursor.execute("SELECT SUM(valor_de_venda) FROM vendas WHERE polo_de_venda = ?", (loja_dois,))
        lauro_soma = cursor.fetchone()[0]
        return lauro_soma
        conexao.close()

    def loja_cam():
        conexao = sqlite3.connect('emitir_nota.db')
        cursor = conexao.cursor()
        loja_tres = 'camaçari'
        cursor.execute("SELECT SUM(valor_de_venda) FROM vendas WHERE polo_de_venda = ?", (loja_tres,))
        camacari_soma = cursor.fetchone()[0]
        return camacari_soma
        conexao.close()

    salvador_soma = loja_sal()
    lauro_soma = loja_lau()
    camacari_soma = loja_cam()

       # Verificando qual é o maior
    if salvador_soma >= lauro_soma and salvador_soma >= camacari_soma:
        print("Salvador é a lider de vendas com R$ ",salvador_soma)
    elif lauro_soma >= salvador_soma and lauro_soma >= camacari_soma:
        print("Lauro de Freitas é a lider de vendas com R$ ",lauro_soma)
    else:
        print("Camaçari é a lider de vendas com R$ ",camacari_soma)


    input("Aperte zero para voltar\n")

    # voltar para def menu_consultas():

tot_melhor_loja()