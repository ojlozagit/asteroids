import random

from circleshape import *
from constants   import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white",
                                  self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            # We want to split the old asteroid into two new ones
            # that aretravelling at faster and opposing angles
            new_angle       = random.uniform(20, 50)
            new_velocities  = [self.velocity.rotate(new_angle),
                               self.velocity.rotate(-new_angle)]
            new_radius      = self.radius - ASTEROID_MIN_RADIUS

            for v in range(len(new_velocities)):
                asteroid = Asteroid(self.position.x, self.position.y,
                                    new_radius)
                asteroid.velocity = new_velocities[v] * 1.2