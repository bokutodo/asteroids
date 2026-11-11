from circleshape import CircleShape
import pygame
from constants import *
import random
from logger import log_event



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            asteroid1_vel = self.velocity.rotate(rand_angle)
            asteroid2_vel = self.velocity.rotate(-rand_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid1.velocity = asteroid1_vel * 1.2
            asteroid2.velocity = asteroid2_vel * 1.2
            



