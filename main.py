import pygame # type: ignore
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import random

def main():
    print("Starting Asteroids!")

    try:
        SCREEN_HEIGHT=int(input("Enter desired window height in px: "))
        SCREEN_WIDTH=int(input("Enter desired window width in px: "))

    except Exception:
        print("Height/Width must be numerical")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (rocks, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroidField = AsteroidField()

    while True:

        screen.fill("black")

        updatable.update(dt)
        for rock in rocks:
            if player.collisions(rock):
                print("Game over!")
                return
            for shot in shots:
                if shot.collisions(rock):
                    shot.kill()
                    rock.kill()
                    angle=random.uniform(20,50)
                    asteroid1 = Asteroid(rock.position[0], rock.position[1], rock.radius-ASTEROID_MIN_RADIUS)
                    asteroid2 = Asteroid(rock.position[0], rock.position[1], rock.radius-ASTEROID_MIN_RADIUS)
                    asteroid1.velocity = rock.velocity.rotate(angle)*1.2
                    asteroid2.velocity = rock.velocity.rotate(-angle)*1.2

        for draws in drawable:
            draws.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt=clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
