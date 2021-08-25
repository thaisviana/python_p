import socket
import psutil
import pickle
from random import randint
from CONSTANTS import PORTA, MENSAGEM_NUMERO, MENSAGEM_COR

def gera_cor_aleatoria(addr):
    id = addr[1]
    if id % 2 == 0:
        return f"({randint(0,255)}, {0}, {0})" #vermelho
    else:
        return f"({0}, {0}, {randint(0,255)})" #azul

def get_memory_and_cpu():
    resposta = {}
    resposta["cpu"] = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    resposta["mem_percent"] = round(mem.used/mem.total,3)
    return pickle.dumps(resposta)
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
    while msg_do_cliente != "fim":
        socket_cliente.send(get_memory_and_cpu())
        msg_do_cliente = socket_cliente.recv(1024)
        msg_do_cliente = msg_do_cliente.decode('utf-8')
    socket_cliente.close()