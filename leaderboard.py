import pygame
from json_manipulation import recupTimes
from convert import convertTime


def leaderboard():
    pygame.font.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Leaderboard")
    fontSize = 18
    font = pygame.font.Font("fonts/PixelOperatorMono8-Bold.ttf", fontSize)
    title = pygame.image.load("MenuFrames/leaderboard_title.png")
    quitImg = pygame.image.load("MenuFrames/editor_exit.png")

    COLORS = [(201, 176, 55), (180, 180, 180), (150, 90, 56), (255, 255, 255)]
    Yscore = 120
    listNames, listTimes = recupTimes()

    leaderboard = True
    while leaderboard:
        win.fill((0, 0, 0))

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leaderboard = False
                return

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and event.pos[0] >= 531
                and event.pos[0] <= 576
                and event.pos[1] >= 531
                and event.pos[1] <= 576
            ):
                leaderboard = False
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5 and Yscore + 30 * len(listNames) > 510:
                    Yscore -= 15
                if event.button == 4 and Yscore < 120:
                    Yscore += 15

        i = 0
        for pseudo, time in zip(listNames, listTimes):
            text = str(i + 1) + ". " + pseudo + " | " + convertTime(time)
            if i < 3:
                top = font.render(text, True, COLORS[i])
            else:
                top = font.render(text, True, COLORS[3])
            win.blit(
                top,
                (
                    (300 - 1.5 * fontSize)
                    - (fontSize) * (len(str(i + 1) + ". " + pseudo)),
                    Yscore + 30 * i,
                ),
            )
            i += 1

        win.blit(title, (0, 0))
        pygame.draw.rect(win, (0, 0, 0), (0, 510, 600, 90))
        win.blit(quitImg, (529, 529))
        pygame.display.update()


if __name__ == "__main__":
    leaderboard()
