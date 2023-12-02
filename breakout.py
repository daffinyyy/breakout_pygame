import pygame
import random
import numpy
from rectangle import *

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 900

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20

BALL_SIZE = 20

matrix = [[],[],[],[],[],[]]

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2023-11-30")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (SCREEN_WIDTH - score_text_rect.width, 
                          score_text_rect.height)

# player 1
player_1 =  Player("assets/player.png", "h", PLAYER_WIDTH, PLAYER_HEIGHT, 300, SCREEN_HEIGHT - 100, 5)
ball = Ball("assets/player.png", BALL_SIZE, 300, SCREEN_HEIGHT/2, 8, -30)

# bricks
x = 25
y = 70

for i in range(0, 6):
    if i == 5:
        x = 25
    for j in range(0, 6):
        if i <= 1:
            matrix[i].append(Brick("assets/player.png", "h", 90, 20, x, y, 0,  COLOR_BLUE))
            x += 114
            if j == 5 and i == 0:
                x = 25
                y += 30
            if j == 5 and i == 1:
                x = 25
                y += 30

        elif i > 1 and i <= 3:
            matrix[i].append(Brick("assets/player.png", "h", 90, 20, x, y, 0,  COLOR_GREEN))
            x += 114
            if j == 5 and i == 2:
                x = 25
                y += 30
            elif j == 5 and i == 3:
                x = 25
                y += 30

        elif i > 3:
            matrix[i].append(Brick("assets/player.png", "h", 90, 20, x, y, 0,  COLOR_ORANGE))
            x += 114
            if j == 5 and i == 4:
                x = 25
                y += 30

# victory
victory = False

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_1.move_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_1.move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_1.move_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
               player_1.move_right = False
    

    # checking the victory condition
    if not victory:

        # clear screen
        screen.fill(COLOR_BLACK)
        
        player_1.move(0,SCREEN_WIDTH - PLAYER_WIDTH)
        ball.move(0, SCREEN_WIDTH - BALL_SIZE, 10, 840 - BALL_SIZE)

        # drawing objects
        screen.blit(score_text, score_text_rect)
        screen.blit(ball.game_object, (ball.x, ball.y))
        screen.blit(player_1.game_object, (player_1.x, player_1.y)) #SCREEN_HEIGHT - 100))
        
        for x in range(0, 6):
            for y in range(0, 6):
                screen.blit(matrix[x][y].game_object, (matrix[x][y].x, matrix[x][y].y))


    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()