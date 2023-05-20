from servidorUDP import switch_case


def exibir_tela_boas_vindas():
    print("==================================")
    print(" Bem-vindo(a) à loja Marabrás!")
    print("==================================")
    print("")
    print("Iniciando as aplicações...")
    print("Comunicando com o servidor")
#Cliente conectando ao Servidor



 

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



   