import socket
import pickle
from time import sleep
from CONSTANTS import PORTA, MENSAGEM_COR, MENSAGEM_NUMERO
from random import choice

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(('0.0.0.0', PORTA))
    for i in range(5):
        s.send(choice([MENSAGEM_COR, MENSAGEM_NUMERO]).encode("ascii"))

        info_bytes = s.recv(1024)
        print(i, pickle.loads(info_bytes))
        sleep(1)
        
    s.send(b"fim")
    s.close()
except Exception as erro:
    print(str(erro))