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
            # loads, flips and rotates the image
            image = pygame.image.load(path)
            self.sprites.append(pygame.transform.rotate(pygame.transform.flip(image, True, False), 270))

    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]


class Pillar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load('./img/pillar.png'), (80, 400))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def move(self):
        self.y += 0.05
        self.rect.y = self.y
        if self.y >= 710:
            self.y = -400


if __name__ == '__main__':
    player = Player(10, 10)
    print(player)
