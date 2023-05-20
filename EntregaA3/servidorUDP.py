# -------------------
# Servidor Socket UDP
# -------------------

# importando a biblioteca
import socket



print("Eu sou o SERVIDOR UDP!")

# definindo ip e porta
HOST = 'localhost'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando


# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print("Aguardando cliente...")



while (True):
	print("-----")
	# cliente conectou - recuperando informações do cliente
	msg, enderecoCliente = servidor.recvfrom(9000)
	print(f"Cliente {enderecoCliente} enviou mensagem")
	mensagem = msg.decode("utf-8")
	print(f"Mensagem enviada pelo cliente: {mensagem}")
	print(f"Este servidor vai devolver a mensagem ao cliente {enderecoCliente}")
	resposta = "Resposta do servidor: " + mensagem
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
	if (mensagem == "adeus"):
		# Fim da conversa. Servidor vai encerrar.
		break

print("Encerrando o servidor...")
servidor.close()
