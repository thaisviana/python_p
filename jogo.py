import pygame
from random import randint

pygame.init()
largura_tela, altura_tela = 500, 500
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
VERMELHO = (255, 0, 0)
LARANJA = (246, 130, 0)
tela.fill(PRETO)
conta_segundos = 10


class Quadradinho():
    def __init__(self):
        self.largura, self.altura = 30, 30
        self.x, self.y = randint(
            0, largura_tela - self.largura), randint(0, altura_tela - self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (randint(20, 255), randint(20, 255), randint(20, 255))

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

# Para imprimir o texto com o tempo


def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, BRANCO)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

# Mostra a tela final com a pontução obtida. Representa o placar final.
def mostra_pontuacao_final(tela, pontos):
    tela.fill(PRETO)
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação: " + str(pontos) + " quadradinhos", 1, BRANCO)
    textpos = text.get_rect(center=(tela.get_width()/2, tela.get_height()/2))
    tela.blit(text, textpos)
pontos = 0
# Variavel para contar quantas esperas de 50Hz ou 0,02s
conta_clocks = 0

def calcula_pontos(q_clicado):
    if q_clicado.cor[0] > 150 and q_clicado.cor[1] < 80 and q_clicado.cor[2] < 80:
        return 1
    elif q_clicado.cor[0] < 80 and q_clicado.cor[1] > 150 and q_clicado.cor[2] < 80:
        return 2
    elif q_clicado.cor[0] < 80 and q_clicado.cor[1] < 80 and q_clicado.cor[2] > 150:
        return 3
    return 1

lista_quadrinhos = []

tela.fill(PRETO)
for i in range(20):
    q = Quadradinho()
    q.desenha(tela)
    lista_quadrinhos.append(q)

terminou = False
while not terminou:
    conta_clocks += 1

    # A cada 50 cont_clocks, temos 1s (0,02s x 50 = 1s)
    if conta_clocks == 50:
        conta_segundos -= 1
        conta_clocks = 0
        # lista_quadrinhos = []
        # for i in range(20):
        #     q = Quadradinho()
        #     lista_quadrinhos.append(q)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for q in lista_quadrinhos:
                if q.area.collidepoint(pos):
                    lista_quadrinhos.remove(q)
                    pontos += calcula_pontos(q)
    if conta_segundos >= 0 :
        tela.fill(PRETO)
        for q in lista_quadrinhos:
            q.desenha(tela)
        mostra_tempo(conta_segundos,pontos)
        pygame.display.update()
    else:
        mostra_pontuacao_final(tela, pontos)  
        pygame.display.update() 
        lista_quadrinhos = []
    clock.tick(50)

pygame.display.quit()
pygame.quit()
