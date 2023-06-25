import pygame

# intialize pygame
pygame.init()

#use 2D vectors
vector = pygame.math.Vector2

# create a display surface (title size is 32x32 so window is divisable by the tile sizes)
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("ANIMATIONS!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#define classes
class Tile(pygame.sprite.Sprite):
    """class to read and create individual tiles and place them in the display"""
    def __init__(self, x, y, image_int, main_group, sub_group=""):
        super().__init__()
        # load in the correct image and add it to the correct sub group
        if image_int == 1:
            self.image = pygame.image.load("advanced_study/assets/dirt.png")
        elif image_int == 2:
            self.image = pygame.image.load('advanced_study/assets/grass.png')
            sub_group.add(self)
            print(sub_group)
        elif image_int == 3:
            self.image = pygame.image.load('advanced_study/assets/water.png')
            sub_group.add(self)
        
        #add every time to main group
        main_group.add(self)

        #get the rect of the image and position it within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


class Player(pygame.sprite.Sprite):
    """player class that a user can control"""
    def __init__(self, x, y, grass_tiles, water_tiles):
        super().__init__()

        #animation frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []

        #appending images into a list
        #moving right
        for i in range(1, 9):
            self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(f"advanced_study/assets/boy/Run ({i}).png"), (64,64)))

        #moving left
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #idle right
        for i in range(1, 9):
            self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(f"advanced_study/assets/boy/Idle ({i}).png"), (64,64)))

        #idle left
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))


        self.current_sprite = 0
        self.image = self.move_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y + 32)

        self.starting_x = x
        self.starting_y = y
        
        self.grass_tiles = grass_tiles
        self.water_tiles = water_tiles

        #kinematics vectors (first value is the x, second valuse is the y)
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0,0)

        #kinematic constants
        self.HORIZONTAL_ACCELERATION = 1
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.5 #GRAVITY
        self.VERTICAL_JUMP_SPEED = 15 #determines how high we can jump


    def update(self):
        self.move()
        self.collision_check()
    

    def move(self):
        #set the acceleration vector to (0,0) so there it initially no acceleration
        #if there is no force(key press) acting on the player then acceleration should be 0
        #vertical acceleration is always present
        self.acceleration = vector(0,self.VERTICAL_ACCELERATION)
        # if the user is pressing a key, set the x-component of the acceleration vector to a non zero value
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, .2)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, .2)
        else:
            if self.velocity.x > 0:
                self.animate(self.idle_right_sprites, .3)
            else:
                self.animate(self.idle_left_sprites, .3)

        #calculated new kinematics values
        #update acceleration to take friction into account
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        #update the velocity
        self.velocity += self.acceleration
        #update the position with new velcoity plus half the acceleration to reach top speed
        self.position += self.velocity + 0.5*self.acceleration

        #update new rect based on kinematics calcuations and add wrap around when player walks off screen
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0
        self.rect.bottomleft = self.position


    def collision_check(self):
        #check for collisions with grass tiles
        collided_platforms = pygame.sprite.spritecollide(self, self.grass_tiles, False)
        if collided_platforms:
            #only snap to platform if falling down(velocity y is moving in positive direction or down the screen)
            if self.velocity.y > 0:
                self.position.y = collided_platforms[0].rect.top +3
                self.velocity.y = 0

        #check for collisions with water tiles
        if pygame.sprite.spritecollide(self, self.water_tiles, False):
            print("You cant swim")
            self.position = vector(self.starting_x, self.starting_y)
            self.velocity = vector(0,0)
    
    
    def jump(self):
        #only jump if on grass tile
        if pygame.sprite.spritecollide(self, self.grass_tiles, False):
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED

    def animate(self, sprite_list, speed):
        #loop through the sprite list changing the current sprite
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        self.image = sprite_list[int(self.current_sprite)]

#create sprite groups
main_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
my_player_group = pygame.sprite.Group()

#Create the title map -----> 0 will represent no tile, 1 -> dirt, 2 -> grass, 3 -> water, 4 -> player
#20 rows and 30 columns
tile_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,1,1,1,1,1,1],
]

# create each tile from the tile map
for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, main_tile_group)
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, main_tile_group, grass_tile_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, main_tile_group, water_tile_group)
        elif tile_map[i][j] == 4:
            my_player = Player(j*32, i*32, grass_tile_group, water_tile_group)
            my_player_group.add(my_player)

# load in the background
backgroun_image = pygame.image.load("advanced_study/assets/background.png")
backgroun_rect = backgroun_image.get_rect()
backgroun_rect.topleft = (0,0)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # checking for player space bar tap for jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.jump()
    
    #blit background image
    display_surface.blit(backgroun_image, backgroun_rect)

    #draw tiles
    main_tile_group.draw(display_surface)

    #update and draw sprites
    my_player_group.update()
    my_player_group.draw(display_surface)

    #update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()