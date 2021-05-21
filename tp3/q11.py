#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro 
# no centro da tela que se move da esquerda para a direita. Sempre que chegar na extremidade direita, o círculo deve voltar 
# à extremidade esquerda, retomando o movimento da esquerda para a direita.

import pygame
from pygame.locals import *

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL = (255, 0, 0), (0,0,255)
tela.fill(PRETO)
largura_quadrado,altura_quadrado = 30,30

class Teclas:
    def __init__(self, w,a,s,d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d

x,y= largura_tela/2, altura_tela/2
teclas = Teclas(False, False, False, False)

def desenha_circulo_azul(x,y):
    cor = AZUL
    pygame.draw.circle(tela, AZUL, (x,y), 50)

def movimenta_elemento(teclas, x,y):
    if teclas.w and y > 0:
        y -= 2
    elif teclas.s and y < altura_tela:
        y += 2
    if teclas.a and x > 0:
        x -= 2
    elif teclas.d and x < largura_tela:
        x += 2
    return x,y

def escreve_texto(texto):
    font = pygame.font.Font(None, 24)
    text = font.render(texto, 1, BRANCO)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("q11 - tp3")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        # Enquanto estiver pressionado, o coelho vai se mexer
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                teclas.w = True
            elif event.key == K_a:
                teclas.a = True
            elif event.key == K_s:
                teclas.s = True
            elif event.key == K_d:
                teclas.d = True    
        #No momento que parou de pressionar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                teclas.w = False
            elif event.key == pygame.K_a:
                teclas.a = False
            elif event.key == pygame.K_s:
                teclas.s = False
            elif event.key == pygame.K_d:
                teclas.d = False
    x,y = movimenta_elemento(teclas,x,y)
    desenha_circulo_azul(x,y)
    pygame.display.update() 

pygame.display.quit()
pygame.quit()

