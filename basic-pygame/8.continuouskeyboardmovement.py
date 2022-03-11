import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Movement")

#pygame constants
##pygame clock
FPS=60
clock=pygame.time.Clock()

##pygame velocity
VELOCITY=5

#load image
dragon_image=pygame.image.load('dragon-right.png')
dragon_rect=dragon_image.get_rect()
dragon_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

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

    #Get a list of keys currently being held
    keys=pygame.key.get_pressed()
    # print(keys)
    if keys[pygame.K_LEFT]:
        dragon_rect.x-=VELOCITY

    if keys[pygame.K_RIGHT]:
         dragon_rect.x+=VELOCITY

    if keys[pygame.K_UP]:
         dragon_rect.y-=VELOCITY

    if keys[pygame.K_DOWN]:
         dragon_rect.y+=VELOCITY

    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image,dragon_rect)

    pygame.display.update()
    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()


