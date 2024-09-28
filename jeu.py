import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1372, 950))
pygame.display.set_caption('Jeu de dame')
ecran_noir = pygame.image.load('écran noir.jpg')
ecran_noir = pygame.transform.scale(ecran_noir, (1000, 1000))
background = pygame.image.load('Jeu-de-Dames_01.png')
jeton_rouge = pygame.image.load('jeton rouge.jpg')
jeton_noir = pygame.image.load('jeton noir.png')
background = pygame.transform.scale(background, (972, 950))

class Jeton():
    def __init__(self, role, coord):
        self.role = role
        self.coord = coord

running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
