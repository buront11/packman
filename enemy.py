from os import kill
import pygame
import math
from pygame import Rect

class Enemy(pygame.sprite.Sprite):

    MOVESPEED = 2.0

    def __init__(self,position, blocks):
        super(Enemy,self).__init__()
        self.images = list()
        self.images.append(pygame.image.load('./img/enemy.png').convert())
        self.images.append(pygame.image.load('./img/enemyweek.png').convert())
        
        self.index = 0

        self.image = self.images[self.index]

        self.move_dict = {'R':[self.MOVESPEED,0],'L':[-self.MOVESPEED,0],'U':[0,-self.MOVESPEED],'D':[0,self.MOVESPEED]}
        self.previous_action = None

        self.dead_state = False
        self.wait_state = True
        self.ignore_timer = 300

        self.blocks = blocks

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = position[0],position[1]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self,p_x,p_y,player_immune_state):
        if self.wait_state:
            pass
        else:
            if player_immune_state:
                self.index = 1
                max_distance = 0
                for move, speed in self.move_dict.items():
                    if self.collision(speed[0],speed[1]):
                        if self.chase_player(p_x,p_y,speed[0],speed[1]) > max_distance:
                            if self.move_reverser(move):
                                next_move = move
                                max_distance = self.chase_player(p_x,p_y,speed[0],speed[1])
            else:
                self.index = 0
                min_distance = 1000000.0
                for move, speed in self.move_dict.items():
                    if self.collision(speed[0],speed[1]):
                        if self.chase_player(p_x,p_y,speed[0],speed[1]) < min_distance:
                            if self.move_reverser(move):
                                next_move = move
                                min_distance = self.chase_player(p_x,p_y,speed[0],speed[1])
                        
                    print(min_distance,end=" ")
                print()
                print(min_distance)
                self.ignore_timer -= 1

            self.image = self.images[self.index]
            tmp = self.move_dict[next_move]
            if self.collision(tmp[0],tmp[1]):
                self.x += tmp[0]
                self.y += tmp[1]

            if self.ignore_timer <= 0:
                self.immune_ignore_state = False

            if self.dead_state:
                self.kill()

            self.previous_action = next_move

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def chase_player(self,p_x,p_y,next_x,next_y):
        # プレイヤーとの最短距離を計算
        player_x = p_x
        player_y = p_y

        width = 32
        height = self.rect.height

        newx = self.x + next_x
        newy = self.y + next_y

        Norm_x = abs(player_x-newx)
        Norm_y = abs(player_y-newy)

        return math.sqrt(Norm_x**2+Norm_y**2)

    def collision(self,verx,very):
        width = 32
        height = 32

        newx = self.x + verx
        newrectx = Rect(newx, self.y, width, height)
        newy = self.y + very
        newrecty = Rect(self.x, newy, width, height)

        # ブロックとの衝突判定
        for block in self.blocks:
            collide_x = newrectx.colliderect(block.rect)
            collide_y = newrecty.colliderect(block.rect)
            if collide_x:  # 衝突するブロックあり
                return False
            elif collide_y:  # 衝突するブロックあり
                return False
            
        return True

    def move_reverser(self, move):
        if move =='R':
            if self.previous_action == 'L':
                return False
        elif move == 'L':
            if self.previous_action == 'R':
                return False
        elif move == 'U':
            if self.previous_action == 'D':
                return False
        elif move == 'D':
            if self.previous_action == 'U':
                return False
    
        return True