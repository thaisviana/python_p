import pygame
from random import randint
from time import sleep

pygame.init()
largura_tela, altura_tela = 500, 500
tela = pygame.display.set_mode((largura_tela, altura_tela))

BRANCO, PRETO = (255,255,255), (0,0,0)
VERMELHO = (255,0,0)
LARANJA = (246,130,0)
tela.fill((2,183,255))

centro_largura_boneco = largura_tela/2
centro_altura_boneco = 200
centro_altura_rosto_boneco = centro_altura_boneco - 60

def desenha_quadrado_cor_randomica():
    largura_quadrado,altura_quadrado = 30,30
    cor = (randint(0,255),randint(0,255),randint(0,255))
    x,y = randint(0,altura_tela-altura_quadrado),randint(0,largura_tela-largura_quadrado)
    pygame.draw.rect(tela, cor, (x,y,largura_quadrado, altura_quadrado), 0)

def desenha_botoes(tamanho):
    pygame.draw.circle(tela,VERMELHO , (centro_largura_boneco,centro_altura_boneco), tamanho)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,centro_altura_boneco+22), tamanho)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,centro_altura_boneco+44), tamanho)

def desenha_corpo(raio_principal):
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,centro_altura_boneco-raio_principal-20), raio_principal-10)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,centro_altura_boneco), raio_principal)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,centro_altura_boneco+(2*raio_principal+10)), 2*raio_principal)

def desenha_chapeu(tamanho_chapeu):
    pygame.draw.rect(tela, PRETO, (centro_largura_boneco-30,centro_altura_rosto_boneco-30,tamanho_chapeu+20, 10), 0)
    pygame.draw.rect(tela, PRETO, (centro_largura_boneco-20,centro_altura_rosto_boneco-70,tamanho_chapeu, tamanho_chapeu), 0)

def desenha_bracos(delta_braco):
    altura_mao = centro_altura_boneco-60
    pygame.draw.circle(tela, PRETO, (centro_largura_boneco-delta_braco,altura_mao), 10)
    pygame.draw.circle(tela, PRETO, (centro_largura_boneco+delta_braco,altura_mao), 10)
    pygame.draw.line(tela, PRETO,(centro_largura_boneco+delta_braco/2,centro_altura_boneco+10),(centro_largura_boneco+delta_braco,altura_mao), 10)
    pygame.draw.line(tela, PRETO,(centro_largura_boneco-delta_braco/2,centro_altura_boneco+10),(centro_largura_boneco-delta_braco,altura_mao), 10)

def desenha_nariz():
    pygame.draw.polygon(tela, LARANJA, [[centro_largura_boneco, centro_altura_rosto_boneco-5], [centro_largura_boneco-20, centro_altura_rosto_boneco+5], [centro_largura_boneco, centro_altura_rosto_boneco]], 0)

terminou = False
while not terminou:
    pygame.display.update()
    desenha_bracos(60)
    desenha_corpo(40)
    desenha_botoes(6)
    desenha_chapeu(40)
    desenha_nariz()
    pygame.display.update()
    sleep(1)
    tela.fill((2,183,255))
    centro_altura_boneco -= 4
    centro_altura_rosto_boneco = centro_altura_boneco - 60
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()
pygame.quit()