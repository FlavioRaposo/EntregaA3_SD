## falta colocar while em alguns menu com switch

from Emitir_pedido import input_emitir_pedido

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

def emitir_pedidos():
    input_emitir_pedido()
    respostasn = ""

    while respostasn.lower() != "sim" and respostasn.lower() != "não":

        respostasn = input("Deseja emitir outro pedido?")

        if respostasn.lower() == "sim":
            emitir_pedidos()
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


### def tot_venda_vendedor():
### def tot_venda_filial():
### def tot_venda_periodo():
### def melhor_loja():
### def melhor_vendedor():

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
