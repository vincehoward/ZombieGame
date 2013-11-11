# Projectile module

import pygame, random
from functools import partial

grey = (55, 55, 55)

class Projectile(pygame.sprite.DirtySprite):

    change_x = 0
    change_y = 0
    m_x = 0
    m_y = 0
    old_x = 0
    old_y = 0
    new_x = 0
    new_y = 0
    radius = 0
    
    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self) 
        self.image = pygame.Surface([2, 2])
        self.image.fill(grey)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.x_velocity = 0
        self.y_velocity = 0
    
    def fired(self):
        self.dirty = 1
        mousePos = pygame.mouse.get_pos()
        self.m_x = mousePos[0]
        self.m_y = mousePos[1]

    def collidetest(self, surv, sprgroup):
        scircle = pygame.sprite.collide_circle_ratio(2.5)
        scollided = pygame.sprite.collide_circle(self, scircle)

        collided =  \
            pygame.sprite.spritecollideany(self, sprgroup)

        if collided:
            self.dirty = 0
        elif not scollided:
            self.dirty = 0
        else:
            if  self.rect.left > self.m_x:
                self.x_velocity = -5
            elif self.rect.left < self.m_x:
                self.x_velocity = 5

            if self.rect.top > self.m_y:
                self.y_velocity = -5
            elif self.rect.top < self.m_y:
                self.y_velocity = 5

    def update(self):
        self.old_x = self.rect.left
        self.new_x = self.old_x + self.change_x
        self.old_y = self.rect.top
        self.new_y = self.old_y + self.change_y
        self.rect.left = self.new_x
        self.rect.top = self.new_y
        self.rect.move_ip((self.x_velocity, self.y_velocity))
