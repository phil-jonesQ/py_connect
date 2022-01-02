"""
Class to define a cell on the board
"""

import pygame

class BoardCell(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

        self.image = pygame.image.load('assets/board_element.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

