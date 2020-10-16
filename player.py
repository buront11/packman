from block import Block
import pygame
from pygame import Rect, image
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.transform import rotate

class Packman(pygame.sprite.Sprite):
    
    MOVE_SPEED = 2
    
    def __init__(self, position, blocks):
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
        
        self.blocks = blocks
        self.index = 0
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
            self.image = self.right_images[self.index]
            self.index += 1
            self.dx += self.MOVE_SPEED
        elif pressed_keys[K_LEFT] and self.collision(-1*self.MOVE_SPEED,0):
            self.image = self.left_images[self.index]
            self.index += 1
            self.dx -= self.MOVE_SPEED
        elif pressed_keys[K_UP] and self.collision(0,-1*self.MOVE_SPEED):
            self.image = self.up_images[self.index]
            self.index += 1
            self.dy -= self.MOVE_SPEED
        elif pressed_keys[K_DOWN] and self.collision(0,self.MOVE_SPEED):
            self.image = self.down_images[self.index]
            self.index += 1
            self.dy += self.MOVE_SPEED
        
        
        self.rect.x = int(self.dx)
        self.rect.y = int(self.dy)
        
        
        
    def collision(self,verx,very):
        width = self.rect.width
        height = self.rect.height

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