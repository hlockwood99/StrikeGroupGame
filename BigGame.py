#STRIKEGROUPGAME
#https://pythonprogramming.net/pygame-python-3-part-1-intro/
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((1920,1080))

clock = pygame.time.Clock()

gameover = FALSE

while not gameover:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameover = True

		print(event)

	pygame.display.update()
	clock.tick(60)

