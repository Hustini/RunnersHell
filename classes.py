import os
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('img/player/player1.png'))
        self.sprites.append(pygame.image.load('img/player/player2.png'))
        self.sprites.append(pygame.image.load('img/player/player3.png'))
        self.sprites.append(pygame.image.load('img/player/player4.png'))
        self.sprites.append(pygame.image.load('img/player/player5.png'))
        self.sprites.append(pygame.image.load('img/player/player6.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.x = x
        self.y = y

    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


if __name__ == '__main__':
    player = Player(10, 10)
    print(player)
