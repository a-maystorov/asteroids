import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    score = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Final Score: {score}")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    score += 10
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
