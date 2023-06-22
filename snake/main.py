import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("SNAKE!")

# set FPS and Clock
FPS = 20
clock = pygame.time.Clock()

# set game values
SNAKE_SIZE = 20



# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()