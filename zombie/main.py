import pygame, random

# use 2D vector
vector = pygame.math.Vector2

# intialize pygame
pygame.init()

# set a display surface (tile size is 32x32 so 1280/32 = 40 tiles wide and 736/32 = 23 tiles hig\)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Zombie Knight!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# define classes
class Game():
    """class to help manage the gameplay"""
    def __init__(self):
        #set constant variables
        self.STARTING_ROUND_TIME = 30

        #set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME

        #set fonts
        self.title_font = pygame.font.Font('zombie/fonts/Poultrygeist.ttf', 48)
        self.HUD_font = pygame.font.Font('zombie/fonts/Pixel.ttf', 24)

    def update(self):
        #update the round time every second
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

    def draw(self):
        #set colors
        WHITE = (255,255,255)
        GREEN = (25,200,25)

        #set text
        score_text = self.HUD_font.render('Score: ' + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render('Health: ' + str(100), True, WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)

        title_text = self.title_font.render('Zombie Knight', True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render('Night: ' + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render('Sunrise in: ' + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)

        #draw the HUD
        display_surface.blit(score_text,score_rect)
        display_surface.blit(health_text,health_rect)
        display_surface.blit(title_text,title_rect)
        display_surface.blit(round_text,round_rect)
        display_surface.blit(time_text,time_rect)


    def add_zombie(self):
        pass

    def check_collisions(self):
        pass

    def check_round_completion(self):
        pass

    def check_gameover(self):
        pass

    def start_new_round(self):
        pass

    def pause_game(self):
        pass
    
    def reset_game(self):
        pass


class Tile(pygame.sprite.Sprite):
    """class to represent a 32x32 tile"""
    def __init__(self,x, y, image_int, main_group, sub_group = ""):
        super().__init__()
        #load in the image and add it to the correct sub group
        #dirt
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load('zombie/images/tiles/Tile (1).png'), (32,32))
        elif image_int ==2:
            self.image = pygame.transform.scale(pygame.image.load('zombie/images/tiles/Tile (2).png'), (32,32))
            sub_group.add(self)
        elif image_int ==3:
            self.image = pygame.transform.scale(pygame.image.load('zombie/images/tiles/Tile (3).png'), (32,32))
            sub_group.add(self)
        elif image_int ==4:
            self.image = pygame.transform.scale(pygame.image.load('zombie/images/tiles/Tile (4).png'), (32,32))
            sub_group.add(self)
        elif image_int ==5:
            self.image = pygame.transform.scale(pygame.image.load('zombie/images/tiles/Tile (5).png'), (32,32))
            sub_group.add(self)
        
        #add all tiles to main group
        main_group.add(self)

        #get the rect of the image and the position its in
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


class Player(pygame.sprite.Sprite):
    """class the user can control"""
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def check_animations(self):
        pass

    def jump(self):
        pass

    def fire(self):
        pass

    def reset(self):
        pass

    def animate(self):
        pass


class Bullet(pygame.sprite.Sprite):
    """class for projectile launched by the player"""
    def __init__(self):
        pass

    def update(self):
        pass


class Zombie(pygame.sprite.Sprite):
    """enemy class that moves across the screen"""
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def check_animations(self):
        pass

    def animate(self):
        pass


class RubyMaker(pygame.sprite.Sprite):
    """a tile that is animated - a ruby will be generated here"""
    def __init__(self, x, y, main_group):
        super().__init__()

        #animation frames
        self.rub_sprites = []

        #rotating
        for i in range(7):
            self.rub_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/ruby/tile00{i}.png'), (64,64)))
        
        # load image and get sprite
        self.current_sprite = 0
        self.image = self.rub_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        # add to the main group for drawing purposes
        main_group.add(self)

    def update(self):
        self.animate(self.rub_sprites, .25)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]


class Ruby (pygame.sprite.Sprite):
    """a class a player must collect to earn points"""
    def __init__(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def check_collisions(self):
        pass

    def animate(self):
        pass


class Portal(pygame.sprite.Sprite):
    """class that if collided with will transport you"""
    def __init__(self, x, y, color, portal_group):
        super().__init__()
        # animations frames
        self.portal_sprites = []

        # portal animation
        if color == "green":
            for i in range(22):
                if i < 10:
                    i = "0" + str(i)
                    self.portal_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/portals/green/tile0{i}.png'),(72,72)))
                else:
                    self.portal_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/portals/green/tile0{i}.png'),(72,72)))
        elif color == "purple":
            for i in range(22):
                if i < 10:
                    i = "0" + str(i)
                    self.portal_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/portals/purple/tile0{i}.png'),(72,72)))
                else:
                    self.portal_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/portals/purple/tile0{i}.png'),(72,72)))

        #load and image and get rect
        self.current_sprite =random.randint(0, len(self.portal_sprites) -1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        #add to the portal group
        portal_group.add(self)
    
    def update(self):
        self.animate(self.portal_sprites, .2)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]

# create stripe groups
my_main_tile_group = pygame.sprite.Group()
my_plateform_group = pygame.sprite.Group()

my_player_group = pygame.sprite.Group()
my_bullet_group = pygame.sprite.Group()

my_zombie_group = pygame.sprite.Group()

my_portal_group = pygame.sprite.Group()
my_ruby_group = pygame.sprite.Group()

# create the tile map ---> 
# 0 -> no tile, 1 -> dirt, 2-5 -> platforms, 6 -> ruby maker, 7-8 -> portals, 9 -> player
# 23 rows and 40 columns
tile_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,6,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,0,0,0,0,0,0,0,0,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

#generate the tile object from the tile map
for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        #dirt tile
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, my_main_tile_group)

        #platform tile
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, my_main_tile_group, my_plateform_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, my_main_tile_group, my_plateform_group)
        elif tile_map[i][j] == 4:
            Tile(j*32, i*32, 4, my_main_tile_group, my_plateform_group)
        elif tile_map[i][j] == 5:
            Tile(j*32, i*32, 5, my_main_tile_group, my_plateform_group)
        elif tile_map[i][j] == 6:
            RubyMaker(j*32, i*32, my_main_tile_group)
        elif tile_map[i][j] == 7:
            Portal(j*32, i*32, "green", my_portal_group)
        elif tile_map[i][j] == 8:
            Portal(j*32, i*32, "purple", my_portal_group)
            

        #ruby maker
        elif tile_map[i][j] == 6:
            pass

        #portal maker
        elif tile_map[i][j] == 7:
            pass
        elif tile_map[i][j] == 8:
            pass

        #create player
        elif tile_map[i][j] == 9:
            pass


# load in background image (we must resize image)
background_image = pygame.transform.scale(pygame.image.load('zombie/images/background.png'), (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

#create a game
my_game = Game()

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # blit background
    display_surface.blit(background_image,background_rect)

    #update and draw main tile group to screen
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)

    # update and draw sprite groups
    my_portal_group.update()
    my_portal_group.draw(display_surface)

    #update and draw the game
    my_game.update()
    my_game.draw()

    # update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()