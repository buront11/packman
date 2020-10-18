from block import Block
from scoreBoard import ScoreBoard
import pygame
from pygame import Rect, image
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.transform import rotate

class Packman(pygame.sprite.Sprite):
    
    MOVE_SPEED = 2
    
    def __init__(self, position, enemys, blocks, cookies, powercookies, score_board):
        super(Packman,self).__init__()
        # 画像の設定用
        self.right_images = list()
        for i in range(5):
            self.right_images.append(pygame.image.load("./img/packman1.png").convert())
        for i in range(5):
            self.right_images.append(pygame.image.load("./img/packman2.png").convert())
        for i in range(5):
            self.right_images.append(pygame.image.load("./img/packman3.png").convert())
            
        self.left_images = list()
        for i in range(5):
            self.left_images.append(pygame.image.load("./img/packmanLeft1.png").convert())
        for i in range(5):
            self.left_images.append(pygame.image.load("./img/packmanLeft2.png").convert())
        for i in range(5):
            self.left_images.append(pygame.image.load("./img/packmanLeft3.png").convert())
            
        self.up_images = list()
        for i in range(5):
            self.up_images.append(pygame.image.load("./img/packmanUp1.png").convert())
        for i in range(5):
            self.up_images.append(pygame.image.load("./img/packmanUp2.png").convert())
        for i in range(5):
            self.up_images.append(pygame.image.load("./img/packmanUp3.png").convert())
        
        self.down_images = list()
        for i in range(5):
            self.down_images.append(pygame.image.load("./img/packmanDown1.png").convert())
        for i in range(5):
            self.down_images.append(pygame.image.load("./img/packmanDown2.png").convert())
        for i in range(5):
            self.down_images.append(pygame.image.load("./img/packmanDown3.png").convert())
        
        self.enemys = enemys
        self.score_board = score_board
        self.cookies = cookies
        self.powercookies = powercookies
        self.blocks = blocks
        self.score = 0
        self.index = 0
        self.dead_state = False
        self.immune_state = False
        self.immune_timer = 600
        self.image = self.right_images[self.index]
        self.rect = self.image.get_rect()
        
        self.rect.x, self.rect.y = position[0],position[1]
        
        self.dx = float(self.rect.x)
        self.dy = float(self.rect.y)
        
    def update(self):
        if self.index >= len(self.right_images):
            self.index = 0
            
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_RIGHT] and self.collision(self.MOVE_SPEED,0):
            self.collision_cookie(self.MOVE_SPEED,0)
            self.collision_powercookie(self.MOVE_SPEED,0)
            self.image = self.right_images[self.index]
            self.index += 1
            self.dx += self.MOVE_SPEED
        elif pressed_keys[K_LEFT] and self.collision(-1*self.MOVE_SPEED,0):
            self.collision_cookie(-1*self.MOVE_SPEED,0)
            self.collision_powercookie(-1*self.MOVE_SPEED,0)
            self.image = self.left_images[self.index]
            self.index += 1
            self.dx -= self.MOVE_SPEED
        elif pressed_keys[K_UP] and self.collision(0,-1*self.MOVE_SPEED):
            self.collision_cookie(0,-1*self.MOVE_SPEED)
            self.collision_powercookie(0,-1*self.MOVE_SPEED)
            self.image = self.up_images[self.index]
            self.index += 1
            self.dy -= self.MOVE_SPEED
        elif pressed_keys[K_DOWN] and self.collision(0,self.MOVE_SPEED):
            self.collision_cookie(0,self.MOVE_SPEED)
            self.collision_powercookie(0,self.MOVE_SPEED)
            self.image = self.down_images[self.index]
            self.index += 1
            self.dy += self.MOVE_SPEED
        
        

        if self.immune_state:
            self.immune_timer -= 1
        
        if self.immune_timer <= 0:
            self.immune_state = False
            self.immune_timer = 600

        self.collision_enemy()

        self.rect.x = int(self.dx)
        self.rect.y = int(self.dy)
        
    def collision_cookie(self,verx,very):
        width = 30
        height = 30

        newx = self.dx + verx
        newrectx = Rect(newx, self.dy, width, height)
        newy = self.dy + very
        newrecty = Rect(self.dx, newy, width, height)

        # ブロックとの衝突判定
        for cookie in self.cookies:
            collide_x = newrectx.colliderect(cookie.rect)
            collide_y = newrecty.colliderect(cookie.rect)
            if collide_x:  # 衝突するブロックあり
                self.score_board.add_score(100)
            elif collide_y:  # 衝突するブロックあり
                self.score_board.add_score(100)

    def collision_powercookie(self,verx,very):
        width = 30
        height = 30

        newx = self.dx + verx
        newrectx = Rect(newx, self.dy, width, height)
        newy = self.dy + very
        newrecty = Rect(self.dx, newy, width, height)

        # ブロックとの衝突判定
        for cookie in self.powercookies:
            collide_x = newrectx.colliderect(cookie.rect)
            collide_y = newrecty.colliderect(cookie.rect)
            if collide_x:  # 衝突するブロックあり
                self.immune_state = True
            elif collide_y:  # 衝突するブロックあり
                self.immune_state = True
        # for power in self.powercookies:
        #     collide = self.rect.colliderect(power.rect)
        #     if collide:  # 敵するブロックあり
        #         self.immune_state = True

    def collision(self,verx,very):
        width = 30
        height = 30

        newx = self.dx + verx
        newrectx = Rect(newx, self.dy, width, height)
        newy = self.dy + very
        newrecty = Rect(self.dx, newy, width, height)

        # ブロックとの衝突判定
        for block in self.blocks:
            collide_x = newrectx.colliderect(block.rect)
            collide_y = newrecty.colliderect(block.rect)
            if collide_x:  # 衝突するブロックあり
                return False
            elif collide_y:  # 衝突するブロックあり
                return False
            
        return True

    def collision_enemy(self):
        # 敵との衝突判定
        for enemy in self.enemys:
            collide = self.rect.colliderect(enemy.rect)
            if collide:  # 敵するブロックあり
                if self.immune_state:
                    enemy.dead_state = True
                else:
                    self.dead_state = True

    def get_position(self):
        return self.rect.x,self.rect.y