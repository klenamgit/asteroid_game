from constants import SHOT_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from pygame import Surface, draw

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface: Surface, color="white",width=LINE_WIDTH):
        draw.circle(surface,color, (self.position.x, self.position.y), self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt