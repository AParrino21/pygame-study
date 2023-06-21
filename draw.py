import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Draw!")

# color constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

# setting the background color of the display window
display_surface.fill(BLUE)

# draw a line
#line(surface, color, (starting point), (ending point), thickness)
pygame.draw.line(display_surface, RED, (0, 150), (600, 150), 5)

#circle(surface, color, (center), radius, thickness...0 for fill)
pygame.draw.circle(display_surface, GREEN, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 75), 10, 2)

#rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, RED, (0, 0, 100, 100))
pygame.draw.rect(display_surface, CYAN, (150, 10, 100, 100))

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update the display
    pygame.display.update()

# end the game
pygame.quit()