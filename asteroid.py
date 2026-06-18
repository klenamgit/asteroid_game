from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from pygame import Color, Surface, draw
from circleshape import CircleShape
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: Surface, color="white",width=LINE_WIDTH):
        draw.circle(surface,color, (self.position.x, self.position.y), self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            log_event("asteroid_destroyed")
            return []
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            first_asteroid.velocity = self.velocity.rotate(random_angle) *1.2
            second_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            second_asteroid.velocity = first_asteroid.velocity.rotate(-random_angle) *1.2
            return [first_asteroid, second_asteroid]