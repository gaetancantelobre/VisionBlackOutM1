
import pygame

# Initialize pygame
pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls")

# Define the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the ball properties
ball_radius = 50
ball1_pos = (200, 300)
ball2_pos = (600, 300)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the balls
    pygame.draw.circle(screen, RED, ball1_pos, ball_radius)
    pygame.draw.circle(screen, BLUE, ball2_pos, ball_radius)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
