#STRIKEGROUPGAME
#https://pythonprogramming.net/pygame-python-3-part-1-intro/
#https://www.pygame.org/docs/

#Images from:
#http://www.nextreflexdc.com/mail-clip-art/mail-clip-art-mail-clip-art-free-clipart-panda-free-clipart-images-download/
#http://bradlys-double-7.wikia.com/wiki/Bullet_Bill
#http://www.vancitymommyd.com/7221/waves-clipart-02-12-2017/waves-clipart-waves-ocean-wave-clip-art-vector-free-clipart-images-clipartcow-3-plant-clipart/
#https://www.pinterest.com/pin/312859505341393738/
#http://docs.garagegames.com/torquex/official/content/documentation/TorqueX%202D/Tutorials/Airplane.html

import pygame
import time
import random
from MineMaze import maze
global over
global oops
pygame.init()
height = 800
width = 1200
mainGame = pygame.display.set_mode((width,height))
#Colors
white = (255,255,255)
black = (0,0,0)
blue = (30,64,150)
beach = (110,70,40)
treecolor = (30, 70, 40)
green = (0,255,0)
red = (255,0,0)
#Stats
HP = 100
morale = 100
#Randomizing
randomlist =[]
d = 90
ymove = 0
dmove = 0
d1move = 0
xmove = 0
#Inital Placing of Images
w = 800
v = 500
w1 = 600
v1 = 500
w2 = 400
v2 = 500
w3 = w1
v3 = 0
a= -300
b=-700
w4 = 1200
v4 = 500
w5 = 1200
v5 = 500
w6 = 1000
v6= 0

message = False
over = False
r=0
n=0
clock = pygame.time.Clock()
#Battleship images
img = pygame.image.load('battleship.png')
img = pygame.transform.scale(img,(175,55))
#Carrier Images
caimg = pygame.image.load('carrier.png')
caimg = pygame.transform.scale(caimg,(250,100))
#Destroyer Images
dimg = pygame.image.load('destroyer.png')
dimg = pygame.transform.scale(dimg,(150,50))
#Whale Images
wimg = pygame.image.load('Whale.png')
wimg = pygame.transform.scale(wimg,(100,100))
#wave Images
waveimg = pygame.image.load('rogueWave.png')
waveimg = pygame.transform.scale(waveimg,(200,200))
#Anchor Images
portimg = pygame.image.load('anchor.png')
portimg = pygame.transform.scale(portimg,(200,200))
#Torpedo Images
simg = pygame.image.load('StrayTorp.png')
simg = pygame.transform.scale(simg, (100,100))
#mail Images
mimg = pygame.image.load('mail.jpg')
mimg = pygame.transform.scale(mimg, (100,100))
#mine images
mine = pygame.image.load('SeaMine.png')
mine1 = pygame.transform.scale(mine,(20,20))


def letters(message,x2,y2,fontsize):
	font = pygame.font.Font("freesansbold.ttf", fontsize)
	message = font.render(message, True, white)
	mainGame.blit(message, (x2, y2))

#Printing the battleship onto the window

def battleship(w,v,d):
	newimg = pygame.transform.rotate(img, d)
	mainGame.blit(newimg,(w,v))

#Printing carrier onto the window

def carrier(w1,v1,d):
	myimg = pygame.transform.rotate(caimg, d)
	mainGame.blit(myimg,(w1,v1))

#Printing destroyer onto window

def destroyer(w2,v2,d):
	deimg = pygame.transform.rotate(dimg, d)
	mainGame.blit(deimg, (w2,v2))


def dawhale(w3, v3):
	mainGame.blit(wimg, (w3,v3))


def dawave(w4,v4):
	mainGame.blit(waveimg,(w4,v4))


def dastraytorp(w5,v5):
	mainGame.blit(simg,(w5,v5))


def daport(w6,v6):
	mainGame.blit(portimg,(w6,v6))


def damail(w7,v7):
	mainGame.blit(mimg,(w7,v7))	

def currentHealth(HP):
	letters('Health:' + str(HP) + '/100:',120,700,24)
	health = pygame.Rect(300,700,HP,20)
	pygame.draw.rect(mainGame, red, health)

def currentMorale(morale):
	letters('Morale' + str(morale) + '/100:',120,750,24)
	moralebar = pygame.Rect(300,750,morale,20)
	pygame.draw.rect(mainGame,green,moralebar)

def sea_mine(x1,y1):
		gameDisplay.blit(mine1,(x1,y1))

def done():
	global over
	global HP
	global oops
	letters('You hit a mine!',100,400,100)
	HP = HP -50
	pygame.display.update()
	pygame.time.delay(2000)
	message = True
	oops = True


while not over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			over = True
	
#Turning Left and Right_________________________________
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				xmove = -5
			if event.key == pygame.K_RIGHT and w <= 1000:
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
	if w2 <= 120:
			xmove = 5
	if w >=1000:
		xmove = -5

	if HP<= 0:
		over = True
		endGame = pygame.display.set_mode((width,height))
		endGame.fill(red)

	if morale <=0:
		over = True
	mainGame.fill(blue)

	w += xmove
	w1 += xmove
	w2 += xmove
	v += ymove
	v1 += ymove
	v2 += ymove
	w3 = w1
	
	# Drawing the Beaches
	rect1 = pygame.Rect(0,0,80,800)
	rect2 = pygame.Rect(1120,0,80,800)
	pygame.draw.rect(mainGame, beach, rect1)
	pygame.draw.rect(mainGame, beach, rect2)


	#Making the moving trees
	if a < height:
		tree = pygame.Rect(20,a, 40, 40)
		pygame.draw.rect(mainGame, treecolor, tree)
		speed = 5
		a = a+speed
	else:
		a = a-height

	if b < height:
		tree1 = pygame.Rect(1140,b, 40, 40)
		pygame.draw.rect(mainGame, treecolor, tree1)
		b = b+speed
	else:
		b = b-height


#Randomizing the events

	r+=5
	if r == 1000:
		n = int(random.uniform(1,6))
		while n in randomlist:
			n = int(random.uniform(1,6))
		randomlist.append(n)
		r= 0

			
	if n == 1:
		#Hitting a whale
		if v3<height:
			v3 +=5
		if v3>= 0 and v3<605:
			dawhale(w3,v3)
		if v3>= 600 and v3 <605:
			message = 'You hit a whale!'
			letters(message, 200, 400, 100)
			message = True
			morale = morale - 25
			
	elif n ==2:
		#Rogue Wave
		if w4 > 0:
			w4-=5
		if w4<=900 and w4 >100:
			dawave(w4,v4)
		if w4 >= 100 and w4<105:
			message = 'A rogue wave hit you!'
			letters(message, 100, 400, 100)
			message = True
			HP -= 15

	elif n ==3:
		#Stray Torp
		if w5>0:
			w5-=5
		if w5 <=900 and w5>=w:
			dastraytorp(w5,v5)
		if w5>=w and w5<w+5:
			message = 'A Stray Torp struck one of your ships!'
			letters(message, 50, 400, 50)
			message = True
			HP -= 25
	elif n == 4:
		#Stopping at a port
		if v6<height:
			v6+=5
		if v6>= 0 and v6<505:
			daport(w6,v6)
		if v6>=500 and v6<505:
			message = 'Stopping at a port'
			letters(message, 50, 400, 80)
			message = True
			HP+=50
	

	elif n ==5:
		#Mine Mini Game
		mazegame = maze(HP)
		mazegame.thegame()
		HP = mazegame.healthpoints
		n= 0
		pygame.display.update()
		clock.tick(60)

	
	#Makes Sure that the health does not go above 100
	if HP>100:
		HP=100
	if morale>100:
		morale = 100

	currentHealth(HP)
	currentMorale(morale)
	battleship(w,v,d)
	carrier(w1,v1,d)
	destroyer(w2,v2,d)
	clock.tick(60)
	pygame.display.update()
	if message == True:
		pygame.time.delay(2000)
		message = False
pygame.quit()
quit()