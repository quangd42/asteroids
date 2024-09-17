from typing import Self
import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: int) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def is_collided(self, other: Self) -> bool:
        return self.position.distance_to(other.position) <= (self.radius + other.radius)
