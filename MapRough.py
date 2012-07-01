# Map module

import pygame

grey = (55, 55, 55)

class Map(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(grey)
 
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        
        self.image.fill(grey)

    #def gen():

    #def update(self):