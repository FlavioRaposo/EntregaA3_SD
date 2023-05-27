import socket

# Função que será chamada remotamente
def conect_server():
    return "Servidor conectado com sucesso"


# Configurações do servidor UDP
host = 'localhost'  # Endereço IP do servidor
port = 9000  # Porta do servidor

# Criação do socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print(f"Servidor UDP aguardando conexões em {host}:{port}")

# Loop infinito para receber e processar requisições
while True:
    data, address = sock.recvfrom(1024)
    print(f"Requisição recebida de {address[0]}:{address[1]}")

    # Chamada da função e obtenção do resultado
    resultado = conect_server()
  # Envio do resultado de volta para o cliente
    sock.sendto(resultado.encode(), address)

