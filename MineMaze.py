import pygame
import time
import random

pygame.init()
global rect
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
	global rect
	rect = newimg.get_rect()
	rect.x = 200+x
	rect.y = 600+y
	gameDisplay.blit(newimg,rect)

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
x = 0
y = 0
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
	
	if rect.x<= 110 or rect.x>=990:
		done()
	elif rect.x<=900 and rect.y>=480 and rect.y<=520:
		done()
	elif rect.y >=750:
		done()
	elif rect.x>=200 and rect.y<=120 and rect.y>=80:
		done()
	elif rect.x<=370 and rect.x>=330 and rect.y<=750 and rect.y>=570:
		done()
	elif rect.x<=680 and rect.x>=640 and rect.y<=660 and rect.y>=500:
		done()
	elif rect.x<=850 and rect.x>=810 and rect.y<=750 and rect.y>=570:
		done()
	elif rect.x<=920 and rect.x>=880 and rect.y<=500 and rect.y>=260:
		done()
	elif rect.x<=780 and rect.x>=740 and rect.y<=340 and rect.y>=100:
		done()
	elif rect.x<=480 and rect.x>=440 and rect.y<=425 and rect.y>=185:
		done()
	elif rect.x<=320 and rect.x>=280 and rect.y<=380 and rect.y>=140:
		done()
	elif rect.x<=600 and rect.x>=560 and rect.y<=500 and rect.y>=400:
		done()
	elif rect.x<=620 and rect.x>=580 and rect.y<=300 and rect.y>=140:
		done()
	elif rect.x<=220 and rect.x>=100 and rect.y<=320 and rect.y>=280:
		done()
	if rect.x<=220 and rect.y<=100:
		letters('Congrats! You made it through the mine maze!!', 20, 400, 50)
		over =True
	
	
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()