import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('C:/Users/Tec01/OneDrive/Música/Deep Sea(MP3_160K).mp3')
pygame.mixer.music.play(loops=0, start=123.0)
while pygame.mixer.music.get_busy():
    pass

