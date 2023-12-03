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

FIRST_BRICK_X = 25
BRICK_WIDTH = 90
BRICK_HEIGHT = 20
BRICK_OFFSET = 24

bricks = []

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
player_1 = Player("assets/player.png", "h", PLAYER_WIDTH, PLAYER_HEIGHT, 300, SCREEN_HEIGHT - 100, 8)
ball = Ball("assets/player.png", BALL_SIZE, 300, SCREEN_HEIGHT / 2, 8, -30)

# brick
color = COLOR_BLUE
row_y = 70

for i in range(0, 6):
    bricks.append([])
    brick_x = FIRST_BRICK_X
    for j in range(0, 6):
        if i == 2:  # Change color of bricks
            color = COLOR_GREEN
        elif i == 4:
            color = COLOR_ORANGE
        bricks[i].append(Brick("assets/player.png", "h", BRICK_WIDTH, BRICK_HEIGHT, brick_x, row_y, color))
        brick_x += BRICK_WIDTH + BRICK_OFFSET
    row_y += 30

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

        player_1.move(0, SCREEN_WIDTH - PLAYER_WIDTH)
        ball.move(0, SCREEN_WIDTH - BALL_SIZE, 0, SCREEN_HEIGHT - BALL_SIZE)

        # drawing objects
        screen.blit(score_text, score_text_rect)
        screen.blit(ball.game_object, (ball.x, ball.y))
        screen.blit(player_1.game_object, (player_1.x, player_1.y))  # SCREEN_HEIGHT - 100))

        for x in range(0, 6):
            for y in range(0, 6):
                if (not bricks[x][y].destroyed):
                    screen.blit(bricks[x][y].game_object, (bricks[x][y].x, bricks[x][y].y))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()