#!/usr/bin/env python
# Survivor module

import pygame

white = (255, 255, 255)

class Survivor(pygame.sprite.DirtySprite):

    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((white))
        self.rect = self.image.get_rect()
        """
            self.image.load('(os.getenv('CURRENT_DIR))',  \
            '/resources/pictures/survivor.jpg')
        """
        self.rect.top = y
        self.rect.left = x
        
        sprites = pygame.sprite.allsprites

    def change_dir(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Survivor.change_speed(self, -2, 0)
            elif event.key == pygame.K_RIGHT:
                Survivor.change_speed(self, 2, 0)
            elif event.key == pygame.K_UP:
                Survivor.change_speed(self, 0, -2)
            elif event.key == pygame.K_DOWN:
                Survivor.change_speed(self, 0, 2)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Survivor.change_speed(self, 2, 0)
            elif event.key == pygame.K_RIGHT:
                Survivor.change_speed(self, -2, 0)
            elif event.key == pygame.K_UP:
                Survivor.change_speed(self, 0, 2)
            elif event.key == pygame.K_DOWN:
                Survivor.change_speed(self, 0, -2)

    def change_speed(self, x, y):
        Survivor.change_x += x
        Survivor.change_y += y

    def update(self):
        self.dirty = 1

        old_x = self.rect.left
        new_x = old_x + self.change_x
        self.rect.left = new_x

        old_y = self.rect.top
        new_y = old_y + self.change_y
        self.rect.top = new_y

        collided =  \
            functools.partial(pygame.sprite.spritecollide, self)
        
        for x in sprites:
            if collided (x):
                self.rect.left = old_x
                self.rect.top = old_y
