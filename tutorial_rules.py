import pygame
from moviepy.editor import VideoFileClip


def tutorial():
    tutorial = VideoFileClip("sound_video/movie_tutorial.mp4")
    tutorial.preview(fps=60)
    return

