import pygame
from constants import *
from player import Player, Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initializing the game
    pygame.init()

    # Setting the screen resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Setting up the gaming clock
    clock = pygame.time.Clock()
    dt = 0

    # Creating the groups
    updatables, drawables, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    Shot.containers = (updatables, drawables, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatables.update(dt)
        for asteroid in asteroids:
            if not asteroid.collision(player):
                exit()
            for shot in shots:
                if not asteroid.collision(shot):
                    shot.kill()
                    asteroid.kill()

        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
