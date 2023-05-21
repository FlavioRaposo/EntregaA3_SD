from MenuGerente import geren_principal
import socket
# ------------------
# Cliente Socket UDP
# ------------------

print("Eu sou um CLIENTE gerente")


# Definindo ip e porta
HOST = 'localhost'  # Endereco IP do Servidor
PORT = 9003

	# Criar um socket UDP
cliente_gerente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_gerente.bind((HOST, PORT))

while True:
	# Enviar mensagem para o cliente 2
	print("... Entrando com nova mensagem de texto para vendedor")
	mensagem = input("digite sua mensagem aqui.")
	cliente_gerente.sendto(mensagem.encode(), ('localhost', 9002))

	# Receber resposta do cliente 2
	dados, endereco = cliente_gerente.recvfrom(9002)
	resposta = dados.decode()
	print("Resposta do vendedor:", resposta)
	if mensagem == "sair":
		cliente_gerente.close()
		geren_principal()
	# Fechar o socket



