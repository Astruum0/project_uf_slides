import pygame
from functions import resetLevel
from pygame.locals import *
from caracter import Caracter


def pausemenu(win):
    pause = True
    pausemenudarken = pygame.image.load("MenuFrames/pausedarken.png")
    SizeX = 373
    SizeY = 49
    PlusX = 113.5
    ResumePlusY = 250
    RestartPlusY = 305
    SizeXQuit = 127
    PlusXQuit = 236.5
    QuitButtonPlusY = 525
    while pause == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pause = False
                return True
            ###RESUME BUTTON START###
            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > ResumePlusY
                and event.pos[1] < ResumePlusY + SizeY
            ):
                ResumeImg = pygame.image.load("menuframes/resume_hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > ResumePlusY
                and event.pos[1] < ResumePlusY + SizeY
            ):
                pause = False
                return False
            else:
                ResumeImg = pygame.image.load("menuframes/resume_neutral.png")

            ###RESUME BUTTON END###
            ###RESTART BUTTON START###
            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > RestartPlusY
                and event.pos[1] < RestartPlusY + SizeY
            ):
                RestartImg = pygame.image.load("menuframes/restart_hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > RestartPlusY
                and event.pos[1] < RestartPlusY + SizeY
            ):
                pause = False
                return False
            else:
                RestartImg = pygame.image.load(
                    "menuframes/restart_neutral.png")

            ###RESTART BUTTON END###
            ###QUIT BUTTON START###
            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusXQuit
                and event.pos[0] < PlusXQuit + SizeXQuit
                and event.pos[1] > QuitButtonPlusY
                and event.pos[1] < QuitButtonPlusY + SizeY
            ):
                QuitImg = pygame.image.load("menuframes/QuitButton_Hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusXQuit
                and event.pos[0] < PlusXQuit + SizeXQuit
                and event.pos[1] > QuitButtonPlusY
                and event.pos[1] < QuitButtonPlusY + SizeY
            ):
                pause = False
                return True
            else:
                QuitImg = pygame.image.load(
                    "menuframes/QuitButton_Neutral.png")
            ###QUIT BUTTON END###

            keys = pygame.key.get_pressed()
            if keys[K_RETURN]:
                pause = False
                return False

            win.blit(pausemenudarken, (0, 0))
            win.blit(ResumeImg, (PlusX, ResumePlusY))
            win.blit(RestartImg, (PlusX, RestartPlusY))
            win.blit(QuitImg, (PlusXQuit, QuitButtonPlusY))
        pygame.display.update()
