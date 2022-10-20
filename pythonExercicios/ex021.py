#faça um programa que execute um mp3 ao rodar o programa
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass