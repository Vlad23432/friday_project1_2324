import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings



        self.image = pg.image.load('images/alien.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):

        self.screen.blit(self.image, self.rect)