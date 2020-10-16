import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,position):
        super(Block,self).__init__()
        self.image = pygame.image.load("./img/block.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = position