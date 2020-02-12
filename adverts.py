import pygame


def non_valid():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("SLIDES")
    clock = pygame.time.Clock()
    bg = pygame.image.load("menuframes/advert_nonvalidstage.png")

    confirmLoop = True
    while confirmLoop:
        win.blit(bg, (0, 0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                confirmLoop = False
                return

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[1] > 333
                and event.pos[1] < 383
                and event.pos[0] > 200
                and event.pos[0] < 400
            ):
                confirmLoop
                return

        pygame.display.update()


if __name__ == "__main__":
    non_valid()

