import pygame, random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("MONSTER WRANGLER!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#define classes
class Game():
    """class to control gameplay"""
    def __init__(self):
        """initialize game"""
        pass
    
    def update(self):
        """update game object"""
        pass
    
    def draw(self):
        """draw the HUD and others to the displays"""
        pass

    def check_collisions(self):
        """check for collisions between player and monster"""
        pass

    def start_new_round(self):
        """populate board with new monsters"""
        pass

    def choose_new_target(self):
        """choose a new target monster for the player"""
        pass
    
    def pause_game(self):
        """pause the game"""
        pass

    def reset_game(self):
        """reset game"""
        pass


class Player(pygame.sprite.Sprite):
    """player class that the user can control"""
    def __init__(self):
        """initialize player"""
        super().__init__()
        self.image = pygame.image.load('monster_wrangler/knight.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound('monster_wrangler/catch.wav')
        self.die_sound = pygame.mixer.Sound('monster_wrangler/die.wav')
        self.warp_sound = pygame.mixer.Sound('monster_wrangler/warp.wav')

    def update(self):
        """update player object"""
        keys = pygame.key.get_pressed()
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

    def warp(self):
        """warp the player to the bottom of the safe zone"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset_player(self):
        """if player dies resets to bottom of screen"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT


class Monster(pygame.sprite.Sprite):
    """class to create enemy monster objects"""
    def __init__(self, x, y, image, monster_type):
        """initialize game"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #monster type is an int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        #set random motion
        self.dx =random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    
    def update(self):
        """update monster"""
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #bounce the monster off the edges of the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.dy = -1*self.dy            


#create a player group and player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#create a monster group
my_monster_group = pygame.sprite.Group()
#test monster
monster = Monster(500,500, pygame.image.load('monster_wrangler/green_monster.png'), 1)
my_monster_group.add(monster)
monster = Monster(100,500, pygame.image.load('monster_wrangler/blue_monster.png'), 0)
my_monster_group.add(monster)

#create a game object
my_game = Game()


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the display
    display_surface.fill((0,0,0))

    #update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    my_game.update()
    my_game.draw()

    #update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()