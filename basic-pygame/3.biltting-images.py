import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images")

#Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)

#change display surface color
display_surface.fill(RED)

#create images - returns surface object with images drawn on it
#we can then get rect of surface to use rect to place images on the display surface

#load an image
dragon_left_img=pygame.image.load("dragon-left.png")
dragon_left_rect=dragon_left_img.get_rect()
dragon_left_rect.topleft=(0,0)

dragon_right_img=pygame.image.load("dragon-right.png")
dragon_right_rect=dragon_right_img.get_rect()
dragon_right_rect.topright=(WINDOW_WIDTH,0)

#draw a line
pygame.draw.line(display_surface,WHITE,(0,80),(WINDOW_WIDTH,80),8)

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

    #Blit(Copy) the given image object at the given location
    display_surface.blit(dragon_right_img,dragon_right_rect)
    display_surface.blit(dragon_left_img,dragon_left_rect)

    #update the display
    pygame.display.update()

#End the game
pygame.quit()


