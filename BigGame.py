#STRIKEGROUPGAME
#https://pythonprogramming.net/pygame-python-3-part-1-intro/
#https://www.pygame.org/docs/

#Images from:
#http://docs.garagegames.com/torquex/official/content/documentation/TorqueX%202D/Tutorials/Airplane.html
import pygame

pygame.init()

height = 800
width = 1600
gameDisplay = pygame.display.set_mode((width,height))

blue = (30,64,150)


img = pygame.image.load('battleship.png')
newimg = pygame.transform.scale(img,(275,75))
#printing the battleship onto the window
def battleship(x,y,d):
	rimg = pygame.transform.rotate(newimg, d)
	gameDisplay.blit(rimg,(x,y))


caimg = pygame.image.load('carrier.png')
caimg = pygame.transform.scale(caimg,(375,130))

#Printing carrier onto the window
def carrier(x1,y1,d):
	myimg = pygame.transform.rotate(caimg, d1)
	gameDisplay.blit(myimg,(x1,y1))
	



d = 90
d1 = 90
ymove = 0
dmove = 0
d1move = 0
xmove = 0
x = 600
y = 300
x1 = 200
y1 = 300
clock = pygame.time.Clock()

over = False

while not over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			over = True
#Turning Left and Right_________________________________
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			xmove = -5
			dmove = 1
		elif event.key == pygame.K_RIGHT:
			xmove = 5
			dmove = -1
		#Moving Forward and Backwards_________________________________
		elif event.key == pygame.K_UP:
			ymove = -5
		elif event.key == pygame.K_DOWN:
			ymove = 1

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			xmove = 0
			dmove = 0
			d1move = 0
			ymove = 0




	x += xmove
	x1 += xmove
	d += dmove
	d1 += dmove
	y += ymove
	y1 += ymove
	gameDisplay.fill(blue)
	battleship(x,y,d)
	carrier(x1,y1,d1)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()