from MenuGerente import geren_principal
import socket
# ------------------
# Cliente Socket UDP
# ------------------

print("Eu sou um CLIENTE vendedor")




# Definindo ip e porta
HOST = 'localhost'  # Endereco IP do Servidor
PORT = 9002

	# Criar um socket UDP
cliente_Vendedor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_Vendedor.bind((HOST, PORT))

while True:
	# Enviar mensagem para o cliente 2
	print("... Entrando com nova mensagem de texto para gerente")
	mensagem = input("digite sua mensagem aqui.")
	cliente_Vendedor.sendto(mensagem.encode(), ('localhost', 9003))

	# Receber resposta do cliente 2
	dados, endereco = cliente_Vendedor.recvfrom(9003)
	resposta = dados.decode()
	print("Resposta do gerente:", resposta)
	if mensagem == "sair":
		cliente_Vendedor.close()
		geren_principal()

	# Fechar o socket



