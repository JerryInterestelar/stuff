import pygame

class Point:
    def __init__(self, x, y, r, color):
        self.pos_x = x
        self.pos_y = y
        self.r = r
        self.draw(color)

    def draw(self, color):
        self.surface = pygame.Surface((self.r*2, self.r*2))
        self.shape = pygame.draw.circle(self.surface, color, (self.r, self.r), self.r)
        self.surface.set_colorkey((0,0,0))
