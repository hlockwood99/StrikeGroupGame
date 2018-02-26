#Fighter Pilot Game
#Goal: To be able to dodge missiles

import pygame
import time
import random

pygame.init()

display_width = 1200
display_height = 800

black = (0,0,0)
red = (255,0,0)
blue = (135,206,250)

plane_width = 85

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fighter Ace")
clock = pygame.time.Clock()

PlaneImg= pygame.image.load('tomcat.png')
misImg = pygame.image.load('aim-9.png')
mis1Img =pygame.transform.scale(misImg,(30,120))
mis1Img = pygame.transform.rotate(mis1Img, 180)




def misDodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render('Dodged: '+str(count), True, black)
	gameDisplay.blit(text,(0,0))

def missiles(misx, misy, misw, mish, color):
	gameDisplay.blit(mis1Img, [misx, misy, misw, mish])
	

def plane(x,y):
	gameDisplay.blit(PlaneImg, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',25)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	time.sleep(2)

	pygame.display.update()

def win():
	message_display('You have dodged all the enemy missiles!')

	time.sleep(2)

	pygame.quit()
	quit()	

def death():
	message_display('You have been shot down by enemy planes')

	time.sleep(2)

	pygame.quit()
	quit()

def game_loop():
	x = (display_width * 0.4)
	y = (display_height * 0.7)
	x_change = 0

	mis_startx = random.randrange(0,display_width)
	mis_starty = -600
	mis_speed = 9
	mis_width = 25
	mis_height = 100

	misCount = 1

	dodged = 0
	
	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -8
				if event.key == pygame.K_RIGHT:
					x_change = 8

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		gameDisplay.fill(blue)
		missiles(mis_startx, mis_starty, mis_width, mis_height, red)
		mis_starty += mis_speed
		plane(x,y)


		misDodged(dodged)


		if x > display_width - plane_width:
			x_change =-1
		if x < -70:
			x_change = 1

		if mis_starty > display_height:
			mis_starty = 0 - mis_height
			mis_startx = random.randrange(0,display_width)
			dodged +=1
			mis_speed +=1

			if dodged == 25:
				win()


		if y < mis_starty+mis_height:
			print('y Crossover')

			if x > mis_startx and x < mis_startx + mis_width or x+plane_width > mis_startx and x + plane_width < mis_startx+mis_width:
				print('x Crossover')
				death()



		pygame.display.update()
		clock.tick(60)
game_loop()
pygame.quit()
quit()