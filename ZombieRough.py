# Zombie module

import pygame, random

green = (0, 255, 0)

class Zombie(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([10, 10])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self, wallList, survivorX, survivorY):
        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        self.rect.top = new_y

        self.rect.move_ip((self.x_velocity, self.y_velocity))

        collide = pygame.sprite.spritecollide(self, wallList, False)

        if self.rect.top < survivorY:
            self.y_velocity = 1
            if collide:
                self.rect.top = old_y
                self.y_velocity = 0
        elif  self.rect.top > survivorY:
            self.y_velocity = -1
            if collide:
                self.rect.top = old_y
                self.y_velocity = 0
        else:
            self.y_velocity = 0

        collide = pygame.sprite.spritecollide(self, wallList, False)

        if  self.rect.left > survivorX:
            self.x_velocity = -1
            if collide:
                self.rect.left = old_x
                self.x_velocity = 0
        elif self.rect.left < survivorX:
            self.x_velocity = 1
            if collide:
                self.rect.left = old_x
                self.x_velocity = 0
        else:
            self.x_velocity = 0


        if self.rect.left < 10:
            self.rect.left = 10
        elif self.rect.right > 1270:
            self.rect.right = 1270

        if self.rect.top <= 10:
            self.rect.top = 10
        elif self.rect.bottom >= 1014:
            self.rect.bottom = 1014