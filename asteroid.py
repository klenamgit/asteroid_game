from constants import LINE_WIDTH
from pygame import Color, Surface, draw
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: Surface, color="white",width=LINE_WIDTH):
        draw.circle(surface,color, (self.position.x, self.position.y), self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt