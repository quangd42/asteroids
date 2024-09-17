import sys

import pygame

import constants as const
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()

    print(f"Screen width: {const.SCREEN_WIDTH}")
    print(f"Screen height: {const.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    dt: float = 0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(const.SCREEN_WIDTH / 2, const.SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # TODO: typing?
        for thing in drawable:
            thing.draw(screen)
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collided(player):
                sys.exit("Game over!")
            for shot in shots:
                if shot.is_collided(asteroid):
                    asteroid.split()
                    shot.kill()

        # Redraw screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
