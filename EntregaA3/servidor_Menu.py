def switch_case(argument):
    switcher = {
        1: "entrando como vendedor",
        2: "entrando como gerente"
    }
    return switcher.get(argument, "Opção inválida")