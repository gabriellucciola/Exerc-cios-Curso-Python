import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('../Extras/sekaisaikou.mp3')  # precisa colar a música na pasta onde está o arquivo
pygame.mixer.music.play()
pygame.event.wait()
