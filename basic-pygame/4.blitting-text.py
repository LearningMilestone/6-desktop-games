import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Text")

#Define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

#See all available system fonts
font=pygame.font.get_fonts()
print(font)
# for custom font,download ttf from https://www.fontspace.com/ website
#load font

#Define system fonts
system_font=pygame.font.SysFont('calibri',64)
#Define custom font
custom_font=pygame.font.Font('ShortBaby-Mg2w.ttf',32)

#Adding text in pygame is similar to adding images
#Define text
#This returns surface
system_text=system_font.render("Dragon's Rule !",True,GREEN,DARKGREEN)
#get rect of the text surface
system_text_rect=system_text.get_rect()

#positioning
system_text_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)


#Define text
#This returns surface
custom_text=custom_font.render(" Move the dragon soon ! ",True,GREEN)
#get rect of the text surface
custom_text_rect=custom_text.get_rect()

#positioning
custom_text_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+100)

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
    #blit the text to the display surface
    display_surface.blit(system_text,system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    pygame.display.update()
#End the game
pygame.quit()


