import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)
        
        pos_new_angle = self.velocity.rotate(random_angle)
        neg_new_angle = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        pos_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        pos_new_asteroid.velocity = pos_new_angle * 1.2
        neg_new_asteroid.velocity = neg_new_angle * 1.2

