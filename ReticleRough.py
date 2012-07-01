# Reticle module

import pygame

red = (255, 0, 0)

class Reticle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((red))
        self.rect = self.image.get_rect()
        
    def update(self, pos):
        x = pos[0]
        y = pos[1]
        self.rect.left = x
        self.rect.top = y