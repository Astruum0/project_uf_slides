import pygame
from moviepy.editor import VideoFileClip


def tutorial():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        tutorial = VideoFileClip("sound_video/movie_tutorial.mp4")
        tutorial.preview(fps=60)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu()
