gray = (67, 70, 75)
litegray = (129,135,144)

def startscreen():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        mainGame.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Strike Group Simulator", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        mainGame.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        button("Start",300,900,100,50,gray,litegray,loop)
        button("Quit",600,900,100,50,gray,litegray,quit)

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Start", smallText)
        textRect.center = ( (300+(100/2)), (900+(50/2)) )
        mainGame.blit(textSurf, textRect)


        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(mainGame, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(mainGame, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    mainGame.blit(textSurf, textRect)