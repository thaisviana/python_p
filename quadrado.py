import pygame

pygame.init()
largura_tela, altura_tela = 500, 500
tela = pygame.display.set_mode((largura_tela, altura_tela))

BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO = (255, 0, 0)
largura_quadrado,altura_quadrado = 30,30
tela.fill(PRETO)


def desenha_quadrado_vermelho(x,y):
    cor = VERMELHO
    pygame.draw.rect(tela, cor, (x,y,largura_quadrado, altura_quadrado), 0)

terminou = False
x, y = largura_tela/2 - largura_quadrado/2 , altura_tela/2 - altura_quadrado/2
while not terminou:
    desenha_quadrado_vermelho(x,y)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                x -= 1
            if event.key == ord('d'):
                x += 1
            if event.key == ord('w'):
                y -= 1
            if event.key == ord('s'):
                y += 1
            tela.fill(PRETO)        
            desenha_quadrado_vermelho(x,y)
            pygame.display.update()

pygame.display.quit()
pygame.quit()