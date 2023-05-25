## falta colocar while em alguns menu com switch
import sqlite3


def geren_principal():
    print("==================================")
    print("          Menu Gerente            ")
    print("==================================")
    print("    Escolha a Opção desejada")
    print("==================================")
    print("1 - Emitir Pedido")
    print("2 - Fazer Consultas")
    print("3 - Mensagem para o vendedor")
    print("4 - Voltar")

    Gprinc_escolha = int(input("Digite sua opção > "))

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

    Mconsu_escolha = int(input("Digite sua opção > "))


##### espaço para defs que vao contribir com as consulta no servidor


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



### def tot_venda_periodo():
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

### def melhor_loja():
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

### def melhor_vendedor():
## vou criar uma tabel a chamada 

######

## def msg_vendedor():

#### inicio do menu Vendedor

def vendedor_menu_princ():
    print("==================================")
    print("          Menu Vendedor            ")
    print("==================================")
    print("    Escolha a Opção desejada")
    print("==================================")
    print("1 - Emitir Pedido")
    print("2 - Meu controle de vendas")
    print("3 - Mensagem para o Gerente")
    print("4 - Voltar")

    Gprinc_escolha = int(input("Digite sua opção > "))

### def controle_vendas():
