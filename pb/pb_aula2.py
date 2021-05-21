import pygame
centro_largura_boneco = 250
altura_centro_cara_boneco = 190
altura_centro_corpo_boneco = altura_centro_cara_boneco +40
BRANCO = (255,255,255)
PRETO = (0,0,0)
LARANJA = (246,130,0)
VERMELHO = (230,0,0)

def desenha_chapeu():
    pygame.draw.rect(tela, PRETO, (centro_largura_boneco-24,altura_centro_cara_boneco-20,48, 8), 0)
    pygame.draw.rect(tela, PRETO, (centro_largura_boneco-15,altura_centro_cara_boneco-50,30, 30), 0)

def desenha_nariz():
    pygame.draw.polygon(tela, LARANJA, [[centro_largura_boneco, altura_centro_cara_boneco-5], [centro_largura_boneco-15, altura_centro_cara_boneco+5], [centro_largura_boneco, altura_centro_cara_boneco]], 0)


def desenha_bracos():
    pygame.draw.circle(tela, PRETO, (centro_largura_boneco-50,altura_centro_cara_boneco+10), 8)
    pygame.draw.circle(tela, PRETO, (centro_largura_boneco+50,altura_centro_cara_boneco+10), 8)
    pygame.draw.line(tela, PRETO,(centro_largura_boneco+25,altura_centro_cara_boneco+30),(centro_largura_boneco+50,altura_centro_cara_boneco+10), 8)
    pygame.draw.line(tela, PRETO,(centro_largura_boneco-25,altura_centro_cara_boneco+30),(centro_largura_boneco-50,altura_centro_cara_boneco+10), 8)

pygame.init()
largura_tela, altura_tela = 500, 500
tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill((2,183,255))
terminou = False
while not terminou:

    desenha_bracos()
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,altura_centro_corpo_boneco+60), 50)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,altura_centro_corpo_boneco), 30)
    pygame.draw.circle(tela, BRANCO, (centro_largura_boneco,altura_centro_cara_boneco), 20)

    desenha_nariz()

    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,altura_centro_corpo_boneco-12), 4)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,altura_centro_corpo_boneco), 4)
    pygame.draw.circle(tela, VERMELHO, (centro_largura_boneco,altura_centro_corpo_boneco+12), 4)
    desenha_chapeu()
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True
pygame.display.quit()
pygame.quit()