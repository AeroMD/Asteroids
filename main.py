from constants import *
from logger import log_state
from player import Player
import pygame # type: ignore

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} \nScreen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)  


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill("black")
            player.update(dt)
            player.draw(screen)
            pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60) / 1000




if __name__ == "__main__":
    main()
