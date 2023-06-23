import pygame, random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("GROUP COLLIDE!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# define classes
class Game():
    """a class to help manage and run our game"""
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group
    
    def update(self):
        self.check_collisions()

    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)


class Knight(pygame.sprite.Sprite):
    """A simple class to represent a player who fights monsters"""
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('intermediate/knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = random.randint(1,5)

    def update(self):
        """update the knight"""
        self.rect.y -= self.velocity


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


#create a monster group and add 12 monsters
monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*64, 10)
    monster_group.add(monster)

#create a knight group and add 12 knight
knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOW_HEIGHT-64)
    knight_group.add(knight)

#create a game object
game = Game(monster_group, knight_group)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the display
    display_surface.fill((0,0,0))

    #update and draw the sprite groups
    monster_group.update()
    monster_group.draw(display_surface)

    knight_group.update()
    knight_group.draw(display_surface)

    game.update()

    #update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()