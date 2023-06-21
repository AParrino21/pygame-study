import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("MOVEMENT!")

#set game values
VELOCITY = 10

#load in image
curly = pygame.image.load('curly.png')
curly_rect = curly.get_rect()
curly_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                curly_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                curly_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                curly_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                curly_rect.y += VELOCITY

    # fill the display surface to cover old images
    display_surface.fill((0,0,0))

    # Blit (copy) a surface object at the given coords to our display
    display_surface.blit(curly, curly_rect)

    #update the display
    pygame.display.update()

# end the game
pygame.quit()