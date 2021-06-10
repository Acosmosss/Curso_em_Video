# Primeira vez usando o pygame :)
import pygame
# Iniciando mixer do pygame 
pygame.mixer.init()
# Iniciando o pygame
pygame.init()
# Pegando a musica da pasta
pygame.mixer.music.load('Copie o diretorio da sua musica aqui.')
# Começando a musica, loops= quantas vezes vc quer repetir a musica.
# start= de que minuto ela começa em float(1 = 1 segundo)
pygame.mixer.music.play(loops=0, start=0)
# laço while para que a musica não pare, até acabar
while pygame.mixer.music.get_busy():
    pass

