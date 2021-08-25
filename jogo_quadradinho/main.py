import pygame
from CONSTANTS import largura_tela, altura_tela, cor, tempo_total_do_jogo,numero_inicial_de_quadradinhos
from Quadradinho import Quadradinho
from time import sleep

def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render(f"Tempo: {tempo}s | Pontuação: {pontos}", 1, cor['BRANCO'])
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

def mostra_pontuacao_final(tela, pontos):
    tela.fill(cor['PRETO']) # Limpa tela
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação: " + str(pontos) + " pontos", 1, cor['BRANCO'])
    textpos = text.get_rect(center=(tela.get_width()/2, tela.get_height()/2))
    tela.blit(text, textpos)

def calcula_pontuacao(pontos, quadradinho):
    r, g, b = quadradinho.cor[0], quadradinho.cor[1], quadradinho.cor[2]
    cor  = "outra cor"
    ponto = 1
    if r > 100 and r > g+b:
        cor = "VERMELHO"
        ponto = 2
    if b > 80 and b > g+r:
        cor = "AZUL"
        ponto = 3
    if g > 80 and g > b+r:
        cor = "VERDE"
        ponto = 4
    print("rgb", r, g, b, cor)
    return pontos + ponto

pygame.init()

tela = pygame.display.set_mode((largura_tela, altura_tela))
efeito = pygame.mixer.Sound('jogo_quadradinho/coin.wav')
clock = pygame.time.Clock()
tempo_corrente = tempo_total_do_jogo
pontos = 0
conta_clocks = 0
terminou = False
lista_de_quadradinhos = Quadradinho.cria_n_quadradinhos(numero_inicial_de_quadradinhos)

while not terminou:
    conta_clocks += 1
    if tempo_corrente > 0:
        mostra_tempo(tempo_corrente, pontos)
        for q in lista_de_quadradinhos:
            q.desenha(tela)

        if conta_clocks == 50:
            conta_clocks = 0
            tempo_corrente -= 1
            quadradinho = Quadradinho()
            lista_de_quadradinhos.append(quadradinho)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
                pos = pygame.mouse.get_pos()
                for q in lista_de_quadradinhos:
                    if q.area.collidepoint(pos):
                        lista_de_quadradinhos.remove(q)
                        efeito.play()
                        pontos = calcula_pontuacao(pontos, q)
            if event.type == pygame.QUIT:
                terminou = True
        if tempo_corrente == 0:
            lista_de_quadradinhos.clear()
            mostra_pontuacao_final(tela, pontos)
        pygame.display.update()
        tela.fill(cor['PRETO'])
    else:
        mostra_pontuacao_final(tela, pontos)
        pygame.display.update()
        tela.fill(cor['PRETO'])
    clock.tick(50)

pygame.display.quit()
pygame.quit()