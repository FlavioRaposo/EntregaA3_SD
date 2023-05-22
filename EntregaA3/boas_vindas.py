# ------------------
# Cliente Socket UDP
# ------------------

print("Eu sou um CLIENTE UDP!")

# Importando a biblioteca'
import socket

# Definindo ip e porta
HOST = 'localhost'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor estará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = ('localhost', 9000)

iniciando_conexao = "Iniciando conexão"
cliente.sendto(iniciando_conexao.encode("utf-8"), enderecoServidor)

#while (iniciando_conexao != "fim"):
	# Enviando mensagem ao servidor
#	print("... Vou mandar uma mensagem para o servidor")
#	cliente.sendto(iniciando_conexao.encode("utf-8"), enderecoServidor)

	# Recebendo resposta do servidor
#	msg, endereco = cliente.recvfrom(9000)
##	print("... O servidor me respondeu:", msg.decode("utf-8"))

	# Obtendo nova mensagem do usuário
#	print("... Entrando com nova mensagem de texto para enviar")
#	mensagem = input("Mensagem > ")

#print("... Encerrando o cliente")
#cliente.close()

def exibir_tela_boas_vindas():
    print("==================================")
    print(" Bem-vindo(a) à loja Marabrás!")
    print("==================================")
    print("")
    print("Iniciando as aplicações...")
    iniciando_conexao = ("Iniciando conexão")
    cliente.sendto(iniciando_conexao.encode("utf-8"), enderecoServidor)
    msg, endereco = cliente.recvfrom(9000)
    print( msg.decode("utf-8"))
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


