import pygame
from pygame.locals import *
from json_manipulation import importToJson, recupLevelNames, overwiteLevel
import json


def saveLevel(lvl):

    pygame.font.init()
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Save your Level")
    clock = pygame.time.Clock()
    font = pygame.font.Font("fonts/PixelOperatorMono8-Bold.ttf", 30)
    fontWarning = pygame.font.Font("fonts/PixelOperatorMono8-Bold.ttf", 12)
    bg = pygame.image.load("menuframes/inputbackground.png")
    index = 0

    levelsName = recupLevelNames()

    name = []

    saving = True
    while saving:
        win.blit(bg, (0, 0))
        clock.tick(60)
        text = ""
        for letter in name:
            text += letter
        for event in pygame.event.get():
            if event.type == QUIT:
                saving = False
                return

            if event.type == MOUSEBUTTONDOWN:
                if (
                    event.pos[0] >= 521
                    and event.pos[0] <= 560
                    and event.pos[1] >= 315
                    and event.pos[1] <= 355
                    and len(text) > 1
                ):
                    if text in levelsName:
                        overwiteLevel(lvl, text)
                    else:
                        importToJson(lvl, text)
                    saving = False
                    return
                if (
                    event.pos[0] >= 531
                    and event.pos[0] <= 576
                    and event.pos[1] >= 531
                    and event.pos[1] <= 576
                ):
                    saving = False
                    return

            if event.type == KEYDOWN and event.unicode != "" and event.unicode != '"':
                if event.key == K_LEFT:
                    if index > 0:
                        index -= 1
                elif event.key == K_RIGHT:
                    if index < len(name):
                        index += 1
                elif event.key == K_BACKSPACE and len(name) > 0:
                    name.pop(index - 1)
                    index -= 1
                elif event.key == K_RETURN:
                    if text in levelsName:
                        overwiteLevel(lvl, text)
                    else:
                        importToJson(lvl, text)
                    saving = False
                    return
                elif len(name) <= 14 and event.unicode != "\x7f":
                    name.insert(index, event.unicode)
                    index += 1

        if text in levelsName:
            warning1 = fontWarning.render(
                "This level name already exists !", True, (255, 0, 0),
            )
            warning2 = fontWarning.render(
                "Saving this level will overwrite on it", True, (255, 0, 0),
            )
            win.blit(warning1, (55, 385))
            win.blit(warning2, (55, 400))

        pygame.draw.ellipse(win, (80, 80, 80), (55 + (index * 30), 321, 5, 30))

        textname = font.render(text, True, (20, 20, 20))
        win.blit(textname, (55, 321))

        pygame.display.update()


if __name__ == "__main__":
    saveLevel([1])
