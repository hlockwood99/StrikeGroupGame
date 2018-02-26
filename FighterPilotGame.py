#Fighter Pilot Game
#Goal: To be able to dodge missiles

import pygame
import time
import random
class Fighter:
	def __init__(self,HP):
		self.display_width = 1200
		self.display_height = 800

		self.black = (0,0,0)
		self.blue = (135,206,250)
		self.red = (255,0,0)
		self.plane_width = 85

		self.fighterdisplay = pygame.display.set_mode((self.display_width,self.display_height))
		pygame.display.set_caption("Fighter Ace")
		self.clock = pygame.time.Clock()

		self.PlaneImg= pygame.image.load('tomcat.png')
		self.misImg = pygame.image.load('aim-9.png')
		self.mis1Img =pygame.transform.scale(self.misImg,(30,120))
		self.mis1Img = pygame.transform.rotate(self.mis1Img, 180)
		self.gameExit = False
		self.x = (self.display_width * 0.4)
		self.y = (self.display_height * 0.7)
		self.x_change = 0
		self.totalhealth = HP
		self.mis_startx = random.randrange(0,self.display_width)
		self.mis_starty = -600
		self.mis_speed = 9
		self.mis_width = 25
		self.mis_height = 100

		self.misCount = 1

		self.dodged = 0




	def misDodged(self,count):
		self.font = pygame.font.SysFont(None, 25)
		self.text = self.font.render('Dodged: '+str(count), True, self.black)
		self.fighterdisplay.blit(self.text,(0,0))

	def missiles(self,misx, misy, misw, mish, color):
		self.fighterdisplay.blit(self.mis1Img, [misx, misy, misw, mish])
		

	def plane(self,x,y):
		self.fighterdisplay.blit(self.PlaneImg, (x,y))

	def text_objects(self,text, font):
		self.textSurface = self.font.render(text, True, self.black)
		return self.textSurface, self.textSurface.get_rect()

	def message_display(self,text):
		self.largeText = pygame.font.Font('freesansbold.ttf',25)
		TextSurf, self.TextRect = Fighter.text_objects(self,text, self.largeText)
		self.TextRect.center = ((self.display_width/2),(self.display_height/2))
		self.fighterdisplay.blit(TextSurf, self.TextRect)

		time.sleep(2)

		pygame.display.update()

	def win(self):
		Fighter.message_display(self,'You have dodged all the enemy missiles!')
		self.totalhealth -= 25
		time.sleep(2)
		self.gameExit = True

	def death(self):
		Fighter.message_display(self,'You have been shot down by enemy planes')

		time.sleep(2)
		self.gameExit = True


	def game_loop(self):
		while not self.gameExit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()


				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.x_change = -8
					if event.key == pygame.K_RIGHT:
						self.x_change = 8

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						self.x_change = 0

			self.x += self.x_change

			self.fighterdisplay.fill(self.blue)
			Fighter.missiles(self,self.mis_startx, self.mis_starty, self.mis_width, self.mis_height, self.red)
			self.mis_starty += self.mis_speed
			Fighter.plane(self,self.x,self.y)


			Fighter.misDodged(self,self.dodged)


			if self.x > self.display_width - self.plane_width:
				self.x_change =-1
			if self.x < -70:
				self.x_change = 1

			if self.mis_starty > self.display_height:
				self.mis_starty = 0 - self.mis_height
				self.mis_startx = random.randrange(0,self.display_width)
				self.dodged +=1
				self.mis_speed +=1

				if self.dodged == 25:
					Fighter.win(self,)


			if self.y < self.mis_starty+self.mis_height:

				if self.x > self.mis_startx and self.x < self.mis_startx + self.mis_width or self.x+self.plane_width > self.mis_startx and self.x + self.plane_width < self.mis_startx+self.mis_width:
					Fighter.death(self)



			pygame.display.update()
			self.clock.tick(60)