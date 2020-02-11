import pygame
import time


class Timer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.origine = time.time()
        self.start = True
        self.timer = 0
        self.save = 0

        self.font = pygame.font.Font("fonts/PixelOperatorMono8-Bold.ttf", 25)
        self.s = "0"
        self.ms = "000"
        self.m = "0"
        self.h = "0"

    def show(self, win):

        self.duree = str(round(self.timer + self.save, 3))
        if "." in self.duree:
            self.s, self.ms = self.duree.split(".")
            self.m = str(int(self.s) // 60)
            self.h = str(int(self.m) // 60)
            self.m = str(int(self.m) % 60)
            self.s = str(int(self.s) % 60)
            if self.ms == "0":
                self.ms = "000"
        else:
            self.s = self.duree
            self.ms = "000"
            self.m = str(int(self.s) // 60)
            self.h = str(int(self.m) // 60)
            self.m = str(int(self.m) % 60)
            self.s = str(int(self.s) % 60)

        self.text = self.font.render(
            self.h.zfill(2) + ":" + self.m.zfill(2) + ":" + self.s.zfill(2),
            True,
            (255, 255, 255),
        )
        win.blit(self.text, (self.x, self.y))

    def update(self):
        if self.start:
            self.actual = time.time()
            self.timer = self.actual - self.origine
        else:
            self.origine = time.time()

    def refresh(self):
        self.origine = time.time()
        self.start = True
        self.timer = 0
        self.save = 0
        self.s = "0"
        self.ms = "000"
        self.m = "0"
        self.h = "0"

    def getTime(self):
        return round(self.timer + self.save, 3)

    def pause(self):
        self.save += self.timer
        self.timer = 0
        self.start = False

    def resume(self):
        self.start = True
        self.origine = time.time()
