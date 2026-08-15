from constants import *
from circleshape import CircleShape
import pygame # pyright: ignore[reportMissingImports]

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", pygame.Vector2(self.position), self.radius, width = LINE_WIDTH)
    def update(self, dt):
        self.position = self.position + self.velocity * dt