import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Red Screen')

# Define the red color
red = (255, 0, 255)


def draw_window():
    screen.fill(red)
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
