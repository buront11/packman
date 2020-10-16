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
    screen = pygame.display.set_mode((480,480))
    pygame.display.set_caption("test app")
    
    map = Map("./stage.txt")
    block_group = map.get_map()
    packman = Packman([32,32],block_group)
    my_group = pygame.sprite.Group(packman)
    
    clock = pygame.time.Clock()
    
    screen.fill((0,0,0))
    
    while True:
        
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
        my_group.update()
        my_group.draw(screen)
        
        block_group.draw(screen)
        
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()