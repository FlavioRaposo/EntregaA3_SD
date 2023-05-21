def switch_case(argument):
    switcher = {
        1: "entrando como vendedor",
        2: "entrando como gerente"
    }
    return switcher.get(argument, "Opção inválida")


## interface de menu e resposta do gerente, user case

def menuGerente_principal():

    print("==================================")
    print("    Escolha a Opção desejada")
    print("==================================")
    print("1 - Emitir Pedido")
    print("2 - Fazer Consultas")
    print("3 - Mensagem para o vendedor")
    print("4 - Voltar")

    escolha = int(input("Digite sua opção > "))


def switch_case_menu_ger(argument):
    switcher = {
        1: "entrando emitir nota",
        2: "entrando em consultas",
        3: " entrando em mensagem",
        4: "entrando em voltar"
    }
    return switcher.get(argument, "Opção inválida")

resultado = switch_case_menu_ger(escolha)
print(resultado)
##########################################################


