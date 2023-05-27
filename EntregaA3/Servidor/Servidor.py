import threading
import socket

clientes = []

def main():
    host = 'localhost'  # Endereço IP do servidor
    port = 9000

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        server.bind((host, port))
        server.listen(10)
        print('\n Servidor Conectado com sucesso\n')
    except:
        return print('\n Não foi possivel iniciar o servidor:\n')
    
    while True:
        cliente, addr = server.accept()
        clientes.append(cliente)
        
        thread1 = threading.Thread(target=mensagem_tratada, args=[cliente])
        thread1.start()
        
def mensagem_tratada(cliente):
    while True:
        try:
            msg,address = cliente.recv(2048)
            broadcast(msg,cliente)
        except:
            deleteCliente(cliente)
            break
        
def broadcast(msg,cliente):
    for clientesItem in clientes:
        if clientesItem != cliente:
            try:
                clientesItem.send(msg)
            except:
                deleteCliente(clientesItem)
                break

def deleteCliente(cliente):
    clientes.remove(cliente)
    
main()

