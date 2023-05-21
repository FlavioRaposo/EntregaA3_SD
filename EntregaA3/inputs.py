## input de Vendedor
def input_emitir_pedido():
    print("==================================")
    print("    Emitir pedido de Venda")
    print("==================================")
    codigo_vendedor = input("Digite o código do vendedor: ")
    vendedor = input("Digite o nome do vendedor: ")
    polo_de_venda = input("Digite o polo de venda: ")
    data_de_venda = input("Digite a data de venda (dd/mm/aaaa): ")
    valor_de_venda = float(input("Digite o valor de venda: "))
    print("#########################################################")

    print("\nDados inseridos:")
    print("Código:", codigo_vendedor)
    print("Vendedor:", vendedor)
    print("Polo de venda:", polo_de_venda)
    print("Data de venda:", data_de_venda)
    print("Valor de venda:", "R$", valor_de_venda)


