#Fighter Pilot Game
#Goal: To be able to engage enemy planes and dodge missiles

import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fighter Ace")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

plane_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

crashed = False

PlaneImg= pygame.image.load('tomcat.jpg')

def plane(x,y):
	gameDisplay.blit(PlaneImg, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(diplay_height/2))
	gameDisplay.blit(TextSurf, TextRact)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def death():
	message_display('You have Died')

def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0

	gameExit = False

	while not gameExit:

		car_speed = 0


	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		gameDisplay.fill(white)
		car(x,y)	

		if x > display_width - car_width or x < 0:
			gameExit = True

		pygame.display.update()
		clock.tick(60)
game_loop()
pygame.quit()
quit()