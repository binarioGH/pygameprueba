#-*-coding: utf-8-*-
import pygame

def main():
	pygame.init()
	gameDisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Snake")
	#Game loop
	death = False
	while not death:
		for event in pygame.event.get():
			print(event)
		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()