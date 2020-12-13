import pygame
from pygame.sprite import Sprite


class Heart(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()
