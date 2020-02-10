import pygame
from pygame.locals import *


def pausemenu(win):
    pause = True
    pausemenudarken = pygame.image.load("MenuFrames/pausedarken.png")
    print("Fonction lancée")
    while pause == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pause = False
                return True
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            pause = False
            return False

        win.blit(pausemenudarken, (0, 0))
        pygame.display.update()
