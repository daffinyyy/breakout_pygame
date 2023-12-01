import pygame
import random
import numpy
from rectangle import *

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 900

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 10

BALL_SIZE = 10

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2023-11-30")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (SCREEN_WIDTH - score_text_rect.width / 2, 
                          score_text_rect.height / 2 + 5)

# player 1
player_1 =  Player("assets/player.png", "h", PLAYER_WIDTH, PLAYER_HEIGHT, 300, SCREEN_HEIGHT - 100, 5)
ball = Ball("assets/player.png", BALL_SIZE, 300, SCREEN_HEIGHT/2, 8, -30)

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
        ball.move(0,SCREEN_WIDTH - BALL_SIZE, 0, SCREEN_HEIGHT - BALL_SIZE)

        # drawing objects
        screen.blit(score_text, score_text_rect)
        screen.blit(ball.game_object, (ball.x, ball.y))
        screen.blit(player_1.game_object, (player_1.x, player_1.y)) #SCREEN_HEIGHT - 100))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()