import pygame
import time
from tutorial_rules import tutorial
from moviepy.editor import VideoFileClip
from game import Game
from levelselector import levelSelector
from leaderboard import leaderboard


game = Game()
pygame.init()

pygame.display.set_caption("SLIDES")
gameIcon = pygame.image.load("menuframes/game_icon_32x32.png")
pygame.display.set_icon(gameIcon)
clock = pygame.time.Clock()


def intro_video():
    intro = VideoFileClip("sound_video/movie_intro.mp4")
    intro.preview(fps=60)
    main_menu()


def main_menu():
    ###DEFINITION VARIABLES###
    display_width = 600
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    PlayImg = pygame.image.load("menuframes/PlayButton_Neutral.png")
    EditorImg = pygame.image.load("menuframes/EditorButton_Neutral.png")
    SelectLevelImg = pygame.image.load("menuframes/SelectLevel_Neutral.png")
    RulesImg = pygame.image.load("menuframes/Rules_Neutral.png")
    QuitImg = pygame.image.load("menuframes/QuitButton_Neutral.png")
    LogoImg = pygame.image.load("menuframes/mainlogo.png")
    LeaderBoardImg = pygame.image.load("menuframes/leaderboard.png")
    soundImg = [
        pygame.image.load("menuframes/sound_on.png"),
        pygame.image.load("menuframes/sound_off.png"),
    ]
    soundOn = True

    SizeX = 373
    SizeY = 49
    PlusX = 113.5
    PlayImgPlusY = 250
    EditorImgPlusY = 305
    SelectLevelPlusY = 360
    RulesImgPlusY = 415
    SizeXQuit = 127
    PlusXQuit = 236.5
    QuitButtonPlusY = 525
    ######
    ###MUSIQUE###
    pygame.mixer.music.load("sound_video/mainmenutheme.mp3")
    pygame.mixer.music.play()
    click_sound = pygame.mixer.Sound("sound_video/click.wav")
    select_sound = pygame.mixer.Sound("sound_video/select.wav")
    pygame.mixer.init()

    play_select = [True, True, True, True, True]
    #########
    ###GAME LOOP###
    MenuRunning = True
    while MenuRunning:
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        gameDisplay.fill((0, 0, 0))
        pygame.display.set_caption("SLIDES")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MenuRunning = False
            ###PLAY BUTTON MOUSEOVER AND ACTION###

            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > PlayImgPlusY
                and event.pos[1] < PlayImgPlusY + SizeY
            ):
                if play_select[0] and soundOn:
                    pygame.mixer.Sound.play(select_sound)
                    play_select[0] = False
                PlayImg = pygame.image.load("menuframes/PlayButton_Hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > PlayImgPlusY
                and event.pos[1] < PlayImgPlusY + SizeY
            ):
                pygame.mixer.music.stop()
                if soundOn:
                    pygame.mixer.Sound.play(click_sound)
                game.runGame()
            else:
                play_select[0] = True
                PlayImg = pygame.image.load(
                    "menuframes/PlayButton_Neutral.png")

            ###PLAY BUTTON END###
            ###EDITOR BUTTON MOUSEOVER AND ACTION###

            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > EditorImgPlusY
                and event.pos[1] < EditorImgPlusY + SizeY
            ):
                if play_select[1] and soundOn:
                    pygame.mixer.Sound.play(select_sound)
                    play_select[1] = False
                EditorImg = pygame.image.load(
                    "menuframes/EditorButton_Hover.png")
            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > EditorImgPlusY
                and event.pos[1] < EditorImgPlusY + SizeY
            ):
                pygame.mixer.music.stop()
                if soundOn:
                    pygame.mixer.Sound.play(click_sound)
                game.clearLevel()
                game.runEditor()
            else:
                play_select[1] = True
                EditorImg = pygame.image.load(
                    "menuframes/EditorButton_Neutral.png")

            ###EDITOR BUTTON END###
            ###SELECT LEVEL BUTTON MOUSEOVER AND ACTION###

            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > SelectLevelPlusY
                and event.pos[1] < SelectLevelPlusY + SizeY
            ):
                if play_select[2] and soundOn:
                    pygame.mixer.Sound.play(select_sound)
                    play_select[2] = False
                SelectLevelImg = pygame.image.load(
                    "menuframes/SelectLevel_Hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > SelectLevelPlusY
                and event.pos[1] < SelectLevelPlusY + SizeY
            ):
                if soundOn:
                    pygame.mixer.Sound.play(click_sound)
                levelSelector()
            else:
                play_select[2] = True
                SelectLevelImg = pygame.image.load(
                    "menuframes/SelectLevel_Neutral.png")

            ###SELECT LEVEL END###
            ###RULES MOUSEOVER AND ACTION###

            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > RulesImgPlusY
                and event.pos[1] < RulesImgPlusY + SizeY
            ):
                if play_select[3] and soundOn:
                    pygame.mixer.Sound.play(select_sound)
                    play_select[3] = False
                RulesImg = pygame.image.load("menuframes/Rules_Hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusX
                and event.pos[0] < PlusX + SizeX
                and event.pos[1] > RulesImgPlusY
                and event.pos[1] < RulesImgPlusY + SizeY
            ):
                if soundOn:
                    pygame.mixer.Sound.play(click_sound)
                tutorial()
            else:
                play_select[3] = True
                RulesImg = pygame.image.load("menuframes/Rules_Neutral.png")

            ###RULES BUTTON END###
            ###QUIT BUTTON MOUSEOVER AND ACTION###

            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > PlusXQuit
                and event.pos[0] < PlusXQuit + SizeXQuit
                and event.pos[1] > QuitButtonPlusY
                and event.pos[1] < QuitButtonPlusY + SizeY
            ):
                if play_select[4] and soundOn:
                    pygame.mixer.Sound.play(select_sound)
                    play_select[4] = False
                QuitImg = pygame.image.load("menuframes/QuitButton_Hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > PlusXQuit
                and event.pos[0] < PlusXQuit + SizeXQuit
                and event.pos[1] > QuitButtonPlusY
                and event.pos[1] < QuitButtonPlusY + SizeY
            ):
                if soundOn:
                    pygame.mixer.Sound.play(click_sound)
                MenuRunning = False
            else:
                play_select[4] = True
                QuitImg = pygame.image.load(
                    "menuframes/QuitButton_Neutral.png")

            ### SOUND ###
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] < 75
                and event.pos[1] > 525
                and event.pos[0] > 25
                and event.pos[1] < 575
            ):
                soundOn = not soundOn
                if soundOn:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.stop()
            ### LEADERBOARD ###

            if (
                event.type != pygame.MOUSEBUTTONDOWN
                and event.type == pygame.MOUSEMOTION
                and event.pos[0] > 525
                and event.pos[1] > 525
                and event.pos[0] < 575
                and event.pos[1] < 575
            ):
                if play_select[4] and soundOn:
                    pygame.mixer.Sound.play(select_sound)
                    play_select[4] = False
                LeaderBoardImg = pygame.image.load(
                    "menuframes/leaderboard_hover.png")

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.pos[0] > 525
                and event.pos[1] > 525
                and event.pos[0] < 575
                and event.pos[1] < 575
            ):
                if soundOn:
                    pygame.mixer.Sound.play(click_sound)
                leaderboard()
            else:
                play_select[4] = True
                LeaderBoardImg = pygame.image.load(
                    "menuframes/leaderboard.png")

        gameDisplay.blit(PlayImg, (PlusX, PlayImgPlusY))
        gameDisplay.blit(EditorImg, (PlusX, EditorImgPlusY))
        gameDisplay.blit(SelectLevelImg, (PlusX, SelectLevelPlusY))
        gameDisplay.blit(RulesImg, (PlusX, RulesImgPlusY))
        gameDisplay.blit(QuitImg, (PlusXQuit, QuitButtonPlusY))
        gameDisplay.blit(LogoImg, (75, 75))
        gameDisplay.blit(LeaderBoardImg, (525, 525))
        if soundOn:
            gameDisplay.blit(soundImg[0], (25, 525))
        else:
            gameDisplay.blit(soundImg[1], (25, 525))
        pygame.display.update()

    pygame.quit()


# main_menu()
intro_video()
