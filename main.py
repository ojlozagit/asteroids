# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants      import *
from player         import *
from asteroid       import *
from asteroidfield  import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers        = (updatable, drawable)
    Asteroid.containers      = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True: # gameLoop

        # -- Event handling --
        # We want to allow the user to close screen via the x-button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        # --------------------

        # -- Rendering --
        screen.fill("black") # "black" == (0,0,0) rgb tuple
        for object in drawable:
            object.draw(screen)
        # drawable.draw(screen)
        pygame.display.flip() # used to refresh screen state
        # ---------------

        # We want to pause the gameloop every 1/60 of a second, so as
        # to not be rate limited by the CPU's speed.
        # This time passed should then be saved as the delta (i.e.,
        # time passed since last frame/drawcall)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
