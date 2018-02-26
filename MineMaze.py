import pygame
import time
import random
global healthpoints
class maze:
	def __init__(self,HP):
		self.height = 800
		self.width = 1200
		self.d = 90
		self.healthpoints = HP
		self.ymove = 0
		self.dmove = 0
		self.xmove = 0
		self.x = 200
		self.y = 600
		self.blue = (30,64,150)
		self.black =(0,0,0)
		self.gameDisplay = pygame.display.set_mode((self.width,self.height))
		self.img = pygame.image.load('battleship.png')
		self.newimg = pygame.transform.scale(self.img,(100,30))
		self.mine = pygame.image.load('SeaMine.png')
		self.mine1 = pygame.transform.scale(self.mine,(20,20))

	#printing the battleship onto the window
	def battleship(self,x,y,d):
		self.newestimg = pygame.transform.rotate(self.newimg, d)
		self.gameDisplay.blit(self.newestimg,(x,y))

	

	def sea_mine(self,x1,y1):
		self.gameDisplay.blit(self.mine1,(x1,y1))

	def gamemessage(self,message,x2,y2,fontsize):
		self.font = pygame.font.Font("freesansbold.ttf", fontsize)
		self.message = self.font.render(message, True, self.black)
		self.gameDisplay.blit(self.message, (x2, y2))

	def done(self):
		maze.gamemessage(self,'You hit a mine!',100,400,100)
		self.healthpoints -= 50
		self.oops=True

	def thegame(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.oops = False
		while not self.oops:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.oops = True
			
		#Turning Left and Right_________________________________
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.xmove = -3
						#dmove = 1s
					elif event.key == pygame.K_RIGHT:
						self.xmove = 3
						#dmove = -1
					#Moving Forward and Backwards_________________________________
					elif event.key == pygame.K_UP:
						self.ymove = -3
					elif event.key == pygame.K_DOWN:
						self.ymove = 3
					elif event.key == pygame.K_q:
						self.dmove =0.5
					elif event.key == pygame.K_e:
						self.dmove = -0.5

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_q or event.key == pygame.K_e:
						self.xmove = 0
						self.dmove = 0
						self.ymove = 0


			self.gameDisplay.fill(self.blue)
			self.x += self.xmove
			self.y += self.ymove
			self.d += self.dmove
			
			maze.battleship(self,self.x,self.y,self.d)
			#HORIZ
			for f in range(20):
				maze.sea_mine(self,f*40+200,100)
			for k in range(23):
				maze.sea_mine(self,k*40+110,750)
			#VERT
			for h in range(16):
				maze.sea_mine(self,100,100+40*h)
				maze.sea_mine(self,1000,100+40*h)
			#Inside
			for j in range(21):
				maze.sea_mine(self,j*40+100,500)
			for l in range(5):
				maze.sea_mine(self,350,750-l*40)
				maze.sea_mine(self,660,500+l*40)
				maze.sea_mine(self,830,750-l*40)
			for a in range(7):
				maze.sea_mine(self,900,500-a*40)
				maze.sea_mine(self,760, 100+a*40)
				maze.sea_mine(self,460,185+a*40)
				maze.sea_mine(self,300,140+a*40)
			for b in range(4):
				maze.sea_mine(self,580,500-b*40)
				maze.sea_mine(self,600, 140+b*40)
				maze.sea_mine(self,100+40*b,300)
			
			if self.x<= 110 or self.x>=990:
				maze.done(self)

			elif self.x<=900 and self.y>=480 and self.y<=520:
				maze.done(self)
			elif self.y >=750:
				maze.done(self)
			elif self.x>=200 and self.y<=120 and self.y>=80:
				maze.done(self)
			elif self.x<=370 and self.x>=330 and self.y<=750 and self.y>=570:
				maze.done(self)
			elif self.x<=680 and self.x>=640 and self.y<=660 and self.y>=500:
				maze.done(self)
			elif self.x<=850 and self.x>=810 and self.y<=750 and self.y>=570:
				maze.done(self)
			elif self.x<=920 and self.x>=880 and self.y<=500 and self.y>=260:
				maze.done(self)
			elif self.x<=780 and self.x>=740 and self.y<=340 and self.y>=100:
				maze.done(self)
			elif self.x<=480 and self.x>=440 and self.y<=425 and self.y>=185:
				maze.done(self)
			elif self.x<=320 and self.x>=280 and self.y<=380 and self.y>=140:
				maze.done(self)
			elif self.x<=600 and self.x>=560 and self.y<=500 and self.y>=400:
				maze.done(self)
			elif self.x<=620 and self.x>=580 and self.y<=300 and self.y>=140:
				maze.done(self)
			elif self.x<=220 and self.x>=100 and self.y<=320 and self.y>=280:
				maze.done(self)
			if self.x<=220 and self.y<=100:
				maze.gamemessage(self,'Congrats! You made it through the mine maze!!', 20, 400, 50)
				self.oops =True
			
			
			pygame.display.update()
			self.clock.tick(60)
		pygame.time.delay(2000)