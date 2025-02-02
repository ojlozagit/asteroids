# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # -> pygame.surface.Surface()
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True: # gameLoop
        # we want to allow the user to exit the screen/gameLoop via the x-button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # "black" is the equivalent to passing the (0,0,0) rgb tuple
        player.draw(screen)
        pygame.display.flip() # we want to refresh the screen at the end of the gameLoop
        dt = clock.tick(60) / 1000 # we want to pause the gameloop every 1/60 of a second, so as
                                   # to not be rate limited by the CPU's speed.
                                   # This time passed should then be saved as the delta (i.e.,
                                   # time passed since last frame/drawcall)

if __name__ == "__main__":
    main()
