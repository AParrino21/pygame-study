import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("BLITTING IMAGES!")

# create images returns a surface object with the image on it
# we can then get the rect of the surface and use the rect to position the image
curly = pygame.image.load("basic_study/curly.png")
curly = pygame.transform.scale(curly, (curly.get_width()))
curly_rect = curly.get_rect()
curly_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)



# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) a surface object at the given coords to our display
    display_surface.blit(curly, curly_rect)

    #update the display
    pygame.display.update()

# end the game
pygame.quit()
