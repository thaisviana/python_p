import socket
from CONSTANTS import PORTA, MSG_INCIO, PERGUNTAS

pontos = 0

def envia_pergunta(udp, chave, valor, cliente):
    nl = '\n'
    pergunta = f"{chave}) {valor['pergunta']}{nl}{nl.join(valor['opcoes'])}"
    udp.sendto(pergunta.encode('utf-8'), cliente)

def recebe_reposta():
    (resposta, cliente) = udp.recvfrom(1024)
    return int(resposta.decode('utf-8'))

def calcula_pontuacao(valor, resposta, pontos):
    if resposta == valor['resposta']:
            pontos +=1
    return pontos

udp = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostbyname("")
udp.bind((host, PORTA))
print('Esperando receber na porta', PORTA, '...')
(msg, cliente) = udp.recvfrom(1024)
msg = msg.decode('utf-8')
if msg == MSG_INCIO:
    for chave, valor in PERGUNTAS.items():
        envia_pergunta(udp, chave, valor, cliente)
        resposta = recebe_reposta()
        print(chave, resposta)
        pontos = calcula_pontuacao(valor, resposta, pontos)   

udp.sendto(f"{pontos} PONTOS ".encode('utf-8'), cliente)
udp.close()