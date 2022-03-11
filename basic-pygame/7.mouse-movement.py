import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Mouse Movement")

#load image
dragon_image=pygame.image.load('dragon-right.png')
dragon_rect=dragon_image.get_rect()

# print(dragon_rect)
dragon_rect.topleft=(25,25)
# print(dragon_rect)

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
    #Move based on mouse clicks
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x=event.pos[0]
            mouse_y=event.pos[1]
            dragon_rect.centerx=mouse_x
            dragon_rect.centery=mouse_y
        #Drag the object when mouse is clicked
        if event.type==pygame.MOUSEMOTION and event.buttons[0]==1:
            print(event)
            mouse_x=event.pos[0]
            mouse_y=event.pos[1]
            dragon_rect.centerx=mouse_x
            dragon_rect.centery=mouse_y


    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image,dragon_rect)
    pygame.display.update()

#End the game
pygame.quit()


