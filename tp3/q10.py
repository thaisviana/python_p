#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado 
# no centro da tela. O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. 
# Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado. (código e printscreen)
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

x,y= largura_tela/2-largura_quadrado, altura_tela/2-altura_quadrado
teclas = Teclas(False, False, False, False)

def desenha_quadrado_vermelho(x,y):
    cor = VERMELHO
    pygame.draw.rect(tela, cor, (x,y,largura_quadrado, altura_quadrado), 0)

def move_quadrado(teclas, x,y):
    if teclas.w and y > 0:
        y -= 1
    elif teclas.s and y < altura_tela-30:
        y += 1
    if teclas.a and x > 0:
        x -= 1
    elif teclas.d and x < largura_tela-30:
        x += 1
    return x,y

def escreve_texto(texto):
    font = pygame.font.Font(None, 24)
    text = font.render(texto, 1, BRANCO)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

terminou = False
while not terminou:
    tela.fill(PRETO)
    escreve_texto("q10 - tp3")
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
    x,y = move_quadrado(teclas,x,y)
    desenha_quadrado_vermelho(x,y)
    pygame.display.update() 

pygame.display.quit()
pygame.quit()

