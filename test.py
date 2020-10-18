from block import Block
from pygame.locals import *
from map import Map
import pygame
import player
import sys

from player import Packman

FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((510,510))
    pygame.display.set_caption("test app")
    
    map = Map("./stage.txt")
    
    clock = pygame.time.Clock()
    
    while True:
        
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
        map.update()
        map.draw()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()