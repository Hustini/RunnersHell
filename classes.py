import os
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y


if __name__ == '__main__':
    pass
