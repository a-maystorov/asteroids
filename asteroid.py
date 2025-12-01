import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        x, y = self.position

        velocity1 = self.velocity.rotate(angle)
        asteroid1 = Asteroid(x, y, new_radius)
        asteroid1.velocity = velocity1 * 1.2

        velocity2 = self.velocity.rotate(-angle)
        asteroid2 = Asteroid(x, y, new_radius)
        asteroid2.velocity = velocity2 * 1.2
