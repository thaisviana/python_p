import pygame
from pygame.locals import *
from grafico import desenha_grafico

pygame.init()

window = pygame.display.set_mode((600, 800), DOUBLEBUF)
screen = pygame.display.get_surface()
param1, param2 = 0 , 0
canvas, raw_data = desenha_grafico(param1, param2)

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True