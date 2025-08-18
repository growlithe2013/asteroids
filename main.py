import pygame # type: ignore
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    rocks = pygame.sprite.Group()

    Asteroid.containers = (rocks, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroidField = AsteroidField()

    while True:

        screen.fill("black")


        updatable.update(dt)

        for draws in drawable:
            draws.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt=clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
