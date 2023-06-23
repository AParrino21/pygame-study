import pygame, random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("SPRITE COLLIDE!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# define classes
class Player(pygame.sprite.Sprite):
    """A simple class to represent a player who fights monsters"""
    def __init__(self, x, y, collided_group):
        super().__init__()
        self.image = pygame.image.load('intermediate/knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5
        self.collided_group = collided_group

    def update(self):
        """update the player"""
        self.move()
        self.check_collision()
    
    def move(self):
        """move the player"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity

    def check_collision(self):
        """check for collisions between player and monster group"""
        # .spritecollide(self, group to collide with, whether or not the collison destorys that object)
        pygame.sprite.spritecollide(self, self.collided_group, True)

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

#create a player group
player_group = pygame.sprite.Group()
player = Player(500, 500, monster_group)
player_group.add(player)


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

    player_group.update()
    player_group.draw(display_surface)

    #update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()