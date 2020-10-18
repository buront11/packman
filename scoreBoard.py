import pygame
import sys

class ScoreBoard():
    def __init__(self):
        super(ScoreBoard,self).__init__()
        self.sysfont = pygame.font.SysFont(None,40)
        self.score = 0
    
    def draw(self, screen):
        score_img = self.sysfont.render(str(self.score), True, (255,255,0))
        x = 1100
        y = 100
        screen.blit(score_img, (x, y))
        
    def add_score(self, x):
        self.score += x