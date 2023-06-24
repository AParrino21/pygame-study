import pygame, random

# intialize pygame
pygame.init()

# create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("SPACE INVADERS!")

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# define classes


class Game():
    """class to help control and udate gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        #set game values
        self.round_number = 1
        self.score = 0
        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group

        #set sounds
        self.new_round_sound = pygame.mixer.Sound('space_invaders/new_round.wav')
        self.new_round_sound.set_volume(.05)

        self.breach_sound = pygame.mixer.Sound('space_invaders/breach.wav')
        self.breach_sound.set_volume(.05)

        self.alien_hit_sound = pygame.mixer.Sound('space_invaders/alien_hit.wav')
        self.alien_hit_sound.set_volume(.05)

        self.player_hit_sound = pygame.mixer.Sound('space_invaders/player_hit.wav')
        self.player_hit_sound.set_volume(.05)

        #set font
        self.font = pygame.font.Font('space_invaders/Facon.ttf', 24)

    def update(self):
        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()

    def draw(self):
        #set color
        WHITE = (255,255,255)

        #set text
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = WINDOW_WIDTH//2
        score_rect.top = 10

        round_text = self.font.render("Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20,10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH - 20, 10)

        #blit the HUD
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text,round_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)



    def shift_aliens(self):
        """shift aliens down the screen"""
        #check if alien group hit an edge
        shift = False
        for alien in (self.alien_group.sprites()):
            if alien.rect.left <= 0 or alien.rect.right >= WINDOW_WIDTH:
                shift = True

        #shift every alien down and change direction and also check for a breach
        if shift:
            breach = False
            for alien in (self.alien_group.sprites()):
                #shift down
                alien.rect.y += 10* self.round_number

                #reverse direction and move the alien off the edge so shift does not trigger again
                alien.direction = -1 * alien.direction
                alien.rect.x += alien.direction * alien.velocity

                #check if an alien has breached the ship
                if alien.rect.bottom >= WINDOW_HEIGHT - 100:
                    breach = True
            
            #aliens breach
            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status("Aliens breached the line", "Press ENTER to continue!")

    def check_collisions(self):
        """check for collisions"""
        # see if any bullets in the player bullet group has hit an alien in the alien group
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 100

        #See if the player has collided with any bullet in the alien bullet group
        if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            self.player_hit_sound.play()
            self.player.lives -= 1

            self.check_game_status("You've been hit!", "Press 'Enter' to continue")

    def check_round_completion(self):
        if not self.alien_group:
            self.round_number += 1
            self.score += 1000*self.round_number

            self.start_new_round()

    def start_new_round(self):
        """start new round"""
        #create a grid of aliens 11 columns and 5 rows
        for i in range(11):
            for j in range(5):
                alien = Alien(64 + i*64, 64 + j*64, self.round_number, self.alien_bullet_group)
                self.alien_group.add(alien)

        #pause the game and prompt user to start
        self.new_round_sound.play()
        self.pause_game(f"SPACE INVADERS ROUND {self.round_number}", "Press Enter to START")

    def check_game_status(self, main_text, sub_text):
        #empty the bullet groups and reset the player and remaining aliens
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.player.reset()
        for alien in self.alien_group:
            alien.reset()
        
        #check if game is over or if it is a round reset
        if self.player.lives < 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)

    def pause_game(self, main_text, sub_text):
        global running
        """pause the game"""
        #set colors
        WHITE = (255,255,255)
        BLACK = (0,0,0)

        # render the text
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        #blit the text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        #pause game untill user hits enter
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def reset_game(self):
        self.pause_game(f"Final Score: {str(self.score)}", "Press ENTER to restart")

        #reset everything
        self.score = 0
        self.round_number = 1
        self.player.lives = 5

        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()

        self.start_new_round()


class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("space_invaders/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives =5
        self.velocity = 8

        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("space_invaders/player_fire.wav")
        self.shoot_sound.set_volume(.05)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def fire(self):
        """Fire a bullet"""
        #Restrict the number of bullets on screen at a time
        if len(self.bullet_group) < 2:
            self.shoot_sound.play()
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)

    def reset(self):
        self.rect.centerx = WINDOW_WIDTH//2


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("space_invaders/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound('space_invaders/alien_fire.wav')
        self.shoot_sound.set_volume(.05)

    def update(self):
        #move the aliens left or right based up positive or negative direction
        self.rect.x += self.direction*self.velocity

        #randomly fire a bullet
        if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        AlienBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

    def reset(self):
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1


class PlayerBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        self.image = pygame.image.load("space_invaders/green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        self.rect.y -= self.velocity

        #If the bullet is off the screen, kill it
        if self.rect.bottom < 0:
            self.kill()


class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load('space_invaders/red_laser.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        self.rect.y += self.velocity

        #if the bullet is off the screen, kill it
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
        


#create bullet groups 
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

#create player group and object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)
my_player_group.add(my_player)

#create alien group
my_alien_group = pygame.sprite.Group()

#create game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
my_game.start_new_round()

# main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #The player wants to fire
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()
            if event.key == pygame.K_ESCAPE:
                my_game.pause_game("Game is Paused", "Press ENTER to RESUME")

    display_surface.fill((0,0,0))

    #update and display sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_player_bullet_group.update()
    my_player_bullet_group.draw(display_surface)

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    my_game.update()
    my_game.draw()

    # update the display
    pygame.display.update()
    clock.tick(FPS)

# end the game
pygame.quit()
