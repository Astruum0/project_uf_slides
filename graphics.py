import pygame
from functions import Convert


class engine:
    def __init__(self):
        self.blocks = [
            pygame.image.load("templates/brick.png"),
            pygame.image.load("templates/snow.png"),
            pygame.image.load("templates/finishflag.png"),
            pygame.image.load("templates/start.png"),
        ]
        self.brick = []
        for i in range(4):
            self.brick.append(
                pygame.image.load("templates/block/" + str(i + 1) + ".png")
            )
        self.bumpers = [
            pygame.image.load("templates/ArrowUp.png"),
            pygame.image.load("templates/ArrowDown.png"),
            pygame.image.load("templates/ArrowLeft.png"),
            pygame.image.load("templates/ArrowRight.png"),
            pygame.image.load("templates/buttonNeutral.png"),
        ]
        self.switchers = [
            pygame.image.load("templates/SwitcherLR.png"),
            pygame.image.load("templates/SwitcherUD.png"),
            pygame.image.load("templates/leverOff.png"),
            pygame.image.load("templates/leverOn.png"),
        ]
        self.lava = []
        for i in range(4):
            self.lava.append(pygame.image.load(
                "templates/Lava/" + str(i + 1) + ".png"))

        self.editorButtons = [
            pygame.image.load("menuframes/editor_play.png"),
            pygame.image.load("menuframes/editor_save.png"),
            pygame.image.load("menuframes/editor_exit.png"),
        ]

        self.kirby_idle = []
        for i in range(20):
            self.kirby_idle.append(pygame.image.load(
                "templates/kirby_idle/" + str(i + 1) + ".png"))

        self.kirby_right = []
        for i in range(8):
            self.kirby_right.append(pygame.image.load(
                "templates/kirby_right/" + str(i + 1) + ".png"))

        self.arrow_up = []
        for i in range(8):
            self.arrow_up.append(pygame.image.load(
                "templates/arrow_up/" + str(i + 1) + ".png"))

        self.arrow_down = []
        for i in range(8):
            self.arrow_down.append(pygame.image.load(
                "templates/arrow_down/" + str(i + 1) + ".png"))

        self.arrow_left = []
        for i in range(8):
            self.arrow_left.append(pygame.image.load(
                "templates/arrow_left/" + str(i + 1) + ".png"))

        self.arrow_right = []
        for i in range(8):
            self.arrow_right.append(pygame.image.load(
                "templates/arrow_right/" + str(i + 1) + ".png"))

    def show(self, win, level, caracter, frame, game, editor, test):
        for col in range(15):
            for lig in range(15):
                x, y = Convert(lig, col)
                if level[lig][col] == 0:
                    pygame.draw.rect(win, (0, 0, 0), (x, y, 40, 40))
                if level[lig][col] == 1:
                    win.blit(self.blocks[0], (x, y))
                if level[lig][col] == 2:
                    win.blit(self.blocks[3], (x, y))
                if level[lig][col] == 3:
                    win.blit(self.blocks[2], (x, y))
                if level[lig][col] == 4:
                    win.blit(self.blocks[1], (x, y))
                if level[lig][col] == 5:
                    win.blit(self.lava[(frame // 10) % 4], (x, y))
                if level[lig][col] == 6:
                    win.blit(self.arrow_up[(frame // 4) % 8], (x, y))
                if level[lig][col] == 7:
                    win.blit(self.arrow_down[(frame // 4) % 8], (x, y))
                if level[lig][col] == 8:
                    win.blit(self.arrow_left[(frame // 4) % 8], (x, y))
                if level[lig][col] == 9:
                    win.blit(self.arrow_right[(frame // 4) % 8], (x, y))
                if level[lig][col] == 10:
                    win.blit(self.bumpers[4], (x, y))
                if level[lig][col] == 11:
                    win.blit(self.switchers[0], (x, y))
                if level[lig][col] == 12:
                    win.blit(self.switchers[1], (x, y))
                if level[lig][col] == 13:
                    win.blit(self.switchers[2], (x, y))
                if level[lig][col] == 14:
                    win.blit(self.switchers[3], (x, y))

        if game or test:
            win.blit(self.kirby_idle[(frame // 5) % 20],
                     (caracter.x, caracter.y, caracter.taille, caracter.taille)),

        if editor and not test:
            for i in range(15):
                for j in range(15):
                    pygame.draw.rect(win, (255, 255, 255),
                                     (i * 40, j * 40, 40, 40), 1)
            win.blit(self.editorButtons[0], (0, 600))
            win.blit(self.editorButtons[1], (300, 600))
            win.blit(self.editorButtons[2], (600, 600))

    def toolbar(self, win, item):
        i = 610
        j = 0
        space = 43

        pygame.draw.rect(win, (0, 0, 0), (i, j, 40, 40))
        j += space
        win.blit(self.blocks[0], (i, j))
        j += space
        win.blit(self.blocks[3], (i, j))
        j += space
        win.blit(self.blocks[2], (i, j))
        j += space
        win.blit(self.blocks[1], (i, j))
        j += space
        win.blit(self.lava[0], (i, j))
        j += space
        win.blit(self.arrow_up[0], (i, j))
        j += space
        win.blit(self.arrow_down[0], (i, j))
        j += space
        win.blit(self.arrow_left[0], (i, j))
        j += space
        win.blit(self.arrow_right[0], (i, j))
        j += space
        win.blit(self.bumpers[4], (i, j))
        j += space
        win.blit(self.switchers[0], (i, j))
        j += space
        win.blit(self.switchers[1], (i, j))
        j += space
        win.blit(self.switchers[2], (i, j))

        pygame.draw.rect(win, (236, 112, 99), (i, item * 43, 40, 40), 2)
