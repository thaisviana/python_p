import socket
from random import randint
from CONSTANTS import PORTA, MENSAGEM_NUMERO, MENSAGEM_COR

def gera_cor_aleatoria(addr):
    id = addr[1]
    if id % 2 == 0:
        return f"({randint(0,255)}, {0}, {0})" #vermelho
    else:
        return f"({0}, {0}, {randint(0,255)})" #azul

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("")
socket_servidor.bind((host, PORTA))

socket_servidor.listen()

print("Servidor de nome", host, "esperando conexão na porta", PORTA)
while True:
    (socket_cliente,addr) = socket_servidor.accept()
    print("Conectado a:", str(addr))

    msg_do_cliente = socket_cliente.recv(1024)
    msg_do_cliente = msg_do_cliente.decode('utf-8')
    if msg_do_cliente == MENSAGEM_COR:
        socket_cliente.send(gera_cor_aleatoria(addr).encode('utf-8'))
    elif msg_do_cliente == MENSAGEM_NUMERO:
        socket_cliente.send(f"{randint(0,10)}".encode('utf-8'))
    else:
        socket_cliente.send("Hei, não entendi".encode('utf-8'))
    socket_cliente.close()