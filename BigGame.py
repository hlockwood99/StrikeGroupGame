#STRIKEGROUPGAME
#https://pythonprogramming.net/pygame-python-3-part-1-intro/
import pygame

pygame.init()

height = 800
width = 1600
gameDisplay = pygame.display.set_mode((width,height))
black =(0,0,0)
blue = (30,64,150)
white=(255,255,255)

img = pygame.image.load('battleship.png')
newimg = pygame.transform.scale(img,(275,75))
def plane(x,y):
	gameDisplay.blit(newimg,(x,y))


x = 600
y = 300

clock = pygame.time.Clock()

over = False

while not over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			over = True

	gameDisplay.fill(blue)
	plane(x,y)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()