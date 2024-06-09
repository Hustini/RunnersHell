import pygame
import sys
from classes import Player
from classes import Pillar

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 710
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Runner Hell')

# Define the Background
BG = pygame.transform.scale(pygame.image.load('./img/background.jpeg'), (screen_width, screen_height))

# Define player and sprite group for animation
moving_sprites = pygame.sprite.Group()
player = Player(30, 550)
moving_sprites.add(player)

# sprite group for the pillar
pillar_sprite = pygame.sprite.Group()
pillars = [Pillar(-50, 0), Pillar(-50, 400), Pillar(-50, -400), Pillar(370, 0), Pillar(370, 400), Pillar(370, -400)]
for i in pillars:
    pillar_sprite.add(i)


def draw_window():
    screen.blit(BG, (0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.009)
    pillar_sprite.draw(screen)
    pygame.display.flip()


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not player.get_facing():
                    player.load_images('./img/player', 6, True)
                    player.set_facing(True)
                else:
                    player.load_images('./img/player', 6, False)
                    player.set_facing(False)

    # draws stuff to the screen
    draw_window()
    for pillar in pillars:
        pillar.move()

# Quit Pygame
pygame.quit()
sys.exit()
