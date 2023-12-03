import pygame
import math
import numpy
from engine import *


class Rectangle():
    def __init__(self, asset, orientation, width, height, pos_x, pos_y, speed, collision=False):
        self.game_object = pygame.image.load(asset)
        if orientation in ["horizontal", "h", "hor"]:
            self.game_object = pygame.transform.rotate(self.game_object, 90)
        self.game_object = pygame.transform.scale(self.game_object, (width, height))
        self.x = pos_x
        self.y = pos_y
        self.destroyed = False
        self.speed = speed
        if (collision):  # create the collider and add it to the active colliders
            self.collider = Box_Collider(pos_x, pos_y, width, height, self)
            Collider.active_colliders.append(self.collider)


class Player(Rectangle):
    def __init__(self, asset, orientation, width, height, pos_x, pos_y, speed):
        super().__init__(asset, orientation, width, height, pos_x, pos_y, speed, True)
        self.move_left = False
        self.move_right = False

    def move(self, limit_left, limit_right):
        can_move = True
        collision = Collider.colision(self.collider)  # Player can't move if is touching ball
        if (collision != None):
            if (isinstance(collision.object, Ball)):
                can_move = False

        if (can_move):
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

            # the collider moves along
            self.collider.x = self.x
            self.collider.y = self.y


class Brick(Rectangle):
    def __init__(self, asset, orientation, width, height, pos_x, pos_y, color):
        super().__init__(asset, orientation, width, height, pos_x, pos_y, 0, True)
        self.game_object.fill(color)


class Ball(Rectangle):
    def __init__(self, asset, size, pos_x, pos_y, speed, angle):
        super().__init__(asset, "v", size, size, pos_x, pos_y, speed, True)
        self.angle = angle

    def move(self, limit_left, limit_right, limit_up, limit_down):
        # move diagonally by the power of algebric calculations
        self.x = self.x + math.cos(math.radians(self.angle)) * self.speed
        self.y = self.y - math.sin(math.radians(self.angle)) * self.speed

        # wall collision
        if self.x <= limit_left:
            self.x = limit_left
            self.turn(-2 * self.angle + 180 * numpy.sign(self.angle))

        elif self.x >= limit_right:
            self.x = limit_right
            self.turn(-2 * self.angle + 180 * numpy.sign(self.angle))

        if self.y <= limit_up:
            self.y = limit_up
            self.turn(-2 * self.angle)

        elif self.y >= limit_down:
            self.y = limit_down
            self.turn(-2 * self.angle)

        # the collider moves along
        self.collider.x = self.x
        self.collider.y = self.y

        # ask the main collider if something is colliding
        collision = Collider.colision(self.collider)
        if (collision != None):

            if (isinstance(collision.object, Brick)):  # the collider is attached to a brick
                print(collision.y, self.collider.y, self.collider.height)
                if ((abs(collision.y - self.collider.y - self.collider.height) <= self.speed)  # downward contact
                        or abs(collision.y + collision.height - self.collider.y) <= self.speed):  # upward contact
                    self.turn(-2 * self.angle)
                else:  # side contact
                    self.turn(-2 * self.angle + 180 * numpy.sign(self.angle))

            if (isinstance(collision.object, Player)):  # the collider is attached to a player
                # the direction of the ball differs based on player moviment
                if ((collision.object.move_right and self.angle > -90) or
                        (collision.object.move_left and self.angle < -90)):
                    self.turn(-2 * self.angle)
                else:
                    self.turn(180)

    def turn(self, angle):
        self.angle += angle
        if self.angle > 180:
            self.angle -= 360
        if self.angle < -180:
            self.angle += 360
