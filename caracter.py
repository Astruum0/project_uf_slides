import pygame
from functions import Convert


class Caracter:

    def __init__(self):
        self.xstart = 0
        self.ystart = 0
        self.x = self.xstart
        self.y = self.ystart
        self.vel = 10
        self.taille = 40
        self.direction = "STAY"

    def move(self, direction):
        if direction == "LEFT":
            self.x -= self.vel
        if direction == "RIGHT":
            self.x += self.vel
        if direction == "UP":
            self.y -= self.vel
        if direction == "DOWN":
            self.y += self.vel

    def setStart(self, level):
        for col in range(15):
            for lig in range(15):
                x, y = Convert(lig, col)
                if level[lig][col] == 2:
                    self.xstart = x
                    self.ystart = y
                    self.x = self.xstart
                    self.y = self.ystart

    def setDir(self, direction, level):
        if level[self.y//40][self.x//40] != 12:
            if (direction == "LEFT" and self.x == 0) or (direction == "LEFT" and level[self.y//40][(self.x//40) - 1] != 1 and level[self.y//40][(self.x//40) - 1] != 12):
                self.direction = direction
            if (direction == "RIGHT" and self.x == 560) or (direction == "RIGHT" and level[self.y//40][(self.x//40) + 1] != 1 and level[self.y//40][(self.x//40) + 1] != 12):
                self.direction = direction
        if level[self.y//40][self.x//40] != 11:
            if (direction == "UP" and self.y == 0) or (direction == "UP" and level[(self.y//40) - 1][self.x//40] != 1 and level[(self.y//40) - 1][self.x//40] != 11):
                self.direction = direction
            if (direction == "DOWN" and self.y == 560) or (direction == "DOWN" and level[(self.y//40) + 1][self.x//40] != 1 and level[(self.y//40) + 1][self.x//40] != 11):
                self.direction = direction

    def immobile(self):
        if self.direction == "STAY":
            return True

    def reset(self):
        self.x = self.xstart
        self.y = self.ystart
        self.direction = "STAY"

    def OutOfBorder(self):
        if self.x < 0 or self.x >= 600 or self.y < 0 or self.y >= 600:
            return True
        else:
            return False

    def update(self, level):
        if self.direction == "LEFT":
            self.move("LEFT")
        if self.direction == "RIGHT":
            self.move("RIGHT")
        if self.direction == "UP":
            self.move("UP")
        if self.direction == "DOWN":
            self.move("DOWN")

        for col in range(15):
            for lig in range(15):
                x, y = Convert(lig, col)
                if col < 14 and self.direction == "RIGHT" and (level[lig][col + 1] == 1 or level[lig][col + 1] == 12) and x == self.x and y == self.y:
                    self.direction = "STAY"
                if col > 0 and self.direction == "LEFT" and (level[lig][col - 1] == 1 or level[lig][col - 1] == 12)and x == self.x and y == self.y:
                    self.direction = "STAY"
                if lig < 14 and self.direction == "DOWN" and (level[lig + 1][col] == 1 or level[lig + 1][col] == 11) and x == self.x and y == self.y:
                    self.direction = "STAY"
                if lig > 0 and self.direction == "UP" and (level[lig - 1][col] == 1 or level[lig - 1][col] == 11) and x == self.x and y == self.y:
                    self.direction = "STAY"
