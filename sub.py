import pygame
from pygame.locals import*
import sys

WHITE = (255,255,255)

def screen_print(screen):
    font = pygame.font.Font(None,50)
    text = "C:/Users/name> "
    text = font.render(text,True,WHITE)
    screen.blit(text,[0,0])
