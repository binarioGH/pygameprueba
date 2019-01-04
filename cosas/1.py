#-*-coding: utf-8-*-
import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")
x = 50
y = 50
width = 40
height = 60
vel = 5
run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			print("Good bye.")
		pygame.draw.rect(win, (100,50,50), (x,y,width,height))
		pygame.display.update()
pygame.quit()