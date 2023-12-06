import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import sys
import math

# Variables to create colors
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)

# Screen size
screen = pygame.display.set_mode((1000, 1000))

# Name of the window
pygame.display.set_caption('Sun and Earth Simulation')

# Initialize pygame
pygame.init()

# Set up sun properties
sun_radius = 50
sun_position = (0, 0)

# Set up earth properties
earth_radius = 20
earth_distance = 150
earth_angle = 0

# Frames per second
fps = 60
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the sun
    pygame.draw.circle(screen, yellow, sun_position, sun_radius)

    # Update earth position
    earth_x = sun_position[0] + earth_distance * math.cos(math.radians(earth_angle))
    earth_y = sun_position[1] + earth_distance * math.sin(math.radians(earth_angle))

    # Draw the earth
    pygame.draw.circle(screen, blue, (int(earth_x), int(earth_y)), earth_radius)

    # Update earth angle for animation
    earth_angle += 1  # You can adjust the speed by changing this value

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Quit pygame and exit the program
pygame.quit()
sys.exit()
