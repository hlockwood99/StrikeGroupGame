import pygame
import time
import random

pygame.init()

global over
height = 800
width = 1200
gameDisplay = pygame.display.set_mode((width,height))

blue = (30,64,150)
black =(0,0,0)


img = pygame.image.load('battleship.png')
newimg = pygame.transform.scale(img,(110,30))
#printing the battleship onto the window
def battleship(x,y,d):
	rimg = pygame.transform.rotate(newimg, d)
	gameDisplay.blit(rimg,(x,y))

mine = pygame.image.load('SeaMine.png')
mine1 = pygame.transform.scale(mine,(20,20))

def sea_mine(x1,y1):
	gameDisplay.blit(mine1,(x1,y1))

def letters(message,x2,y2,fontsize):
	message = str(message)
	font = pygame.font.Font("freesansbold.ttf", fontsize)
	message = font.render(message, True, black)
	gameDisplay.blit(message, (x2, y2))

def done():
	global over
	letters('You hit a mine!',100,400,100)
	over=True

d = 90
ymove = 0
dmove = 0
xmove = 0
x = 200
y = 600
clock = pygame.time.Clock()

over = False


while not over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			over = True
	
#Turning Left and Right_________________________________
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			xmove = -3
			#dmove = 1
		elif event.key == pygame.K_RIGHT:
			xmove = 3
			#dmove = -1
		#Moving Forward and Backwards_________________________________
		elif event.key == pygame.K_UP:
			ymove = -3
		elif event.key == pygame.K_DOWN:
			ymove = 3
		elif event.key == pygame.K_q:
			dmove =0.5
		elif event.key == pygame.K_e:
			dmove = -0.5

	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			xmove = 0
			dmove = 0
			ymove = 0



	x += xmove
	y += ymove
	d += dmove
	gameDisplay.fill(blue)
	'''
	for k in range(100):
		coordsh = int(random.uniform(0,800))
		coordsw = int(random.uniform(0,1200))
		sea_mine(coordsw, coordsh)
	'''
	battleship(x,y,d)
	#HORIZ
	for f in range(20):
		sea_mine(f*40+200,100)
	for k in range(23):
		sea_mine(k*40+110,750)
	#VERT
	for h in range(16):
		sea_mine(100,100+40*h)
		sea_mine(1000,100+40*h)
	#Inside
	for j in range(21):
		sea_mine(j*40+100,500)
	for l in range(5):
		sea_mine(350,750-l*40)
		sea_mine(660,500+l*40)
		sea_mine(830,750-l*40)
	for a in range(7):
		sea_mine(900,500-a*40)
		sea_mine(760, 100+a*40)
		sea_mine(460,185+a*40)
		sea_mine(300,140+a*40)
	for b in range(4):
		sea_mine(580,500-b*40)
		sea_mine(600, 140+b*40)
		sea_mine(100+40*b,300)
	
	if x<= 110 or x>=990:
		done()
	elif x<=900 and y>=480 and y<=520:
		done()
	elif y >=750:
		done()
	elif x>=200 and y<=120 and y>=80:
		done()
	elif x<=370 and x>=330 and y<=750 and y>=570:
		done()
	elif x<=680 and x>=640 and y<=660 and y>=500:
		done()
	elif x<=850 and x>=810 and y<=750 and y>=570:
		done()
	elif x<=920 and x>=880 and y<=500 and y>=260:
		done()
	elif x<=780 and x>=740 and y<=340 and y>=100:
		done()
	elif x<=480 and x>=440 and y<=425 and y>=185:
		done()
	elif x<=320 and x>=280 and y<=380 and y>=140:
		done()
	elif x<=600 and x>=560 and y<=500 and y>=400:
		done()
	elif x<=620 and x>=580 and y<=300 and y>=140:
		done()
	elif x<=220 and x>=100 and y<=320 and y>=280:
		done()
	if x<=220 and y<=100:
		letters('Congrats! You made it through the mine maze!!', 20, 400, 50)
		over =True

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()