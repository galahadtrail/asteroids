import pygame
from circleshape import *
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt