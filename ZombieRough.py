#!/usr/bin/env python
# Zombie module

import pygame, random
from functools import partial

green = (0, 255, 0)

class Zombie(pygame.sprite.DirtySprite):

    change_x = 0
    change_y = 0
    
    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self) 
        self.image = pygame.Surface([10, 10])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self):
        self.dirty = 1
        
        s = pygame.sprite.survivor.rect
        s_x = s[0]
        s_y = s[1]

        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        self.rect.top = new_y

        self.rect.move_ip((self.x_velocity, self.y_velocity))

        sprgroup = pygame.sprite.LayeredDirty
        sprites = sprgroup.sprites
        zom = pygame.sprite.zombie

        collided =  \
            pygame.sprite.spritecollideany(zom, sprgroup)

        if sprites in collided:
            self.rect.top = old_y
            self.rect.left = old_x
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