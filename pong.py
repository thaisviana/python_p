import pygame, sys
from pygame.locals import *

LARGURA_LINHA = 10
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
PALETA_TAMANHO = 50
PALETAOFFSET = 20
FPS = 200
LARGURA_TELA, ALTURA_TELA = 700, 500

BASICFONTSIZE = 20

def desenhaArena(tela):
    pygame.draw.rect(tela, BRANCO, ((0,0), (LARGURA_TELA,ALTURA_TELA)), LARGURA_LINHA*2)
    pygame.draw.line(tela, BRANCO, ((LARGURA_TELA//2),0), ((LARGURA_TELA//2),ALTURA_TELA), (LARGURA_LINHA//4))

def verificaPlacar(paleta1, bola, placar, bolaDirX):
    if bola.left == LARGURA_LINHA: 
        return 0
    elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 1
        return placar
    elif bola.right == LARGURA_TELA - LARGURA_LINHA:
        placar += 10
        return placar
    else: return placar

def inteligenciaArtificial(bola, bolaDirX, paleta2):
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -=1
    return paleta2

# Função para desenhar a paleta
def desenhaPaleta(paleta, tela):
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    pygame.draw.rect(tela, BRANCO, paleta)

def desenhaBola(bola, tela):
	pygame.draw.rect(tela, BRANCO, bola)

#altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX
    bola.y += bolaDirY
    return bola

def verificaColisaoBorda(bola, bolaDirX, bolaDirY):
    if bola.top == (LARGURA_LINHA) or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
            bolaDirY = bolaDirY * -1
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA):
            bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY

#Verifica a colisão da bola com a paleta1 ou paleta2    
def verificaColisaoBola(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        return -1
    else: return 1

#Desenha o placar na tela
def desenhaPlacar(placar, tela):
    font = pygame.font.Font(None, BASICFONTSIZE)
    resultadoSurf = font.render('placar = %s' %(placar), True, BRANCO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 150, 25)
    tela.blit(resultadoSurf, resultadoRect)

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.mouse.set_visible(0)
    pygame.display.set_caption("Pong da Thais")
    FPSCLOCK = pygame.time.Clock()
    placar = 0
    bolaX,bolaY = LARGURA_TELA//2 - LARGURA_LINHA//2,ALTURA_TELA//2 - LARGURA_LINHA//2
    bolaDirX, bolaDirY = -1, -1
    tela.fill(PRETO)

    jogador_um_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    jogador_dois_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    
    paleta1 = pygame.Rect(PALETAOFFSET,jogador_um_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogador_dois_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    terminou = False

    while not terminou:
        pygame.display.update()

        tela.fill(PRETO)
        desenhaArena(tela)
        desenhaPaleta(paleta1, tela)
        desenhaPaleta(paleta2, tela)
        desenhaBola(bola, tela)
        bola = moveBola(bola, bolaDirX, bolaDirY)
        bolaDirX, bolaDirY = verificaColisaoBorda(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verificaColisaoBola(bola, paleta1, paleta2, bolaDirX)
        paleta2 = inteligenciaArtificial (bola, bolaDirX, paleta2)
        placar = verificaPlacar(paleta1, bola, placar, bolaDirX)
        desenhaPlacar(placar, tela)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminou = True    
            elif event.type == MOUSEMOTION:
            	mouseX, mouseY = event.pos
            	paleta1.y = mouseY
        FPSCLOCK.tick(FPS)

    pygame.display.quit()
    pygame.quit()
    sys.exit()


if __name__=='__main__':
	main()