import pygame
import random
import math
from pygame import mixer
import time


def Background():
    screen.blit(background, (0, 0))


def player(X, Y):
    screen.blit(playerimg, (X, Y))


def enemy(X, Y):
    screen.blit(enemyimg[i], (X, Y))


def fire_bullet(X, Y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (X, Y-10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) +
                         math.pow(enemyY-bulletY, 2))
    if distance < 40:
        return True

    else:
        return False


def show_score(X, Y):
    score = font.render('SCORE : ' + str(Score_value), True, (255, 255, 0))
    screen.blit(score, (X, Y))


def game_over():
    over = gameOver_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (300, 250))


# Initialize the pygame
pygame.init()

#  Create the screen
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('f6cfdf4f237b4e7c8a32da46a6511548.jpg')

# Background sound
mixer.music.load("background.wav")
mixer.music.play()


# Title and logo
icon = pygame.image.load('galaxy.png')
pygame.display.set_caption("Space invaders by harsh kumar")
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemys = 5

for i in range(num_of_enemys):
    enemyimg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# Bullet
# ready --> you can't see the bullet
# fire --> the bullet is moving
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'

# score
Score_value = 0
font = pygame.font.Font('Caltons Clean Demo Version.otf', 24)

textX = 10
textY = 10

# Game over

gameOver_font = pygame.font.Font('Caltons Clean Demo Version.otf', 64)


# Game Loop
running = True
while running:
    # RGB - BG colour
    # screen.fill((155, 0, 255))

    # background
    Background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -1.5
                # print("Left key")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 1.5
                # print("Right key")

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # Making boundry for player so it doesnot go out of screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

    # Making enemy move
    for i in range(num_of_enemys):

        # Game Over
        if enemyY[i] > 420:
            for j in range(num_of_enemys):
                enemyY[j] = 20000

            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        Collision = isCollision(
            enemyX[i]+32, enemyY[i]+32, bulletX+32, bulletY+32)
        if Collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            Score_value += 1

            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i])

    # bullet movement

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        # bulletX = playerX
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    # Show score
    show_score(textX, textY)

    pygame.display.update()
