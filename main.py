from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame # type: ignore
import sys

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver} \nScreen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)  

    field = AsteroidField()

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
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60) / 1000




if __name__ == "__main__":
    main()
