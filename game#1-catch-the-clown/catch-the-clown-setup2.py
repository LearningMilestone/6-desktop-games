import pygame,random

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
PLAYER_STARTING_LIVES=5
CLOWN_STARTING_VELOCITY=3
CLOWN_ACCELERATION=.5

score=0
player_lives=PLAYER_STARTING_LIVES
clown_velocity=CLOWN_STARTING_VELOCITY
clown_dx=random.choice([-1,1])
clown_dy=random.choice([-1,1])

# Set colors
BLUE=(1,175,209)
YELLOW=(248,231,28)

#Set fonts
font=pygame.font.Font("Franxurter.ttf",32)

#Set text
title_text=font.render("Catch the Clown",True,"BLUE")
title_rect=title_text.get_rect()
title_rect.topleft=(50,10)

score_text=font.render("Score:" + str(score),True,YELLOW)
score_rect=score_text.get_rect()
score_rect.topright=(WINDOW_WIDTH-50,10)

lives_text=font.render("Player Lives:"+str(player_lives),True,YELLOW)
lives_rect=lives_text.get_rect()
lives_rect.topright=(WINDOW_WIDTH-50,40)

game_over_text=font.render("GameOver",True,BLUE,YELLOW)
game_over_text_rect=game_over_text.get_rect()
game_over_text_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

continue_text=font.render("Click Anywhere to play again..",True,YELLOW,BLUE)
continue_text_rect=continue_text.get_rect()
continue_text_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+64)

#set sound and music
hit_sound=pygame.mixer.Sound('click_sound.wav')
miss_sound=pygame.mixer.Sound('miss_sound.wav')
pygame.mixer.music.load('ctc_background_music.wav')

#Set images
background_image=pygame.image.load("background.png")
background_rect=background_image.get_rect()
background_rect.topleft=(0,0)

clown_image=pygame.image.load('clown.png')
clown_rect=clown_image.get_rect()
clown_rect.center =(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)


#The main game loop
running=True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #checking image display--temporary
    #background image
    display_surface.blit(background_image,background_rect)
    #clown image
    display_surface.blit(clown_image,clown_rect)

    #checking text display--temporary
    display_surface.blit(title_text,title_rect)
    display_surface.blit(score_text,score_rect)
    display_surface.blit(lives_text,lives_rect)
    display_surface.blit(game_over_text,game_over_text_rect)
    display_surface.blit(continue_text,continue_text_rect)



    pygame.display.update()
    clock.tick(FPS)


pygame.quit()

