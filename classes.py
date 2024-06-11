import os
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, animation_dir='./img/player', frames=6):
        super().__init__()
        self.sprites = []
        # true = right, false = left
        self.facing = False
        self.load_images(animation_dir, frames, self.facing)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.x = x
        self.y = y

    def load_images(self, directory, frames, direction):
        self.sprites = []
        for i in range(1, frames + 1):
            path = os.path.join(directory, f'player{i}.png')
            # loads, flips and rotates the image
            image = pygame.image.load(path)
            self.sprites.append(pygame.transform.rotate(pygame.transform.flip(image, True, direction), 270))

    def update(self, speed):
        self.current_sprite += speed
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def get_facing(self):
        return self.facing

    def set_facing(self, value):
        self.facing = value

    def gravity(self):
        if self.facing:
            self.x += 1
            self.rect.x += 1
            if self.rect.x >= 275:
                self.x = 275
                self.rect.x = 275
        else:
            self.x -= 1
            self.rect.x -= 1
            if self.rect.x <= 30:
                self.x = 30
                self.rect.x = 30


class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y, img='./img/rocket.png'):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale_by(pygame.transform.rotate(pygame.image.load(img), 180), 0.1)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 0.5
        self.rect.y += 0.5
        if self.rect.y > 400:
            self.kill()


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
