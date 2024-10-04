import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
    	self.kill()
    	if self.radius <= ASTEROID_MIN_RADIUS:
    		return
    	random_angle = random.uniform(20,51)
    	
    	first = self.velocity.rotate(random_angle)
    	second = self.velocity.rotate(-random_angle)
    	new_radius = self.radius - ASTEROID_MIN_RADIUS
    	
    	astr_first = Asteroid(self.position.x, self.position.y, new_radius)
    	astr_second = Asteroid(self.position.x, self.position.y, new_radius)
    	
    	astr_first.velocity = first * 1.2
    	astr_second.velocity = second * 1.2
