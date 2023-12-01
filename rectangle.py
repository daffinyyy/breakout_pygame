import pygame
import math
import numpy

class Rectangle():
    def __init__(self, asset, orientation, width, height, pos_x, pos_y, speed):
        self.game_object = pygame.image.load(asset)
        if orientation in ["horizontal","h","hor"]:  
            self.game_object = pygame.transform.rotate(self.game_object, 90)
        self.game_object = pygame.transform.scale(self.game_object, (width,height))
        self.x = pos_x
        self.y = pos_y
        self.exist = True
        self.speed = speed

class Player(Rectangle):
    def __init__(self, asset, orientation, width, height, pos_x, pos_y, speed):
        super().__init__(asset, orientation, width, height, pos_x, pos_y, speed)
        self.move_left = False
        self.move_right = False

    def move(self, limit_left, limit_right):
        # player left movement
        if self.move_left:
            self.x -= self.speed
        else:
            self.x += 0

        # player right movement
        if self.move_right:
            self.x += self.speed
        else:
            self.x += 0

        # player 1 collides with left wall
        if self.x <= limit_left:
            self.x = limit_left

        # player 1 collides with right wall
        elif self.x >= limit_right:
            self.x = limit_right

class Brick(Rectangle):
    def __init__(self, asset, orientation, width, height, pos_x, pos_y, speed, color):
        super().__init__(asset, orientation, width, height, pos_x, pos_y, speed)
        self.game_object.fill(color)

class Ball(Rectangle):
    def __init__(self, asset, size, pos_x, pos_y, speed, angle):
        super().__init__(asset, "v", size, size, pos_x, pos_y, speed)
        self.angle = angle

    def move(self, limit_left, limit_right, limit_up, limit_down):
        self.x = self.x + math.cos(math.radians(self.angle)) * (self.speed)
        self.y = self.y - math.sin(math.radians(self.angle)) * (self.speed)
        
        if self.x <= limit_left:
            self.x = limit_left
            self.turn(-90 * numpy.sign(self.angle))

        elif self.x >= limit_right:
            self.x = limit_right
            self.turn(90 * numpy.sign(self.angle))

        if self.y <= limit_up:
            self.y = limit_up
            self.turn(-90 * numpy.sign(self.angle))

        elif self.y >= limit_down:
            self.y = limit_down
            self.turn(90 * numpy.sign(self.angle))

    def turn(self, angle):
        self.angle += angle
        if self.angle > 180:
            self.angle -= 360
        if self.angle < -180:
            self.angle += 360
