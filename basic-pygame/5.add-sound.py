import pygame

#initialize pygame
pygame.init()

#create a display surface & set its captions
WINDOW_WIDTH=600
WINDOW_HEIGHT=300
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

##Add sound from leshy labs
##Loading sound effects - create sound objects
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

#play sound
sound_1.play()

pygame.time.delay(3000)
sound_2.play()


pygame.time.delay(2000)
#change the volume of sound

sound_2.set_volume(.1)
sound_2.play()

#play background music
pygame.mixer.music.load('music.wav')
# arguments:infinite loop or number of times , starting time
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(5000)
pygame.play.music.stop()

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
#End the game
pygame.quit()


