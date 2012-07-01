#/usr/bin/env python

import pygame, random
from SurvivorRough import Survivor
from ReticleRough import Reticle
from MapRough import Map
from ZombieRough import Zombie

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Zombie Game')
screen = pygame.display.set_mode([1280, 1024])
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)

pygame.mouse.set_visible(False)

#Map.gen()
survivor = Survivor(50, 50, )
movingsprites = pygame.sprite.RenderPlain()
movingsprites.add(survivor)

reticle = Reticle()
movingsprites.add(reticle)

zombie = Zombie(random.randint(0, 1280), random.randint(0, 1024))
movingsprites.add(zombie)

wallList = pygame.sprite.RenderPlain()
#left wall
wall = Map(0, 0, 10, 1024)
wallList.add(wall)
#top wall
wall = Map(10, 0, 1270, 10)
wallList.add(wall)
#right wall
wall = Map(1270, 0, 10, 1024)
wallList.add(wall)
#bottom wall
wall = Map(0, 1014, 1270, 10)
wallList.add(wall)

def main():
    done = False

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if event.type == pygame.KEYDOWN or pygame.KEYUP:
                survivor.change_dir(event)

        #Map.update(screen)

        survivor.update(wallList)
        zombie.update(wallList, Survivor.survivor_x, Survivor.survivor_y)
        mousePos = pygame.mouse.get_pos()
        reticle.update(mousePos)
        
        screen.fill(black)
        
        movingsprites.draw(screen)
        wallList.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__': main()