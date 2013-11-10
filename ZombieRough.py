#!/usr/bin/env python
# Zombie module

import pygame, random
from functools import partial

green = (0, 255, 0)

class Zombie(pygame.sprite.DirtySprite):

    change_x = 0
    change_y = 0
    old_x = 0
    old_y = 0
    new_x = 0
    new_y = 0
    
    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self) 
        self.image = pygame.Surface([10, 10])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.x_velocity = 0
        self.y_velocity = 0

    def collidetest(self, surv, sprgroup):
        s_x = surv.rect.left
        s_y = surv.rect.top
        collided =  \
        pygame.sprite.spritecollideany(self, sprgroup)

        if collided:
            self.rect.top = self.old_y
            self.rect.left = self.old_x
        else:
            if self.rect.top < s_y:
                self.y_velocity = 1
            elif  self.rect.top > s_y:
                self.y_velocity = -1
            else:
                self.y_velocity = 0

            if  self.rect.left > s_x:
                self.x_velocity = -1
            elif self.rect.left < s_x:
                self.x_velocity = 1
            else:
                self.x_velocity = 0

    def update(self):
        self.dirty = 1
        self.old_x = self.rect.left
        self.new_x = self.old_x + self.change_x
        self.old_y = self.rect.top
        self.new_y = self.old_y + self.change_y
        self.rect.left = self.new_x
        self.rect.top = self.new_y
        self.rect.move_ip((self.x_velocity, self.y_velocity))
