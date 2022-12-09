
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image, count):
        self.count = count + 1
        self.type = self.count % 2
        super().__init__(image, self.type)
        self.rect.y = 250
