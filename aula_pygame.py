import pygame
from random import randrange
from time import sleep

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)

LARANJA = (246,130,0)

centro_largura_boneco = 400
centro_altura_boneco = 300
cor = (randrange(255),randrange(255),randrange(255))

def desenha_chapeu(altura_centro_cara_boneco):
    pygame.draw.rect(tela, PRETO, (centro_largura_boneco-30,altura_centro_cara_boneco-15,60, 8), 0)
    pygame.draw.rect(tela, PRETO, (centro_largura_boneco-25,altura_centro_cara_boneco-60,50, 50), 0)

tela.fill(cor)
terminou = False
while not terminou:
    pygame.draw.line(tela, PRETO,(centro_largura_boneco-40,centro_altura_boneco),(centro_largura_boneco-90,centro_altura_boneco-50), 8)
    pygame.draw.line(tela, PRETO,(centro_largura_boneco+30,centro_altura_boneco),(centro_largura_boneco+80,centro_altura_boneco-50), 8)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,centro_altura_boneco-60), 30)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,centro_altura_boneco), 40)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,centro_altura_boneco+90), 80)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,centro_altura_boneco-14), 6)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,centro_altura_boneco+10), 6)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,centro_altura_boneco+30), 6)
    pygame.draw.polygon(tela, LARANJA, [[centro_largura_boneco, centro_altura_boneco-55], 
                                        [centro_largura_boneco-15, centro_altura_boneco-55], 
                                        [centro_largura_boneco, centro_altura_boneco-60]], 0)
    desenha_chapeu(centro_altura_boneco-70)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                centro_largura_boneco -= 5
            if event.key == ord('d'):
                centro_largura_boneco += 5
            if event.key == ord('w'):
                centro_altura_boneco -= 5
            if event.key == ord('s'):
                centro_altura_boneco += 5
    tela.fill(cor)

pygame.display.quit()
pygame.quit()