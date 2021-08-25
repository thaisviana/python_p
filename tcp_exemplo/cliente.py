import socket
from time import sleep
from CONSTANTS import PORTA, MENSAGEM_COR, MENSAGEM_NUMERO
from random import choice

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(('0.0.0.0', PORTA))
    s.send(choice([MENSAGEM_COR, MENSAGEM_NUMERO]).encode("utf-8"))

    info_bytes = s.recv(1024)
    print(info_bytes.decode('ascii'))
    
    s.close()
except Exception as erro:
    print(str(erro))