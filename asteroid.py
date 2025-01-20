import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):        
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)

        A = self.velocity.rotate(angle)
        B = self.velocity.rotate(-angle)

        A1 = Asteroid(self.position.x, self.position.y , (self.radius - ASTEROID_MIN_RADIUS))
        A1.velocity = A * 1.2
        A2 = Asteroid(self.position.x, self.position.y , (self.radius - ASTEROID_MIN_RADIUS))
        A2.velocity = B * 1.2