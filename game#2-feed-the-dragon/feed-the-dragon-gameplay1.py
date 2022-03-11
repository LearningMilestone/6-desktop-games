import pygame
import random

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

#set FPS value
FPS=60
clock=pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY


#set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED=(255,0,0)

#set font
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#set text
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#set sound & images

coin_sound = pygame.mixer.Sound("coin_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("ftd_background_music.wav")

#Set images
#load image
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

#The main game loop
running=True
while running:
    #pygame.mixer.music.play(-1)
    #Loop through a list of events which have occured on pygame surface window
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            #print("hi")
            #turn off while loop
            running=False
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_rect.top>64:
        player_rect.top-=PLAYER_VELOCITY

    if keys[pygame.K_DOWN] and player_rect.bottom<WINDOW_HEIGHT:
        player_rect.bottom+=PLAYER_VELOCITY


    # if keys[pygame.K_LEFT] and player_rect.left>0:
    #         player_rect.left-=PLAYER_VELOCITY
    #
    # if keys[pygame.K_RIGHT] and player_rect.right<WINDOW_WIDTH:
    #     player_rect.right+=PLAYER_VELOCITY

    #Move The coin
    if coin_rect.x<0:
        player_lives-=1
        coin_rect.x=WINDOW_WIDTH+BUFFER_DISTANCE
        coin_rect.y=random.randint(64,WINDOW_HEIGHT - 32)
        miss_sound.play()
    else:
        coin_rect.x-=coin_velocity
    #Check for Collisions
    if player_rect.colliderect(coin_rect):
        print("collided")
        score+=1
        coin_velocity+=COIN_ACCELERATION
        #score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
        coin_sound.play()
        coin_rect.x=WINDOW_WIDTH+BUFFER_DISTANCE
        coin_rect.y=random.randint(64,WINDOW_HEIGHT - 32)
        score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
        lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)


    display_surface.fill(RED)

    #Blit the HUD to screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)

    #Blit assets to screen
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)

    pygame.display.update()
    clock.tick(FPS)
#End the game
pygame.quit()


