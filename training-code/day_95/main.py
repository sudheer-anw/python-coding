import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('training-code/day_95/.background.png')

# Title
pygame.display.set_caption("Space Invaders")

# Player
player_img = pygame.image.load('training-code/day_95/lighter.gif')
player_x = 370
player_y = 480
player_x_change = 0

# Alien
alien_img = []
alien_x = []
alien_y = []
alien_x_change = []
alien_y_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    alien_img.append(pygame.image.load('training-code/day_95/alienpblog.png'))
    alien_x.append(random.randint(0, 735))
    alien_y.append(random.randint(50, 150))
    alien_x_change.append(4)
    alien_y_change.append(40)

# Bullet
bullet_img = pygame.image.load('training-code/day_95/laserBullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"  # ready - you can't see the bullet, fire - the bullet is currently moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def alien(x, y, i):
    screen.blit(alien_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(alien_x, alien_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(alien_x - bullet_x, 2) + math.pow(alien_y - bullet_y, 2))
    return distance < 27

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Alien movement
    for i in range(num_of_aliens):
        # Game Over
        if alien_y[i] > 440:
            for j in range(num_of_aliens):
                alien_y[j] = 2000
            game_over_text()
            break

        alien_x[i] += alien_x_change[i]
        if alien_x[i] <= 0:
            alien_x_change[i] = 4
            alien_y[i] += alien_y_change[i]
        elif alien_x[i] >= 736:
            alien_x_change[i] = -4
            alien_y[i] += alien_y_change[i]

        # Collision
        collision = is_collision(alien_x[i], alien_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            alien_x[i] = random.randint(0, 735)
            alien_y[i] = random.randint(50, 150)

        alien(alien_x[i], alien_y[i], i)

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()

