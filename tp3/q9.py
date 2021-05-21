#Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro 
# no centro da tela. (código e printscreen)
import pygame

pygame.init()
largura_tela, altura_tela = 500, 500
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO, AZUL = (255, 0, 0), (0,0,255)
tela.fill(PRETO)

def escreve_texto(texto):
    font = pygame.font.Font(None, 24)
    text = font.render(texto, 1, BRANCO)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)


terminou = False
while not terminou:
    tela.fill(PRETO)
    pygame.draw.circle(tela, AZUL, (largura_tela/2,altura_tela/2), 100)
    escreve_texto("q9 - tp3")
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()
pygame.quit()

