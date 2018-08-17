#-*-coding: utf-8-*-
import pygame
from pygame.locals import *


if __name__ == '__main__':
	pygame.init()
	v = pygame.display.set_mode((400, 300))
	pygame.display.set_caption("Hola mundo")
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				print("El usuario ha cerrado.")
				exit()
		pygame.display.update()