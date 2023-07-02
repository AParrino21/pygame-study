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
    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        super().__init__()

        #constant variables
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8 #GRAVITY
        self.VERTICAL_JUMP_SPEED = 18
        self.STARTING_HEALTH = 100

        #animation frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []
        self.jump_right_sprites = []
        self.jump_left_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []

        #moving animations
        for i in range(1,10):
            self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/player/run/Run ({i}).png'), (64,64)))
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #idling animations
        for i in range(1,10):
            self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/player/idle/Idle ({i}).png'), (64,64)))
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #jumping animations
        for i in range(1,10):
            self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/player/jump/Jump ({i}).png'), (64,64)))
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False)) 

        #attack animations
        for i in range(1,10):
            self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(f'zombie/images/player/attack/Attack ({i}).png'), (64,64)))
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False)) 

        #load image and get rect
        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x,y)

        #attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        #animation booleans
        self.animate_jump = False
        self.animate_fire = False

        #load sounds
        self.jump_sound = pygame.mixer.Sound('zombie/sounds/jump_sound.wav')
        self.slash_sound = pygame.mixer.Sound('zombie/sounds/slash_sound.wav')
        self.portal_sound = pygame.mixer.Sound('zombie/sounds/portal_sound.wav')
        self.hit_sound = pygame.mixer.Sound('zombie/sounds/player_hit.wav')

        #kinematics vectors
        self.position = vector(x,y)
        self.velocity = vector(0,0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y


    def update(self):
        self.move()
        self.check_collisions()
        self.check_animations()

    def move(self):
        #set the acceleration vector
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #if a user is pressing a key, set the x-component of the acceleration to be non zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, .5)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, .5)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .5)
            else:
                self.animate(self.idle_left_sprites, .5)

        #calculate new kinematic values
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

        #update rect based on kinematic calculations and add wrap around movement(one side of screen to the other)
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
        
        self.rect.bottomleft = self.position

    def check_collisions(self):
        #collision check between player and platforms when falling
        if self.velocity.y > 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.position.y = collided_platforms[0].rect.top + 1
                self.velocity.y = 0

        #collision check between players head and platform if jumping up
        if self.velocity.y < 0:
            collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
            if collided_platforms:
                self.velocity.y = 0
                while pygame.sprite.spritecollide(self, self.platform_group, False):
                    self.position.y += 1
                    self.rect.bottomleft = self.position

        #collision checks with portals
        if pygame.sprite.spritecollide(self, my_portal_group, False):
            # self.portal_sound.play()
            #determine which portal you are moving to
            #left and right
            if self.position.x > WINDOW_WIDTH//2:
                self.position.x = 86
            else:
                self.position.x = WINDOW_WIDTH - 184
            #top and bottom
            if self.position.y > WINDOW_HEIGHT//2:
                self.position.y = 64
            else:
                self.position.y = WINDOW_HEIGHT - 132
            
            self.rect.bottomleft = self.position

    def check_animations(self):
        #animate the players jump
        if self.animate_jump:
            if self.velocity.x > 0:
                self.animate(self.jump_right_sprites, .1)
            else:
                self.animate(self.jump_left_sprites, .1)
        
        #animate the player attach
        if self.animate_fire:
            if self.velocity.x > 0:
                self.animate(self.attack_right_sprites, .25)
            else:
                self.animate(self.attack_left_sprites, .25)
        

    def jump(self):
        #only jump if on a platform
        if pygame.sprite.spritecollide(self, my_plateform_group, False):
            # self.jump_sound.play()
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
            self.animate_jump = True

    def fire(self):
        # self.slash_sound.play()
        Bullet(self.rect.centerx, self.rect.centery, self.bullet_group, self)
        self.animate_fire = True

    def reset(self):
        self.position = vector(self.starting_x, self.starting_y)
        self.rect = self.position

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            #end jump animation
            if self.animate_jump:
                self.animate_jump = False
            #end the attack aniamtion
            if self.animate_fire:
                self.animate_fire = False

        self.image = sprite_list[int(self.current_sprite)]


class Bullet(pygame.sprite.Sprite):
    """class for projectile launched by the player"""
    def __init__(self, x, y, bullet_group, player):
        super().__init__()

        #set constants
        self.VELOCITY = 20
        self.RANGE = 500

        #load image and get the rect
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load('zombie/images/player/slash.png'), (32,32))
        else:
            self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load('zombie/images/player/slash.png'),True, False),(32,32))
            self.VELOCITY = -1*self.VELOCITY
        
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.starting_x = x

        bullet_group.add(self)

    def update(self):
        #move the bullet
        self.rect.x += self.VELOCITY

        #if the bullet has passed the range, kill it
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()


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
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
        elif tile_map[i][j] == 9:
            my_player = Player(j*32 -32, i*32 +32, my_plateform_group, my_portal_group, my_bullet_group)
            my_player_group.add(my_player)

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
        if event.type == pygame.KEYDOWN:
            #player wants to jum
            if event.key == pygame.K_SPACE:
                my_player.jump()
            #player wants to fire
            if event.key == pygame.K_RSHIFT:
                my_player.fire()

    # blit background
    display_surface.blit(background_image,background_rect)

    #update and draw main tile group to screen
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)

    # update and draw sprite groups
    my_portal_group.update()
    my_portal_group.draw(display_surface)

    #update and draw player
    my_player_group.update()
    my_player_group.draw(display_surface)

    #update and draw the bullet
    my_bullet_group.update()
    my_bullet_group.draw(display_surface)

    #update and draw the game
    my_game.update()
    my_game.draw()

    # update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()