import json
import pygame
import sys
import random
import time
from classes import Player
from classes import Pillar
from classes import Rocket
from classes import HealthBar


def give_name():  # Json data for the name
    name = str(input('Give me a name'))
    with open('./data.json', 'r') as file:
        data = json.load(file)

    data['player']['name'] = name

    with open('./data.json', 'w') as file:
        json.dump(data, file)


# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up
# give_name()
screen_width = 400
screen_height = 710
rocket_intervals = [0.25, 1]
FPS = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Runner Hell')
pygame.display.set_icon(pygame.image.load('./img/running_girl.png'))

# score
score_increment = 0.1
font = pygame.font.Font('./PressStart2P-Regular.ttf', 20)

# Define the Background
BG = pygame.transform.scale(pygame.image.load('./img/background.jpeg'), (screen_width, screen_height))

# Define player and sprite group for animation
moving_sprites = pygame.sprite.Group()
player = Player(130, 550)
moving_sprites.add(player)

# Health bar
health_bar = HealthBar(125, 10, 150, 30, 3)

# sprite group for the pillar
pillar_sprite = pygame.sprite.Group()
pillars = [Pillar(-50, 0), Pillar(-50, 400), Pillar(-50, -400), Pillar(370, 0), Pillar(370, 400), Pillar(370, -400)]
for i in pillars:
    pillar_sprite.add(i)

# sprite group for rockets
rocket_sprite = pygame.sprite.Group()


def create_rocket():
    x = random.randint(30, screen_width - 30)
    rocket = Rocket(x, 0)
    rocket_sprite.add(rocket)


start_time = time.time()
interval = random.uniform(rocket_intervals[0], rocket_intervals[1])


def end_screen():
    screen.fill((0, 0, 0))
    game_over_text = font.render('GAME OVER', True, (255, 0, 0))
    score_text = font.render(f'Score: {player.get_score()}', True, (255, 0, 0))
    screen.blit(game_over_text, (
        screen_width // 2 - game_over_text.get_width() // 2,
        screen_height // 2 - game_over_text.get_height() // 2 - 20))
    screen.blit(score_text, (
        screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - score_text.get_height() // 2 + 20))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def draw_window(score):
    screen.blit(BG, (0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.009)
    pillar_sprite.draw(screen)
    rocket_sprite.draw(screen)
    player.health.draw(screen)
    screen.blit(score, (180, 60))
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

    # collisions
    for rocket in rocket_sprite:
        gets_hit = pygame.sprite.spritecollide(player, rocket_sprite, True)
        if gets_hit:
            rocket_sprite.remove(rocket)
            player.reduce_health()

    # died
    if player.vital_sign():
        end_screen()

    # score
    player.increase_score(score_increment)
    score_text = font.render(f'{player.get_score()}', True, (255, 255, 255))

    # draws stuff to the screen
    draw_window(score_text)
    for pillar in pillars:
        pillar.move()
    for rocket in rocket_sprite:
        rocket.move()

    current_time = time.time()
    if current_time - start_time >= interval and not player.vital_sign():
        create_rocket()
        start_time = current_time
        interval = random.uniform(rocket_intervals[0], rocket_intervals[1])

    # gravity
    player.gravity()
    player.update(0.009)
    rocket_sprite.update(0.009)

# Quit Pygame
pygame.quit()
clock.tick(FPS)
sys.exit()
