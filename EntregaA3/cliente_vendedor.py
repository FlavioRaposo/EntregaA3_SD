
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
cliente2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = ('localhost', 9000)

print("Vou começar a mandar mensagens para o servidor.")

# Aqui começa a conversa
print("Entrando com mensagem de texto para enviar")
print("(Para sair digite 'fim')")
mensagem = input("Mensagem > ")

while (mensagem != "fim"):
	# Enviando mensagem ao servidor
	print("... Vou mandar uma mensagem para o servidor")
	cliente2.sendto(mensagem.encode("utf-8"), enderecoServidor)

	# Recebendo resposta do servidor
	msg, endereco = cliente2.recvfrom(9000)
	print("... O servidor me respondeu:", msg.decode("utf-8"))

	# Obtendo nova mensagem do usuário
	print("... Entrando com nova mensagem de texto para enviar")
	mensagem = input("Mensagem > ")

print("... Encerrando o cliente")
cliente2.close()
