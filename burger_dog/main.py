import pygame
import random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("BURGER DOG!")

FPS = 60
clock = pygame.time.Clock()

# set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 100
STARTING_BURGER_VELOCITY = 3
BURGER_ACCELRATION = .25
BUFFER_DISTANCE = 100

score = 0
burger_points = 0
burgers_eaten = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY
boost_level = STARTING_BOOST_LEVEL
burger_velocity = STARTING_BURGER_VELOCITY

# set color
ORANGE = (246, 170, 54)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set fonts
font = pygame.font.Font('burger_dog/WashYourHand.ttf', 32)

# set text
points_text = font.render("Burger Points: " + str(burger_points), True, ORANGE)
point_rect = points_text.get_rect()
point_rect.topleft = (10, 10)

score_text = font.render("Score: " + str(score), True, ORANGE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render("Burger Dog", True, ORANGE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

eaten_text = font.render("Burgers Eaten: " + str(burgers_eaten), True, ORANGE)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH//2
eaten_rect.y = 50

lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)

gameover_text = font.render("Final Score: " + str(score), True, ORANGE)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to continue", True, ORANGE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

# set sounds and music
bark_sound = pygame.mixer.Sound("burger_dog/bark_sound.wav")
miss_sound = pygame.mixer.Sound("burger_dog/miss_sound.wav")
pygame.mixer.music.load("burger_dog/bd_background_music.wav")

# set images
player_image_right = pygame.image.load("burger_dog/dog_right.png")
player_image_left = pygame.image.load("burger_dog/dog_left.png")
player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

burger_image = pygame.image.load("burger_dog/burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0 or keys[pygame.K_a] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH or keys[pygame.K_d] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right
    if keys[pygame.K_UP] and player_rect.top > 100 or keys[pygame.K_w] and player_rect.top > 100:
        player_rect.y -= player_velocity
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT or keys[pygame.K_s] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    # add boost
    if keys[pygame.K_SPACE] and boost_level > 0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1
        boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY

    # move the burger and update the burger points
    burger_rect.y += burger_velocity
    burger_points = int(
        burger_velocity * (WINDOW_HEIGHT - burger_rect.y + 100))

    # player missed the burger
    if burger_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()
        burger_rect.topleft = (random.randint(
            0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        burger_velocity = STARTING_BURGER_VELOCITY
        player_rect.centerx = WINDOW_WIDTH//2
        player_rect.bottom = WINDOW_HEIGHT
        boost_level = STARTING_BOOST_LEVEL

    # check for collisions
    if player_rect.colliderect(burger_rect):
        score += burger_points
        burgers_eaten += 1
        bark_sound.play()
        burger_rect.topleft = (random.randint(
            0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        burger_velocity += BURGER_ACCELRATION
        boost_level += 25
        if boost_level > STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL

    # update HUD
    score_text = font.render("Score: " + str(score), True, ORANGE)
    eaten_text = font.render(
        "Burgers Eaten: " + str(burgers_eaten), True, ORANGE)
    boost_text = font.render("Boost: " + str(boost_level), True, ORANGE)
    points_text = font.render(
        "Burger Points: " + str(burger_points), True, ORANGE)
    lives_text = font.render("Lives: " + str(player_lives), True, ORANGE)

    # check for gameover
    if player_lives < 0:
        gameover_text = font.render("Final Score: " + str(score), True, ORANGE)
        display_surface.blit(gameover_text, gameover_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        # pause game until player press a key
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    burgers_eaten = 0
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    burger_velocity = STARTING_BURGER_VELOCITY
                    is_paused = False
                # play wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # fill background
    display_surface.fill(BLACK)

    # blit HUD
    display_surface.blit(points_text, point_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)

    pygame.draw.line(display_surface, WHITE, (0, 100), (WINDOW_WIDTH, 100), 3)

    # blit assets
    display_surface.blit(player_image, player_rect)
    display_surface.blit(burger_image, burger_rect)

    # update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()
