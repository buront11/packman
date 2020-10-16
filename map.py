from block import Block
import pygame


class Map():
    def __init__(self, filename):
        super(Map,self).__init__()
        self.GS = 32
        self.all = pygame.sprite.RenderUpdates()
        self.blocks = pygame.sprite.Group()
        
        self.load(filename)
        
        
    
    def draw(self):
        self.surface.fill((0,0,0))
        self.all.draw(self.surface)
    
    def update(self):
        self.all.update()
        
    def get_map(self):
        return self.blocks

    
    def load(self, filename):
        map = []
        fp = open(filename,"r")
        for i in fp:
            item = i.rstrip()
            map.append(list(item))
            self.row = len(map)
            self.col = len(map[0])
        self.width = self.col * self.GS
        self.height = self.row * self.GS
        fp.close()
        
        for i in range(self.row):
            for j in range(self.col):
                if map[i][j] == 'B':
                    self.blocks.add(Block((j*self.GS,i*self.GS)))
            
        