import pygame, random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("COLLISION DETECTION!")

#set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#set game values
VELOCITY = 5

#load in image
curly = pygame.image.load('curly.png')
curly_rect = curly.get_rect()
curly_rect.center = (150, WINDOW_HEIGHT//2)

phill = pygame.image.load('phill2.png')
phill_rect = phill.get_rect()
phill_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #get list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    #move the image continuously
    if keys[pygame.K_a] and curly_rect.left > 0:
        curly_rect.x -= VELOCITY
    if keys[pygame.K_d] and curly_rect.right < WINDOW_WIDTH:
        curly_rect.x += VELOCITY
    if keys[pygame.K_w] and curly_rect.top > 0:
        curly_rect.y -= VELOCITY
    if keys[pygame.K_s] and curly_rect.bottom < WINDOW_HEIGHT:
        curly_rect.y += VELOCITY    

    #check for collision between two rects
    if curly_rect.colliderect(phill_rect):
        print("hit")   
        #moves phill_rect to a random place after collision
        phill_rect.x = random.randint(0, WINDOW_WIDTH - 200)
        phill_rect.y = random.randint(0, WINDOW_HEIGHT - 200)

    #update the display
    pygame.display.update()

    # fill the display surface to cover old images
    display_surface.fill((0,0,0))

    #draw rectangles to represent the rects of each object
    pygame.draw.rect(display_surface, (255,0,0), curly_rect, 1)
    pygame.draw.rect(display_surface, (255,255,0), phill_rect, 1)

    # Blit (copy) a surface object at the given coords to our display
    display_surface.blit(curly, curly_rect)  
    display_surface.blit(phill, phill_rect)           

    #update the display
    pygame.display.update()

    #tick the clock to only run this loop for as many times as the FPS lets it instead of how fast the computer is
    clock.tick(FPS)

# end the game
pygame.quit()