from scoreBoard import ScoreBoard
from enemy import Enemy
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
    screen = pygame.display.set_mode((1200,1000))
    pygame.display.set_caption("test app")
    
    score_board = ScoreBoard()
    map = Map("./stage.txt")
    block_group = map.get_blocks()
    cookie_group = map.get_cookies()
    powercookie_group = map.get_powercookies()
    enemy_group = map.get_enemys()
    # enemy = Enemy([416,416],block_group)
    # enemy_group = pygame.sprite.Group(enemy)
    packman = Packman([32,32],enemy_group, block_group, cookie_group,powercookie_group, score_board)
    my_group = pygame.sprite.Group(packman)
    
    add_enemy_timer = 0
    enemy_state=[True,True,True,True,True]

    GAME_STATE = 1
    
    clock = pygame.time.Clock()
    
    screen.fill((0,0,0))
    
    while True:
        
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
        if GAME_STATE == 1:
            my_group.update()
            my_group.draw(screen)
            p_x,p_y = packman.get_position()
            enemy_group.update(p_x,p_y,packman.immune_state)
            enemy_group.draw(screen)
            cookie_group.update(p_x,p_y)
            powercookie_group.update(p_x,p_y)
            block_group.draw(screen)
            cookie_group.draw(screen)
            powercookie_group.draw(screen)
            score_board.draw(screen)

            if len(enemy_group.sprites()) < 5:
                enemy_group.add(Enemy((352,320),block_group))
            
            if all(enemy_state):
                enemy_list = enemy_group.sprites()
                enemy_list[0].wait_state = False

            for index,enemy in enumerate(enemy_group):
                enemy_state[index] = enemy.wait_state

            if add_enemy_timer != 0 and add_enemy_timer % 1500 == 0:
                enemy_list = enemy_group.sprites()
                for index,enemy in enumerate(enemy_state):
                    if enemy == True:
                        enemy_list[index].wait_state = False
                        break

            add_enemy_timer += 1

            if packman.dead_state == True:
                GAME_STATE = 2

            if len(cookie_group.sprites()) == 0:
                GAME_STATE =3

        elif GAME_STATE == 2:
            gameover_font = pygame.font.SysFont(None, 80)
            gameover = gameover_font.render("GAME OVER", False, (255,0,0))
            screen.blit(gameover, ((400, 300)))

        elif GAME_STATE == 3:
            gameclear_font = pygame.font.SysFont(None, 80)
            gameclear = gameclear_font.render("GAME CLEAR", False, (255,255,255))
            screen.blit(gameclear, ((400, 300)))
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()