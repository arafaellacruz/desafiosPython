# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

import pygame

pygame.init() #Iniciando a biblioteca
pygame.mixer.music.load('darth_vader.mp3') #Puxando o arquivo que quero carregar no código
pygame.mixer.music.play() #Dizendo o que ele deve fazer com o arquivo
pygame.event.wait() #Informando quando deve parar de executar.