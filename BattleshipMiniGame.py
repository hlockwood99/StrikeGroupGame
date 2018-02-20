import pygame

pygame.init()
pygame.font.init()
height = 900
width = 1200
gameDisplay = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
white = (255,255,255)
blue = (0,0,200)
red = (255,0,0)
black = (0,0,0)
over = False
AtoJ = ["A","B","C","D","E","F","G"]
numbers = ["1","2","3","4","5","6","7"]
def letters(message,x,y,fontsize):
	message = str(message)
	font = pygame.font.Font("freesansbold.ttf", fontsize)
	message = font.render(message, True, black)
	gameDisplay.blit(message, (x, y))

while not over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			over = True
	gameDisplay.fill(white)
	for y in range(7):
		for x in range(7):
			a = x*80+200
			b = y*80+100
			rect1 = pygame.Rect(a, b,40,40)
			pygame.draw.rect(gameDisplay, blue, rect1)
	for w in range(7):
		letters(AtoJ[w],150,100+80*w,40)
		letters(numbers[w],205+80*w,50,40)
	#NEEDS FIXING
	if event.type == pygame.MOUSEBUTTONDOWN:
		c,d = event.pos
		rect2 = pygame.Rect(c,d,40,40)
		pygame.draw.rect(gameDisplay,red, rect2)

	pygame.display.update()
		
	
	clock.tick(60)

pygame.quit()
quit()