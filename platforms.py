import pygame
from pygame.locals import *

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 0))

        self.rect = self.image.get_rect()