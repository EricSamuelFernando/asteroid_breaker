from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import pygame
from circleshape import CircleShape
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        updatable.update(dt)
        player.timer -=dt
        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        for thing in asteroids:
            for bullet in shots:
                if thing.collides_with(bullet):
                    log_event("asteroid_shot")
                    thing.split()
                    pygame.sprite.Sprite.kill(bullet)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             return
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
