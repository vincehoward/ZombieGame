# Reticle module

import pygame

red = (255, 0, 0)

class Reticle(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((red))
        self.rect = self.image.get_rect()
        
    def update(self, m_x, m_y):
        self.dirty = 1
        self.rect.left = m_x
        self.rect.top = m_y