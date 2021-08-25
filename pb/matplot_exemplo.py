import pygame
from pygame.locals import *
from grafico import desenha_grafico
from time import sleep
import psutil
from numpy import polyfit
pygame.init()

window = pygame.display.set_mode((600, 1024), DOUBLEBUF)
screen = pygame.display.get_surface()
window.fill((255,255,255))
param1, param2 = 0 , 0
tempos = []
valores = []
valores_mem = []
for i in range(0,100):
	tempos.append(i)
	valores.append(psutil.cpu_percent())
	mem = psutil.virtual_memory()
	valores_mem.append(round((mem.used/mem.total),3) * 100)
	sleep(0.01)
canvas, raw_data = desenha_grafico(tempos,valores, "CPU %")
size = canvas.get_width_height()
surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
##

canvas, raw_data2 = desenha_grafico(tempos, valores_mem, "MEMÓRIA %")

surf = pygame.image.fromstring(raw_data2, size, "RGB")
screen.blit(surf, (0,480))

pygame.display.flip()

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True