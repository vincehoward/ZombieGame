# Projectile module

import pygame, random
from functools import partial

grey = (55, 55, 55)

class Projectile(pygame.sprite.DirtySprite):

    change_x = 0
    change_y = 0
    
    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self) 
        self.image = pygame.Surface([2, 2])
        self.image.fill(grey)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.x_velocity = 0
        self.y_velocity = 0
        self.m_x = 0
        self.m_y = 0
    
    def fired(self):
        self.dirty = 1
        mousePos = pygame.mouse.get_pos()
        self.m_x = mousePos[0]
        self.m_y = mousePos[1]

    def update(self):

        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        self.rect.top = new_y
        
        surv = pygame.sprite.survivor

        self.rect.move_ip((self.x_velocity, self.y_velocity))
  
        scircle = pygame.sprite.collide_circle_ratio(2.5)
        scollided = scircle(self, surv)

        sprites = pygame.sprite.LayeredDirty.sprites

        collided =  \
            partial(pygame.sprite.spritecollide, self)
        
        for x in sprites:
            if collided (x):
                self.dirty = 0
            elif not scollided:
                self.dirty = 0
            else:
                if  self.rect.left > m_x:
                    self.x_velocity = -5
                elif self.rect.left < m_x:
                    self.x_velocity = 5

                if self.rect.top > m_y:
                    self.y_velocity = -5
                elif self.rect.top < m_y:
                    self.y_velocity = 5