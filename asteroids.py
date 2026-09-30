
import pygame
import random
from logger import log_state, log_event
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, ASTEROID_MIN_RADIUS 
from circleshape import CircleShape
class Asteroids(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface, ) -> None :
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def split(self) -> None:
        if(self.radius >= ASTEROID_MIN_RADIUS):
            pygame.sprite.Sprite.kill(self)
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroids(self.position.x, self.position.y, split_radius)
            ast2 = Asteroids(self.position.x, self.position.y, split_radius)
            ast1.velocity = velocity1 * 1.2
            ast2.velocity = velocity2 * 1.2
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt   
