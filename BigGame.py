#STRIKEGROUPGAME
#https://pythonprogramming.net/pygame-python-3-part-1-intro/
#https://www.pygame.org/docs/

#Images from:
#collide rect
#http://docs.garagegames.com/torquex/official/content/documentation/TorqueX%202D/Tutorials/Airplane.html
import pygame
import time
import random
global over
pygame.init()



height = 800
width = 1200
mainGame = pygame.display.set_mode((width,height))
black = (0,0,0)
blue = (30,64,150)
beach = (110,70,40)
green = (30, 70, 40)

def letters(message,x2,y2,fontsize):
	message = str(message)
	font = pygame.font.Font("freesansbold.ttf", fontsize)
	message = font.render(message, True, black)
	gameDisplay.blit(message, (x2, y2))

#Printing the battleship onto the window
img = pygame.image.load('battleship.png')
img = pygame.transform.scale(img,(175,55))
def battleship(w,v,d):
	newimg = pygame.transform.rotate(img, d)
	mainGame.blit(newimg,(w,v))

#Printing carrier onto the window
caimg = pygame.image.load('carrier.png')
caimg = pygame.transform.scale(caimg,(250,100))
def carrier(w1,v1,d):
	myimg = pygame.transform.rotate(caimg, d)
	mainGame.blit(myimg,(w1,v1))

#Printing destroyer onto window
dimg = pygame.image.load('destroyer.png')
dimg = pygame.transform.scale(dimg,(150,50))
def destroyer(w2,v2,d):
	deimg = pygame.transform.rotate(dimg, d)
	mainGame.blit(deimg, (w2,v2))

d = 90
ymove = 0
dmove = 0
d1move = 0
xmove = 0
w = 800
v = 500
w1 = 600
v1 = 500
w2 = 400
v2 = 500
a= -300
b=-700
clock = pygame.time.Clock()

over = False

while not over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			over = True
	mainGame.fill(blue)
#Turning Left and Right_________________________________
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			xmove = -5
		elif event.key == pygame.K_RIGHT:
			xmove = 5
		#Moving Forward and Backwards_________________________________
		#elif event.key == pygame.K_UP:
			#ymove = -5
		#elif event.key == pygame.K_DOWN:
			#ymove = 1


	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			xmove = 0
			dmove = 0
			d1move = 0
			ymove = 0




	w += xmove
	w1 += xmove
	w2 += xmove
	v += ymove
	v1 += ymove
	v2 += ymove
	
	rect1 = pygame.Rect(0,0,80,800)
	rect2 = pygame.Rect(1120,0,80,800)
	pygame.draw.rect(mainGame, beach, rect1)
	pygame.draw.rect(mainGame, beach, rect2)

	if a < height:
		tree = pygame.Rect(20,a, 40, 40)
		pygame.draw.rect(mainGame, green, tree)
		speed = 5
		a = a+speed
	else:
		a = a-height

	if b < height:
		tree1 = pygame.Rect(1140,b, 40, 40)
		pygame.draw.rect(mainGame, green, tree1)
		b = b+speed
	else:
		b = b-height


	battleship(w,v,d)
	carrier(w1,v1,d)
	destroyer(w2,v2,d)
	clock.tick(60)
	pygame.display.update()
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_e: 
			pygame.init()

			gameDisplay = pygame.display.set_mode((width,height))

			mine = pygame.image.load('SeaMine.png')
			mine1 = pygame.transform.scale(mine,(20,20))
			def sea_mine(x1,y1):
				gameDisplay.blit(mine1,(x1,y1))

			def done():
				global oops
				letters('You hit a mine!',100,400,100)
				oops = True

			dm = 90
			ymove = 0
			dmovem = 0
			xmove = 0
			x = 200
			y = 600

			oops = False

			while not oops:

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						oops = True
				
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
						dmovem =0.5
					elif event.key == pygame.K_e:
						dmovem = -0.5

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						xmove = 0
						dmovem = 0
						ymove = 0



				x += xmove
				y += ymove
				dm += dmovem
				gameDisplay.fill(blue)
				img = pygame.transform.scale(img,(110,35))
				battleship(x,y,dm)
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
				elif x<=220 and y<=100:
					letters('Congrats! You made it through the mine maze!!', 20, 400, 50)
					win = True
					oops = True
					over = True

				pygame.display.update()
				clock.tick(60)
