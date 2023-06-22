import pygame
import random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Feed the Dragon!")

# set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

# set game values
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY

# set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set fonts
font = pygame.font.Font('game_1/assets/AttackGraffiti.ttf', 32)

# set text
score_text = font.render("Score " + str(score), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("Feed the Dragon", True, GREEN, WHITE)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = WINDOW_WIDTH//2
title_text_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives),
                         True, GREEN, DARK_GREEN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

game_over_text = font.render("GAME OVER", True, GREEN, DARK_GREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render(
    "Press any key to play again", True, GREEN, DARK_GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

# set sounds and music
coin_sound = pygame.mixer.Sound("game_1/assets/coin_sound.wav")
miss_sound = pygame.mixer.Sound("game_1/assets/miss_sound.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("game_1/assets/ftd_background_music.wav")

# set images
player_image = pygame.image.load("game_1/assets/dragon_right.png")
player_image_rect = player_image.get_rect()
player_image_rect.left = 32
player_image_rect.centery = WINDOW_HEIGHT//2

coin_image = pygame.image.load("game_1/assets/coin.png")
coin_image_rect = coin_image.get_rect()
coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

# main game loop

# load in background music
pygame.mixer.music.play(-1, 0.0, 5000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check to see if user wants to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_image_rect.top > 64:
        player_image_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_s] and player_image_rect.bottom < WINDOW_HEIGHT:
        player_image_rect.y += PLAYER_VELOCITY

    # move the coin
    if coin_image_rect.x < 0:
        # player missed the coin
        player_lives -= 1
        miss_sound.play()
        coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        # move the coin
        coin_image_rect.x -= coin_velocity

    # check for collisions
    if player_image_rect.colliderect(coin_image_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_image_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

    # update HUD
    score_text = font.render("Score " + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(player_lives),
                         True, GREEN, DARK_GREEN)
    
    # check for game over
    if player_lives == 0:
        display_surface.blit(game_over_text,game_over_text_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()
        # pause while loop untill player presses a key to restart the game/loop
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # if player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_image_rect.y = WINDOW_HEIGHT//2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                # player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    # fill display
    display_surface.fill(BLACK)

    # blit the HUD
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 64), (WINDOW_WIDTH, 64), 2)

    # blit assets to screen
    display_surface.blit(player_image, player_image_rect)
    display_surface.blit(coin_image, coin_image_rect)

    # update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()
