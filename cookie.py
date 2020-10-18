import pygame
from pygame import Rect

class Cookie(pygame.sprite.Sprite):
    def __init__(self,position,filename):
        super(Cookie,self).__init__()
        self.image = pygame.image.load(filename).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self,p_x,p_y):
        self.collision(p_x=p_x,p_y=p_y)

    def collision(self,p_x,p_y):
        width = 30
        height = 30

        player_rect = Rect(p_x, p_y, width, height)
        collide = player_rect.colliderect(self.rect)
        if collide:  # 衝突するプレイヤーあり
            self.kill()
