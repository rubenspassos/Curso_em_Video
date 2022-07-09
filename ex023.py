'''import playsound

playsound.playsound('musica.mp3')'''

import pygame

pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(.3)
input(' Digite algo para encerrar')
# Só Funcionou quando coloquei o input.