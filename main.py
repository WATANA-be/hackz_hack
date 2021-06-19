import pygame
from pygame.locals import*
import sys

import sub

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption("GAME")
    clock = pygame.time.Clock()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_z:
                pass


        screen.fill((0,0,0))

        #txt_input()
        sub.screen_print(screen)


        pygame.display.update()
        clock.tick()

if __name__ == "__main__":
    main()
