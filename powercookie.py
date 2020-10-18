import pygame
from cookie import Cookie

class PowerCookie(Cookie,pygame.sprite.Sprite):
    def __init__(self,position,filename):
        super(PowerCookie,self).__init__(position,filename)
        