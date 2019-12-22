#-*-coding: utf-8-*-
import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
def main():
	pygame.init()
	gameDisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Snake")
	#Game loop
	gameExit = False
	while not gameExit:
		gameDisplay.fill(WHITE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print(event.type)
				gameExit = True
		pygame.draw.rect(gameDisplay, BLACK, (400, 300, 10, 20))

		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()