import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, MUERTE_SOuND, LARGE_CACTUS, GAME_OVER


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        self.muerte = MUERTE_SOuND

    def update(self, game_speed, game):
        type_obstacle = [Cactus(SMALL_CACTUS), Bird(BIRD,random.randint(0,1)), LargeCactus(LARGE_CACTUS)]
        num_random = random.randint(0,2)
        if len(self.obstacles) == 0:
            self.obstacles.append(type_obstacle[num_random])

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    self.muerte.play()
                    pygame.time.delay(1500)
                    game.playing = False
                    break
                else:
                    self.obstacles.pop()
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)