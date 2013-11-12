#/usr/bin/env python

import pygame, random
from SurvivorRough import Survivor
from ReticleRough import Reticle
from MapRough import Map
from ZombieRough import Zombie
from ProjectileRough import Projectile

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

def main():

    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.set_caption('Zombie Game')
    screen = pygame.display.set_mode((1280, 1024))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.mouse.set_visible(False)

    done = False

    #sprites
    survivor = Survivor(50, 50, )
    reticle = Reticle()
    zombie = Zombie(random.randint(0, 1280), \
                    random.randint(0, 1024))
    projectile = Projectile(0, 0)

    #walls
    lwall = Map(0, 0, 10, 1024)
    twall = Map(10, 0, 1270, 10)
    rwall = Map(1270, 0, 10, 1024)
    bwall = Map(0, 1014, 1270, 10)

    allsprites = pygame.sprite.LayeredDirty((lwall, \
                 twall, rwall, bwall, survivor, \
                 reticle, zombie, projectile))

    survgroup = pygame.sprite.Group()
    survgroup.add(lwall, twall, rwall, bwall,  \
                  zombie)
    zombgroup = pygame.sprite.Group()
    zombgroup.add(lwall, twall, rwall, bwall,  \
                  survivor)
    projgroup = pygame.sprite.Group()
    projgroup.add(lwall, twall, rwall, bwall,  \
                  zombie)
    

    allsprites.clear(screen, background)

    clock = pygame.time.Clock()

    done = False
    while not done:
        mousePos = pygame.mouse.get_pos()
        m_x = mousePos[0]
        m_y = mousePos[1]
        mouseClick = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN or pygame.KEYUP:
                survivor.change_dir(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == button1:
                    projectile.fired()

        allsprites.update()
        survivor.collidetest(survgroup)
        zombie.collidetest(survivor, zombgroup)
        projectile.collidetest(survivor, projgroup)
        rects = allsprites.draw(screen)
        pygame.display.update(rects)
        
    pygame.quit()

if __name__ == '__main__': 
    main()
