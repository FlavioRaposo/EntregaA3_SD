
def exibir_tela_boas_vindas():
    print("==================================")
    print(" Bem-vindo(a) à loja Marabrás!")
    print("==================================")
    print("")
    print("Iniciando as aplicações...")
    print("Comunicando com o servidor")
#Cliente conectando ao Servidor

def switch_case(argument):
    switcher = {
        1: "entrando como vendedor",
        2: "entrando como gerente"
    }
    return switcher.get(argument, "Opção inválida")

 

def menu_Principal():
    print("==================================")
    print(" Escolha a opção desejada")
    print("==================================")
    print("Opção 1 - Entrar como Vendedor")
    print("Opção 2 - Entrar como Gerente")
    print("") 

def comunicacaoServidor():
     print("Comunicação estabelecida com servidor")   
    
exibir_tela_boas_vindas()
menu_Principal()

respostaMenuServidor = int(input("Digite sua opção > "))
resultado = switch_case(respostaMenuServidor)
print(resultado)


