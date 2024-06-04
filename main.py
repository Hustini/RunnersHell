import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 710
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Runner Hell')

# Define the Background
BG = pygame.transform.scale(pygame.image.load('./img/background.jpeg'), (screen_width, screen_height))


def draw_window():
    screen.blit(BG, (0, 0))
    pygame.display.flip()


# Main game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draws stuff to the screen
    draw_window()

# Quit Pygame
pygame.quit()
sys.exit()
