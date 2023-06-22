import pygame

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("BURGER DOG!")

FPS = 60
clock = pygame.time.Clock()

#set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELRATION = .25

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

#set color
ORANGE = (246,170,54)
BLACK = (0,0,0)
WHITE = (255,255,255)

#set fonts
font = pygame.font.Font('burger_dog/WashYourHand.ttf', 32)

#set text
points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)



# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update the display
    pygame.display.update()

# end the game
pygame.quit()