import pygame
from random import randint, choice
from CONSTANTS import largura_tela, altura_tela, q_largura, q_altura

CORES = ((255,0,0), (0,255,0), (0,0,255), (255,255,255))

class Quadradinho():
    def __init__(self):
        self.largura = q_largura
        self.altura = q_altura
        self.x = randint(0, largura_tela-self.largura)
        self.y = randint(0, altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = choice(CORES)
        #(randint(40, 255), randint(40, 255), randint(40, 255))
    
    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

    @staticmethod
    def cria_n_quadradinhos(n):
        lista =[]
        for i in range(n):
            quadradinho = Quadradinho()
            lista.append(quadradinho)
        return lista