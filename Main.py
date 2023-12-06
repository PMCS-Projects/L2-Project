import pygame
from pygame import K_ESCAPE
import random
import time

#Variables to create colors
white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

#sets frame rate
fps = pygame.time.Clock

#Screen size
screen = pygame.display.set_mode((600, 400))

#Name of the window
pygame.display.set_caption('L2 Test window')

#Fills the screen with a color
screen.fill(white)

#Updates screen
pygame.display.flip()

#Makes the program run
running = True

while running:
    #Constantly checks for event
    for event in pygame.event.get():
        #Makes escape close the window
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    #Initiates pygame
    pygame.init()
    #Display update keeps updating the screens
    pygame.display.update()
