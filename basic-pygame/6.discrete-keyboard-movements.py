import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Keyboard Movements")

#Set game values
VELOCITY=10

#Load in Images
dragon_image=pygame.image.load("dragon-right.png")
dragon_rect=dragon_image.get_rect()
dragon_rect.centerx=WINDOW_WIDTH//2
dragon_rect.bottom=WINDOW_HEIGHT

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
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("left key pressed")
                dragon_rect.x-=VELOCITY
            elif event.key==pygame.K_RIGHT:
                print("right key pressed")
                dragon_rect.x+=VELOCITY
            elif event.key==pygame.K_UP:
                print("up key pressed")
                dragon_rect.y-=VELOCITY
            elif event.key==pygame.K_DOWN:
                print("down key pressed")
                dragon_rect.y+=VELOCITY
    #Fill the display surface with background color
    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image,dragon_rect)
    pygame.display.update()

#End the game
pygame.quit()


