import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("AUDIO!")

#Load sound effects
sound1 = pygame.mixer.Sound('basic_study/sound.wav')
sound2 = pygame.mixer.Sound('basic_study/sound2.wav')

#play the sound effects
sound1.play()
pygame.time.delay(2000)
sound2.play()
pygame.time.delay(2000)

#change the volume of sound effect
sound2.set_volume(.1)
sound2.play()

#load background music
pygame.mixer.music.load('basic_study/soundBG.wav')
#play and stop the music(how many time to play: -1 is infinite and 0.0 is start time)
pygame.mixer.music.play(-1, 0.0)
# play for 5 seconds then stop
pygame.time.delay(5000)
pygame.mixer.music.stop()


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# end the game
pygame.quit()