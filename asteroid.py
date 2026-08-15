from constants import *
from circleshape import CircleShape
from logger import log_event
import pygame # pyright: ignore[reportMissingImports]
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", pygame.Vector2(self.position), self.radius,width = LINE_WIDTH)
    def update(self, dt):
        self.position = self.position + self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            newV1 = self.velocity.rotate(angle)
            newV2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Ast1 = Asteroid(self.position, self.position, new_radius)
            Ast2 = Asteroid(self.position, self.position, new_radius)
            Ast1.velocity = newV1 * 1.2
            Ast2.velocity = newV2 * 1.2
