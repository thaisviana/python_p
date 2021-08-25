import socket
from CONSTANTS import PORTA, MSG_INCIO
from random import randint

HOST = socket.gethostbyname("")
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORTA)
msg = MSG_INCIO
udp.sendto(msg.encode('utf-8'), dest)
pontos = -1
while pontos <= -1:
    (msg, servidor) = udp.recvfrom(1024)
    msg = msg.decode('utf-8')
    print(msg)
    respota = f"{randint(1,4)}"
    udp.sendto (respota.encode('utf-8'), dest)
    if "PONTOS" in  msg:
        pontuacao = msg.split(" ")[0]
        pontos = int(pontuacao)
print("Você fez", pontos, "pontos")
udp.close()