import pygame
from pygame.locals import *
from json_manipulation import *
from convert import convertTime
import json


def endScreen(time):

    pygame.font.init()
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Save your time")
    clock = pygame.time.Clock()
    font = pygame.font.Font("fonts/PixelOperatorMono8-Bold.ttf", 30)
    fontMini = pygame.font.Font("fonts/PixelOperatorMono8-Bold.ttf", 14)
    bg = pygame.image.load("menuframes/inputscore.png")
    index = 0

    colors = [
        (118, 215, 196),
        (72, 201, 176),
        (26, 188, 156),
        (23, 165, 137),
        (20, 143, 119),
    ]

    timeStr = convertTime(time)

    listNames, listTimes = recupTimes()

    name = []

    saving = True
    while saving:
        win.blit(bg, (0, 0))
        clock.tick(60)
        pseudo = ""
        for letter in name:
            pseudo += letter
        for event in pygame.event.get():
            if event.type == QUIT:
                saving = False
                return

            if event.type == MOUSEBUTTONDOWN:
                if (
                    event.pos[0] >= 519
                    and event.pos[0] <= 519 + 40
                    and event.pos[1] >= 472
                    and event.pos[1] <= 472 + 40
                    and len(pseudo) > 1
                ):
                    saveTime(time, pseudo, listNames)
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
                    saveTime(time, pseudo, listNames)
                    saving = False
                    return
                elif len(name) <= 14 and event.unicode != "\x7f":
                    name.insert(index, event.unicode)
                    index += 1

        if pseudo in listNames:
            warning1 = fontMini.render(
                "This Pseudo is already used !", True, (255, 0, 0),
            )
            warning2 = fontMini.render("Save a new score ?", True, (255, 0, 0),)
            win.blit(warning1, (53, 523))
            win.blit(warning2, (53, 543))

        i = 0
        for pseu, time_ in zip(listNames[:5], listTimes[:5]):
            text = pseu + " - " + convertTime(time_)
            top = fontMini.render(text, True, colors[i])
            win.blit(top, (300 - 7 * (len(text)), 250 + 30 * i))
            i += 1

        pygame.draw.ellipse(win, (80, 80, 80), (53 + (index * 30), 478, 5, 30))

        timeText = font.render(timeStr, True, (243, 156, 18))
        win.blit(timeText, (300 - 15 * (len(timeStr)), 148))

        textname = font.render(pseudo, True, (20, 20, 20))
        win.blit(textname, (53, 478))

        pygame.display.update()


if __name__ == "__main__":
    endScreen(2852.867)
