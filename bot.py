import pygame
from functions import Convert
import copy

class Bot:

    spriteRight = pygame.image.load("templates/bot/botright.png")
    spriteLeft = pygame.image.load("templates/bot/botleft.png")

    def __init__(self, x, y, direction, prevbot, Dir, Tun): 
        self.x = x
        self.y = y
        self.xstart = x
        self.ystart = y
        self.vel = 40
        self.taille = 40
        self.direction = direction
        self.dirstart = self.direction
        self.statusDir = Dir
        self.statusTunnel = Tun
        self.statusDirStart = Dir
        self.statusTunnelStart = Tun
        self.canMove = False
        self.prevBot = prevbot

    def move(self, direction):
        if direction == "LEFT":
            self.x -= self.vel
        if direction == "RIGHT":
            self.x += self.vel
        if direction == "UP":
            self.y -= self.vel
        if direction == "DOWN":
            self.y += self.vel
    
    def show(self, fen):
        
        if self.direction == "RIGHT" or self.direction == "DOWN":
            fen.blit(Bot.spriteRight, (self.x, self.y))
        else:
            fen.blit(Bot.spriteLeft, (self.x, self.y))

    
    def update(self, level):
        self.move(self.direction)
        if self.updateBlock(level) == "DEAD":
                    return "DEAD"
        
        for col in range(15):
            for lig in range(15):
                x, y = Convert(lig, col)
                if (self.x > 560 or self.x < 0 or self.y > 560 or self.y < 0) or (level[lig][col] == 5 and x == self.x and y == self.y):
                    return "DEAD"
                if level[lig][col] == 3 and x == self.x and y == self.y:
                    return "END"
                    
                if col < 14 and self.direction == "RIGHT" and (level[lig][col + 1] == 1 or self.defineTunnel(level, lig, col+1) == 12) and x == self.x and y == self.y: 
                    return self.possibleDirection(lig, col, level)
                if col > 0 and self.direction == "LEFT" and (level[lig][col - 1] == 1 or self.defineTunnel(level, lig, col-1) == 12) and x == self.x and y == self.y: 
                    return self.possibleDirection(lig, col, level)
                if lig < 14 and self.direction == "DOWN" and (level[lig + 1][col] == 1 or self.defineTunnel(level, lig+1, col) == 11) and x == self.x and y == self.y: 
                    return self.possibleDirection(lig, col, level)
                if lig > 0 and self.direction == "UP" and (level[lig - 1][col] == 1 or self.defineTunnel(level, lig-1, col) == 11) and x == self.x and y == self.y: 
                    return self.possibleDirection(lig, col, level)
                if (level[lig][col] == 4 or level[lig][col] == 2) and x == self.x and y == self.y:
                    return self.possibleDirection(lig, col, level)

        

    def updateBlock(self, level):
        for col in range(15):
            for lig in range(15):
                x, y = Convert(lig, col)
                if (
                    self.defineDir(level, lig, col) == 6 
                    and x == self.x 
                    and y == self.y
                ):
                    if (
                        lig > 0 
                        and (level[lig-1][col] == 1 
                        or self.defineTunnel(level, lig-1, col) == 11)
                    ):
                        return "DEAD"
                    else:
                        self.direction = "UP"
                if (
                    self.defineDir(level, lig, col) == 7
                    and x == self.x
                    and y == self.y
                ):
                    if (
                        lig < 14
                        and (level[lig+1][col] == 1 
                        or self.defineTunnel(level, lig+1, col) == 11)
                    ):
                        return "DEAD"
                    else:
                        self.direction = "DOWN"
                if (
                    self.defineDir(level, lig, col) == 8
                    and x == self.x
                    and y == self.y
                ):  
                    if (
                        col > 0 
                        and (level[lig][col-1] == 1 
                        or self.defineTunnel(level, lig, col-1) == 12)
                    ):
                        return "DEAD"
                    else:
                        self.direction = "LEFT"
                if (
                    self.defineDir(level, lig, col) == 9
                    and x == self.x
                    and y == self.y
                ):  
                    if (
                        col < 14
                        and (level[lig][col+1] == 1 
                        or self.defineTunnel(level, lig, col+1) == 12)
                    ):
                        return "DEAD"
                    else:
                        self.direction = "RIGHT"
                if level[lig][col] == 10 and x == self.x and y == self.y and self.direction != "STAY":
                    self.statusDir = (self.statusDir + 1 % 4)
                    
                if (level[lig][col] == 13 or level[lig][col] == 14) and x == self.x and y == self.y and self.direction != "STAY":
                    self.statusTunnel = not self.statusTunnel
                    if level[lig][col] == 13:
                        level[lig][col] = 14
                    elif level[lig][col] == 14:
                        level[lig][col] = 13
        return None
    
    def possibleDirection(self, lig, col, level):
        revres = []
        res = []
        if col < 14 and ((level[lig][col + 1] == 1 or self.defineTunnel(level, lig, col+1) == 12)):
            revres.append("RIGHT")
        if col > 1 and ((level[lig][col - 1] == 1 or self.defineTunnel(level, lig, col-1) == 12)):
            revres.append("LEFT")
        if lig < 14 and ((level[lig + 1][col] == 1 or self.defineTunnel(level, lig+1, col) == 11)): 
            revres.append("DOWN")
        if lig > 0 and ((level[lig - 1][col] == 1 or self.defineTunnel(level, lig-1, col) == 11)): 
            revres.append("UP")
        for Dir in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if not Dir in revres:
                res.append(Dir)
        return res
        
    def defineTunnel(self, level, lig, col):
        tunnel = level[lig][col]
        if level[lig][col] == 11 and self.statusTunnel:
            tunnel += 1
        elif level[lig][col] == 12 and self.statusTunnel:
            tunnel -= 1
        return tunnel
    
    def defineDir(self, level, lig, col):
        direBlock = level[lig][col]
        for _ in range(self.statusDir):      
            if direBlock == 6:
                direBlock = 9
            elif direBlock == 7:
                direBlock = 8
            elif direBlock == 8:
                direBlock = 6
            elif direBlock == 9:
                direBlock = 7
        return direBlock

    def path(self):
        res = [self.dirstart]
        iteratebot = self.prevBot
        while iteratebot:
            res.append(iteratebot.dirstart)
            iteratebot = iteratebot.prevBot
        res.reverse()
        return res


