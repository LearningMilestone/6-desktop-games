import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Drawing on surface")

#Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)

#change background colour of display surface
display_surface.fill(BLUE)

#Draw various shapes on display
#line(surface,color,starting coordinate,end coordinate,thickness)
pygame.draw.line(display_surface,RED,(0,0),(95,95),5)

#circle
pygame.draw.circle(display_surface,CYAN,(100,100),50,0)
pygame.draw.circle(display_surface,CYAN,(300,200),50,10)

#rectangle
pygame.draw.rect(display_surface,YELLOW,(90,200,50,60),0)

#The main game loop
running=True
while running:
    #Loop through a list of events which have occured on pygame surface window
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            #print("hi")
            #turn off while loop
            running=False
    #update the display
    pygame.display.update()

#End the game
pygame.quit()

