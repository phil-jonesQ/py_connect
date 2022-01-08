"""
Class to create a player token YELLOW
"""

import pygame

class YellowToken(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, max_height) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.max_height = max_height
        self.image = pygame.image.load('assets/yellow_token.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def update(self):
        self.rect.y += self.speed

    def freeze(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def constrain(self):
        if self.rect.y > self.max_height:
            self.rect.y = self.max_height
            return (self.rect.x, self.rect.y)
            
    def collide(self, sprite, sprites):
        if pygame.sprite.spritecollide(sprite, sprites, False):
            print("Yellow Collide with red")
            sprite.rect.y = sprite.rect.y - 10 # Freeze piece
            return (sprite.rect.x, sprite.rect.y)


