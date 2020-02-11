import pygame
from bot import Bot
from functions import levelSetStart
from graphics import engine
import json
import copy
import time


def checkLevel(lvl):
    def newbots(
        bots, delete, x, y, Dir, Tun, prevbot, direction=["UP", "DOWN", "LEFT", "RIGHT"]
    ):
        for dire in direction:
            if not [x, y, dire, Dir, Tun] in delete:
                bots.append(Bot(x, y, dire, prevbot, Dir, Tun))
        return bots

    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    graphic = engine()
    pygame.display.set_caption("Level Verification...")
    level = lvl
    checking = True
    xstart, ystart = levelSetStart(level)
    listBots = newbots(
        [],
        [],
        xstart,
        ystart,
        0,
        False,
        None,
        Bot(xstart, ystart, "STAY", None, 0, False).possibleDirection(
            (ystart // 40), (xstart // 40), level
        ),
    )
    deletedBots = []
    start = time.time()
    pathSolving = False

    while checking:
        win.fill((0, 0, 0))
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                checking = False
                return "IMPOSSIBLE"
        if len(listBots) == 0:
            return False
        graphic.show(win, level, listBots[0], 0, False, False, False)
        i = 0
        data = None
        for bot in listBots:
            bot.show(win)

            data = bot.update(level)

            if type(data) == list:
                deletedBot = listBots.pop(i)
                listBots = newbots(
                    listBots,
                    deletedBots,
                    bot.x,
                    bot.y,
                    bot.statusDir,
                    bot.statusTunnel,
                    deletedBot,
                    data,
                )
                listDeletedBot = [
                    deletedBot.xstart,
                    deletedBot.ystart,
                    deletedBot.dirstart,
                    deletedBot.statusDirStart,
                    deletedBot.statusTunnelStart,
                ]

                if not listDeletedBot in deletedBots:
                    deletedBots.append(listDeletedBot)
            if data == "DEAD":
                deletedBot = listBots.pop(i)
                listDeletedBot = [
                    deletedBot.xstart,
                    deletedBot.ystart,
                    deletedBot.dirstart,
                    deletedBot.statusDirStart,
                    deletedBot.statusTunnelStart,
                ]
                if not listDeletedBot in deletedBots:
                    deletedBots.append(listDeletedBot)

            elif data == "END":
                checking = False
                path = bot.path()
                pathSolving = True
            i += 1
        if time.time() - start >= 60:
            return "HARD"
        pygame.display.update()

    indexDir = 0
    solver = Bot(xstart, ystart, path[indexDir], None, 0, False)
    solver.vel = 10
    Bot.spriteRight = pygame.image.load("templates/bot/solverbotright.png")
    Bot.spriteLeft = pygame.image.load("templates/bot/solverbotleft.png")
    while pathSolving:
        win.fill((0, 0, 0))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pathSolving = False

        graphic.show(win, level, solver, 0, False, False, False)
        solver.show(win)
        data = solver.update(level)
        if type(data) == list:
            indexDir += 1
            solver.direction = path[indexDir]
        if data == "END":
            pathSolving = False
            return "FINISH"

        pygame.display.update()


if __name__ == "__main__":
    with open("level_data/normal_level.json") as f:
        normal_levels = json.load(f)
    list_level = []
    for data in normal_levels:
        if data["level_name"] == "pattern":
            pattern = data["level_composition"]
        else:
            list_level.append(data["level_composition"])

    level = list_level[6]
    print(checkLevel(level))

