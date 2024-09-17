import pygame

import constants as const
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, const.PLAYER_RADIUS)

        self.rotation = 0
        self.cooldown = 0

    # in the player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        self.rotation += dt * const.PLAYER_TURN_SPEED

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * const.PLAYER_SPEED * dt

    def update(self, dt: float) -> None:
        if self.cooldown > 0:
            self.cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self) -> None:
        if self.cooldown <= 0:
            s = Shot(self.position.x, self.position.y)
            s.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * const.PLAYER_SHOT_SPEED
            )
            self.cooldown = const.PLAYER_SHOT_COOLDOWN
