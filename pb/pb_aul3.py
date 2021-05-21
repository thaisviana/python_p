import pygame

BRANCO = (255,255,255)
PRETO = (0,0,0)
LARANJA = (246,130,0)
VERMELHO = (230,0,0)

pygame.init()
largura_tela, altura_tela = 1024, 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill(BRANCO)
terminou = False

def mostra_texto(texto, pos, cor):
    font = pygame.font.Font(None, 24)
    text = font.render(f"{texto}", 1, cor)
    textpos = text.get_rect(center=pos,)
    tela.blit(text, textpos)

def desenha_abas():
    aba0 = pygame.Rect(0, 0, 255, 50)
    pygame.draw.rect(tela, PRETO, aba0)
    mostra_texto("ABA ZERO",(128,25), BRANCO)

    aba1 = pygame.Rect(256, 0, 255, 50)
    pygame.draw.rect(tela, PRETO, aba1)
    mostra_texto("ABA UM",(384,25), BRANCO)

    aba2 = pygame.Rect(512, 0, 255, 50)
    pygame.draw.rect(tela, PRETO, aba2)
    mostra_texto("ABA DOIS",(640,25), BRANCO)

    aba3 = pygame.Rect(768, 0, 256, 50)
    pygame.draw.rect(tela, PRETO, aba3)
    mostra_texto("ABA TRÊS",(896,25), BRANCO)
    return [aba0, aba1, aba2, aba3]
texto = "ABA ZERO"
while not terminou:
    abas = desenha_abas()
    mostra_texto("Projeto de Bloco",(512,70),PRETO)
    mostra_texto(texto,(512,94),PRETO)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for index, aba in enumerate(abas):
                    if aba.collidepoint(pos):
                        texto = f"Clicou na aba {index}"
    pygame.display.update()
    tela.fill(BRANCO)
pygame.display.quit()
pygame.quit()
