from enemy import Enemy
from block import Block
from cookie import Cookie
from powercookie import PowerCookie
import pygame


class Map():
    def __init__(self, filename):
        super(Map,self).__init__()
        self.GS = 32
        self.all = pygame.sprite.RenderUpdates()
        self.enemys = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.spblocks = pygame.sprite.Group()
        self.cookies = pygame.sprite.Group()
        self.powercookies = pygame.sprite.Group()
        self.map = []
        self.row = 0
        self.col = 0

        self.load(filename)
        self.make_enemy()
    
    def draw(self):
        self.surface.fill((0,0,0))
        self.all.draw(self.surface)
    
    def update(self):
        self.all.update()
        
    def get_blocks(self):
        return self.blocks

    def get_spblocks(self):
        return self.spblocks

    def get_cookies(self):
        return self.cookies

    def get_powercookies(self):
        return self.powercookies

    def get_enemys(self):
        return self.enemys

    def make_enemy(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.map[i][j] == 'E':
                    self.enemys.add(Enemy((j*self.GS,i*self.GS),self.blocks))
    
    def load(self, filename):
        fp = open(filename,"r")
        for i in fp:
            item = i.rstrip()
            self.map.append(list(item))
            self.row = len(self.map)
            self.col = len(self.map[0])
        self.width = self.col * self.GS
        self.height = self.row * self.GS
        fp.close()
        
        for i in range(self.row):
            for j in range(self.col):
                if self.map[i][j] == 'B':
                    self.blocks.add(Block((j*self.GS,i*self.GS)))
                elif self.map[i][j] == 'C':
                    self.cookies.add(Cookie((j*self.GS+10,i*self.GS+10),"./img/cookie.png"))
                elif self.map[i][j] == 'P':
                    self.powercookies.add(PowerCookie((j*self.GS+5,i*self.GS+5),"./img/powercookie.png"))
                