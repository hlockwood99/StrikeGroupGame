import pygame
import random

pygame.init()

display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()
gameExit = False


eplaneImg = pygame.image.load('sub.png')
eplaneImg1 = pygame.transform.scale(eplaneImg, (150,50))

gray = (67, 70, 75)
blue = (135,206,250)
black = (0,0,0)


def planesDowned(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render('Tangos Downed: '+str(count), True, black)
	gameDisplay.blit(text,(0,0))

def bullet():
	
	bullet1 = pygame.Rect(500,D, 15,35)
	pygame.draw.rect(gameDisplay, black, bullet1)


	

def enemyPlane():
	gameDisplay.blit(eplaneImg1, (epstartx,epstarty))

epstartx = 1200
epstarty = random.randrange(0, 500)
tangos_downed = 0
a = display_height*.875
b = display_width*.5-50

D = 550
bulletSpeed = -10
b_change = 0 
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	b += b_change

	gameDisplay.fill(blue)

	enemyPlane()
	epstartx += -8
	if epstartx == 0:
		epstartx = 1200
		epstarty = random.randrange(0, 400)

	if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				b_change = -10
			if event.key == pygame.K_RIGHT:
				b_change = 10
			if event.key == pygame.K_SPACE:
				bullet()
				D += bulletSpeed
		
			
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				b_change = 0
		if event.key == pygame.K_SPACE:
			bullet()
	
	
	
	deckGun = pygame.Rect(b,600,100,100)
	barrel1 = pygame.Rect(b+20,550, 20,50)
	barrel2 = pygame.Rect(b+60, 550, 20, 50)
	pygame.draw.rect(gameDisplay, gray, barrel2)
	pygame.draw.rect(gameDisplay, gray, barrel1)
	pygame.draw.rect(gameDisplay, gray, deckGun)

	deck = pygame.Rect(0,a,display_width,a)
	pygame.draw.rect(gameDisplay, gray, deck)

	
	pygame.display.update()
	clock.tick(60)