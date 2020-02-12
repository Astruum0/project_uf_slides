import pygame
from pygame.locals import *
from caracter import Caracter
from functions import Convert, resetLevel
from graphics import engine
from check import checkLevel
from saveLevel import saveLevel
from pause import pausemenu
from timer import Timer
from endScreen import endScreen
import copy
import json
import time


class Game:
    def __init__(self):
        pygame.init()
        self.caracter = Caracter()
        self.engine = engine()

        self.win = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.i = 0
        pygame.display.set_caption("SLIDE")
        self.game = False
        self.editor = False
        self.pause = False
        joysticks = []

        with open("level_data/normal_level.json") as f:
            self.normal_levels = json.load(f)
        self.list_level = []
        for data in self.normal_levels:
            if data["level_name"] == "pattern":
                self.pattern = data["level_composition"]
            elif data["level_name"] != "Secret Level":
                self.list_level.append(data["level_composition"])

        self.level = self.list_level[self.i]
        self.caracter.setStart(self.level)
        self.selectedItem = 0
        self.indexFrame = 0

        self.switchDir = 0
        self.switchTunnel = False

        joysticks = []
        for i in range(0, pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
        if len(joysticks) > 0:
            joysticks[-1].init()
            print("-------------------")
            print("Manettes detectees :", joysticks[-1].get_name())

    def runGame(self):
        self.game = True
        self.editor = False
        self.test = False
        self.timer = Timer(0, 625)
        self.win = pygame.display.set_mode((600, 650))
        self.level = self.list_level[self.i]
        self.caracter.setStart(self.level)
        while self.game:
            self.win.fill((0, 0, 0))
            self.clock.tick(60)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.timer.refresh()
                    self.game = False
                    return

            if keys[K_ESCAPE]:
                self.timer.pause()
                output = pausemenu(self.win)
                if output == "QUIT":
                    self.game = False
                    return
                if output == "RESUME":
                    self.timer.resume()
                if output == "RESTART":
                    self.timer.resume()
                    self.level = resetLevel(
                        self.level, self.switchDir, self.switchTunnel
                    )
                    self.switchDir = 0
                    self.switchTunnel = False
                    self.indexFrame = 0
                    self.caracter.reset()
                    self.level = self.list_level[self.i]

            if keys[K_LEFT] and self.caracter.immobile():
                self.caracter.setDir("LEFT", self.level)
            elif keys[K_RIGHT] and self.caracter.immobile():
                self.caracter.setDir("RIGHT", self.level)
            elif keys[K_DOWN] and self.caracter.immobile():
                self.caracter.setDir("DOWN", self.level)
            elif keys[K_UP] and self.caracter.immobile():
                self.caracter.setDir("UP", self.level)
            ###MANETTE###
            elif event.type == pygame.JOYHATMOTION and self.caracter.immobile():
                if event.value == (-1, 0):
                    self.caracter.setDir("LEFT", self.level)
                if event.value == (1, 0):
                    self.caracter.setDir("RIGHT", self.level)
                if event.value == (0, 1):
                    self.caracter.setDir("UP", self.level)
                if event.value == (0, -1):
                    self.caracter.setDir("DOWN", self.level)
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    self.caracter.setStart(self.level)
                    ###############
            elif keys[K_SPACE] or self.caracter.OutOfBorder():
                self.level = resetLevel(self.level, self.switchDir, self.switchTunnel)
                self.switchDir = 0
                self.switchTunnel = False
                self.indexFrame = 0
                self.caracter.reset()
                self.level = self.list_level[self.i]

            self.indexFrame += 1
            self.caracter.update(self.level)
            self.updateBlock()
            self.engine.show(
                self.win,
                self.level,
                self.caracter,
                self.indexFrame,
                self.game,
                self.editor,
                self.test,
            )

            self.timer.update()
            self.timer.show(self.win)

            pygame.display.update()

    def runEditor(self):
        self.editor = True
        self.game = False
        self.test = False
        while self.editor:
            self.win = pygame.display.set_mode((650, 650))
            self.win.fill((0, 0, 0))
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.editor = False
                    return
                if (
                    event.type == MOUSEBUTTONDOWN
                    and event.button == 1
                    and event.pos[0] >= 610
                ):
                    if event.pos[1] > 600:
                        self.editor = False
                        self.test = False
                        return
                    else:
                        self.selectedItem = event.pos[1] // 43

                if (
                    event.type == MOUSEBUTTONDOWN
                    and event.pos[0] < 600
                    and event.pos[1] < 600
                ):
                    if event.button == 1:
                        self.level[event.pos[1] // 40][
                            event.pos[0] // 40
                        ] = self.selectedItem
                    if event.button == 2:
                        self.selectedItem = self.level[event.pos[1] // 40][
                            event.pos[0] // 40
                        ]
                    if event.button == 3:
                        self.level[event.pos[1] // 40][event.pos[0] // 40] = 0
                    if event.button == 5 and self.selectedItem < 13:
                        self.selectedItem += 1
                    if event.button == 4 and self.selectedItem > 0:
                        self.selectedItem -= 1

                if event.type == MOUSEBUTTONDOWN and event.pos[1] > 600:
                    if event.pos[0] > 0 and event.pos[0] < 300:
                        self.testLevel()
                        self.win = pygame.display.set_mode((650, 650))
                    if event.pos[0] > 300 and event.pos[0] < 600:
                        print(self.level)
                        if checkLevel(self.level) == "FINISH":
                            saveLevel(self.level)

            self.engine.toolbar(self.win, self.selectedItem)
            self.engine.show(
                self.win,
                self.level,
                self.caracter,
                self.indexFrame,
                self.game,
                self.editor,
                self.test,
            )
            pygame.display.update()

    def testLevel(self):
        self.win = pygame.display.set_mode((600, 600))
        self.test = True
        self.game = False
        self.caracter.setStart(self.level)
        while self.test:
            self.win.fill((0, 0, 0))
            self.clock.tick(60)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.test = False
                    return

            if keys[K_LEFT] and self.caracter.immobile():
                self.caracter.setDir("LEFT", self.level)
            elif keys[K_RIGHT] and self.caracter.immobile():
                self.caracter.setDir("RIGHT", self.level)
            elif keys[K_DOWN] and self.caracter.immobile():
                self.caracter.setDir("DOWN", self.level)
            elif keys[K_UP] and self.caracter.immobile():
                self.caracter.setDir("UP", self.level)
            ###MANETTE###
            elif event.type == pygame.JOYHATMOTION and self.caracter.immobile():
                if event.value == (-1, 0):
                    self.caracter.setDir("LEFT", self.level)
                if event.value == (1, 0):
                    self.caracter.setDir("RIGHT", self.level)
                if event.value == (0, 1):
                    self.caracter.setDir("UP", self.level)
                if event.value == (0, -1):
                    self.caracter.setDir("DOWN", self.level)
            elif event.type == pygame.JOYBUTTONDOWN and self.caracter.immobile():
                if event.button == 1:
                    self.caracter.setStart(self.level)
                if event.button == 7 and self.pause == False:
                    self.pause = True
                    self.pausemenu()
            ###############
            elif keys[K_ESCAPE]:
                self.level = resetLevel(self.level, self.switchDir, self.switchTunnel)
                self.switchDir = 0
                self.switchTunnel = False
                self.caracter.reset()
                self.test = False
                if self.editor:
                    self.runEditor()
                else:
                    return

            elif keys[K_SPACE] or self.caracter.OutOfBorder():
                self.level = resetLevel(self.level, self.switchDir, self.switchTunnel)
                self.switchDir = 0
                self.switchTunnel = False
                self.caracter.reset()

            self.indexFrame += 1
            self.caracter.update(self.level)
            self.updateBlock()
            self.engine.show(
                self.win,
                self.level,
                self.caracter,
                self.indexFrame,
                self.game,
                self.editor,
                self.test,
            )

            pygame.display.update()

    def updateBlock(self):
        for col in range(15):
            for lig in range(15):
                x, y = Convert(lig, col)
                # Next Level
                if (
                    self.level[lig][col] == 3
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    self.level = resetLevel(
                        self.level, self.switchDir, self.switchTunnel
                    )
                    self.switchDir = 0
                    self.switchTunnel = False
                    self.caracter.reset()
                    self.test = False
                    self.indexFrame = 0
                    if self.editor:
                        self.runEditor()
                    elif not self.game:
                        return
                    if self.game:
                        self.i += 1
                        try:
                            self.level = self.list_level[self.i]
                        except:
                            self.i = 0
                            endScreen(self.timer.getTime())
                            self.game = False
                            return
                        self.caracter.setStart(self.level)

                if (
                    (self.level[lig][col] == 2 or self.level[lig][col] == 4)
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    self.caracter.direction = "STAY"
                if (
                    self.level[lig][col] == 5
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    self.level = resetLevel(
                        self.level, self.switchDir, self.switchTunnel
                    )
                    self.switchDir = 0
                    self.switchTunnel = False
                    self.indexFrame = 0
                    self.caracter.reset()
                    if self.editor:
                        self.runEditor()
                    else:
                        return
                if (
                    self.level[lig][col] == 6
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    if lig > 0 and (
                        self.level[lig - 1][col] == 1 or self.level[lig - 1][col] == 11
                    ):
                        self.level = resetLevel(
                            self.level, self.switchDir, self.switchTunnel
                        )
                        self.switchDir = 0
                        self.switchTunnel = False
                        self.indexFrame = 0
                        self.caracter.reset()
                        if self.editor:
                            self.runEditor()
                        else:
                            return
                    else:
                        self.caracter.direction = "UP"
                if (
                    self.level[lig][col] == 7
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    if lig < 14 and (
                        self.level[lig + 1][col] == 1 or self.level[lig + 1][col] == 11
                    ):
                        self.level = resetLevel(
                            self.level, self.switchDir, self.switchTunnel
                        )
                        self.switchDir = 0
                        self.switchTunnel = False
                        self.indexFrame = 0
                        self.caracter.reset()
                        if self.editor:
                            self.runEditor()
                        else:
                            return
                    else:
                        self.caracter.direction = "DOWN"
                if (
                    self.level[lig][col] == 8
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    if col > 0 and (
                        self.level[lig][col - 1] == 1 or self.level[lig][col - 1] == 12
                    ):
                        self.level = resetLevel(
                            self.level, self.switchDir, self.switchTunnel
                        )
                        self.switchDir = 0
                        self.switchTunnel = False
                        self.indexFrame = 0
                        self.caracter.reset()
                        if self.editor:
                            self.runEditor()
                        else:
                            return
                    else:
                        self.caracter.direction = "LEFT"
                if (
                    self.level[lig][col] == 9
                    and x == self.caracter.x
                    and y == self.caracter.y
                ):
                    if col < 14 and (
                        self.level[lig][col + 1] == 1 or self.level[lig][col + 1] == 12
                    ):
                        self.level = resetLevel(
                            self.level, self.switchDir, self.switchTunnel
                        )
                        self.switchDir = 0
                        self.switchTunnel = False
                        self.indexFrame = 0
                        self.caracter.reset()
                        if self.editor:
                            self.runEditor()
                        else:
                            return
                    else:
                        self.caracter.direction = "RIGHT"
                if (
                    self.level[lig][col] == 10
                    and x == self.caracter.x
                    and y == self.caracter.y
                    and self.caracter.direction != "STAY"
                ):
                    self.switchDir += 1
                    for col in range(15):
                        for lig in range(15):
                            if self.level[lig][col] == 6:
                                self.level[lig][col] = 9
                            elif self.level[lig][col] == 7:
                                self.level[lig][col] = 8
                            elif self.level[lig][col] == 8:
                                self.level[lig][col] = 6
                            elif self.level[lig][col] == 9:
                                self.level[lig][col] = 7
                if (
                    (self.level[lig][col] == 13 or self.level[lig][col] == 14)
                    and x == self.caracter.x
                    and y == self.caracter.y
                    and self.caracter.direction != "STAY"
                ):
                    self.switchTunnel = not self.switchTunnel
                    for col in range(15):
                        for lig in range(15):
                            if self.level[lig][col] == 11:
                                self.level[lig][col] = 12
                            elif self.level[lig][col] == 12:
                                self.level[lig][col] = 11
                            if self.level[lig][col] == 13:
                                self.level[lig][col] = 14
                            elif self.level[lig][col] == 14:
                                self.level[lig][col] = 13

    def clearLevel(self):
        self.level = copy.deepcopy(self.pattern)


if __name__ == "__main__":
    game = Game()
    game.runGame()
    pygame.quit()
