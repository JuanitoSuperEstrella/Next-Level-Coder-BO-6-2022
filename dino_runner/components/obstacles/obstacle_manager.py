import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, game):
        type_obstacle = [Cactus(SMALL_CACTUS), Bird(BIRD)]
        num_random = random.randint(0,1)
        if len(self.obstacles) == 0:
            self.obstacles.append(type_obstacle[num_random])

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.pop();         
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)