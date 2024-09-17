import random
import pygame
from circleshape import CircleShape
import constants as const


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: int) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += dt * self.velocity

    def split(self) -> None:
        self.kill()
        if self.radius > const.ASTEROID_MIN_RADIUS:
            split_angle = random.uniform(20, 50)
            new_radius = self.radius - const.ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = self.velocity.rotate(-split_angle) * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = self.velocity.rotate(split_angle) * 1.2
