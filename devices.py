import pygame
pygame.joystick.init()

####DEBUG###


def controller_inputs():
    joysticks = []
    clock = pygame.time.Clock()

    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print("-------------------")
        print("Manettes detectees :", joysticks[-1].get_name())

        clock.tick(60)
        gameDisplay = pygame.display.set_mode((600, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    print("AA")
                if event.button == 1:
                    print("BB")
                if event.button == 2:
                    print("CC")
                if event.button == 3:
                    print("DD")
        pygame.display.update()


##############

controller_inputs()
