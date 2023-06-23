import pygame, random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("SPRITE CLASSES!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# define classes
class Monster(pygame.sprite.Sprite):
    """A simple class to represent a spooky monster"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('intermediate/blue_monster.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = random.randint(1,5)

    # MUST be named update
    def update(self):
        """update and move the monster"""
        self.rect.y += self.velocity


#create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    monster_group.add(monster)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the display
    display_surface.fill((0,0,0))

    #update and draw the assets
    monster_group.update()
    monster_group.draw(display_surface)

    #update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()
