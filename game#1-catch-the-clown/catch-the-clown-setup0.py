import pygame

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH=945
WINDOW_HEIGHT=600
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Catch The Clown!")

#Set FPS and Clock
FPS=60
clock=pygame.time.Clock()

# Set game values

# Set colors

#Set fonts


#Set text

#set sound and music

#Set images

#The main game loop
running=True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()

