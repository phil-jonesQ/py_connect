"""
Class to create a player token RED
"""

import pygame

class RedToken(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, max_height) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.max_height = max_height
        self.image = pygame.image.load('assets/red_token.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def update(self):
        self.rect.y += self.speed
        self.constrain()


    def constrain(self):
        if self.rect.y > self.max_height:
            self.rect.y = self.max_height

