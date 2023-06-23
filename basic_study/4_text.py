import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("TEXT!")

# color constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)

#define fonts
system_font = pygame.font.SysFont('calibri', 64)

#define text
system_text = system_font.render("Goobis Anubis!!!", True, GREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) a surface object at the given coords to our display
    display_surface.blit(system_text, system_text_rect)

    #update the display
    pygame.display.update()

# end the game
pygame.quit()