import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("MOUSE MOVEMENT!")

#load in image
curly = pygame.image.load('basic_study/curly.png')
curly_rect = curly.get_rect()
curly_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #move based on mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            curly_rect.centerx = mouse_x
            curly_rect.centery = mouse_y

        #where ever the mouse goes, the image goes
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     curly_rect.centerx = mouse_x
        #     curly_rect.centery = mouse_y

        #drags the object when the mouse button is clicked
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            curly_rect.centerx = mouse_x
            curly_rect.centery = mouse_y


    # fill the display surface to cover old images
    display_surface.fill((0,0,0))

    # Blit (copy) a surface object at the given coords to our display
    display_surface.blit(curly, curly_rect)

    #update the display
    pygame.display.update()

# end the game
pygame.quit()