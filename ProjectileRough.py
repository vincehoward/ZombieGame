# Projectile module

import pygame, random

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
        m_x = 0
        m_y = 0
        s_x = 0
        s_y = 0
    
    def fired(self):
        self.dirty = 1

    def update(self, z_x, z_y):

        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        self.rect.top = new_y

        self.rect.move_ip((self.x_velocity, self.y_velocity))

        collide =  \
            pygame.sprite.spritecollide(self, zombie, False)

        if self.rect.left == z_x and self.rect.top == z_y:
            self.dirty = 0

        if  self.rect.left > m_x:
            self.x_velocity = -5
            if collide:
                self.dirty = 0
        elif self.rect.left < m_x:
            self.x_velocity = 5
            if collide:
                self.dirty = 0

        if self.rect.top > m_y:
            self.y_velocity = -5
            if collide:
                self.dirty = 0
        elif self.rect.top < m_y:
            self.y_velocity = 5
            if collide:
                self.dirty = 0

        if self.rect.top > (s_y + 10)  \
           or self.rect.top < (s_y - 10):
            self.dirty = 0
        elif self.rect.top > (s_y + 10)  \
             or self.rect.top < (s_y - 10):
            self.dirty = 0

        collide =  \
            pygame.sprite.spritecollide(self, wallList, False)
        if collide:
            self.rect.left = old_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        self.rect.top = new_y

        collide =  \
            pygame.sprite.spritecollide(self, wallList, False)
        if collide:
            self.rect.top = old_y

"""
        collided = pygame.sprite.spritecollide(collided)
        
        for x in collided:
            if x == zombie:
                self.dirty = 0
            elif x
"""