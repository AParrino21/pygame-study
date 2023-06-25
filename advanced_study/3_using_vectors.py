import pygame

# intialize pygame
pygame.init()

#use 2D vectors
vector = pygame.math.Vector2

# create a display surface (title size is 32x32 so window is divisable by the tile sizes)
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("VECTOR!")

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
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("advanced_study/assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y + 32)

        #kinematics vectors (first value is the x, second valuse is the y)
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0,0)

        #kinematic constants
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15

    def update(self):
        #set the acceleration vector to (0,0) so there it initially no acceleration
        #if there is no force(key press) acting on the player then acceleration should be 0
        self.acceleration = vector(0,0)
        # if the user is pressing a key, set the x-component of the acceleration vector to a non zero value
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0 or keys[pygame.K_a] and self.rect.left > 0:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH or keys[pygame.K_d] and self.rect.right < WINDOW_WIDTH:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION

        #calculated new kinematics values
        #update acceleration to take friction into account
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        #update the velocity
        self.velocity += self.acceleration
        #update the position with new velcoity plus half the acceleration to reach top speed
        self.position += self.velocity + 0.5*self.acceleration
        #update new rect based on kinematics calcuations
        self.rect.bottomleft = self.position
        self.rect.y += 32

#create sprite groups
main_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
my_player_group = pygame.sprite.Group()

#Create the title map -----> 0 will represent no tile, 1 -> dirt, 2 -> grass, 3 -> water, 4 -> player
#20 rows and 30 columns
tile_map = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,4,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
            my_player = Player(j*32, i*32)
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