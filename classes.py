import os
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, animation_dir='./img/player', frames=6):
        super().__init__()
        self.sprites = []
        self.load_images(animation_dir, frames)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.x = x
        self.y = y

    def load_images(self, directory, frames):
        for i in range(1, frames + 1):
            path = os.path.join(directory, f'player{i}.png')
            self.sprites.append(pygame.image.load(path))

    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


if __name__ == '__main__':
    player = Player(10, 10)
    print(player)
