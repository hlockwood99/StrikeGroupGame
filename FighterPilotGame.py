#Fighter Pilot Game
#Goal: To be able to engage enemy planes and dodge missiles

import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fighter Ace")

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

crashed = False

PlaneImg= pygame.image.load(PLACEHOLDER)

def plane(x,y):
	gameDisplay.blit(PlaneImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		

	pygame.display.update()
	clock.tick(60)
