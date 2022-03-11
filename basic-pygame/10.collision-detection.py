import pygame
import random

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection")

##pygame clock
FPS=60
clock=pygame.time.Clock()

##pygame velocity
VELOCITY=5

#load image
dragon_image=pygame.image.load('dragon-right.png')
dragon_rect=dragon_image.get_rect()
dragon_rect.topleft=(25,25)


coin_image=pygame.image.load('coin.png')
coin_rect=coin_image.get_rect()
coin_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

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
    keys=pygame.key.get_pressed()
    #Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY

    #check for collision between 2 rects
    if dragon_rect.colliderect(coin_rect):
        print("colided")
        #Moving coin randomly on collision
        coin_rect.x=random.randint(0,WINDOW_WIDTH-32)
        coin_rect.y=random.randint(0,WINDOW_HEIGHT-32)
        display_surface.blit(coin_image,coin_rect)


    display_surface.fill((0,0,0))
    #draw image rectangles
    pygame.draw.rect(display_surface,(0,255,0),dragon_rect,4)
    pygame.draw.rect(display_surface,(255,255,0),coin_rect,4)

    #blit images
    display_surface.blit(dragon_image,dragon_rect)
    display_surface.blit(coin_image,coin_rect)

    pygame.display.update()
    clock.tick(FPS)
#End the game
pygame.quit()


