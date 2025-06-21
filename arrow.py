import pygame
from pygame.locals import *
import constants

class Arrow:
    def __init__(self, direction="up"):
        self.direction = direction
        self.img = None  # Placeholder for the image, to be set later
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.height = 20 # placeholder for the height of the arrow

        self.y = -self.height/2
        self.speed = 200  # Speed of the arrow falling down (pixels per second)

        self.rect.center = (constants.WINDOWWIDTH // 2, self.y)  # Center the arrow horizontally


    def tick(self, mainClock):
        self.y += self.speed * mainClock.get_time() / 1000.0  # Move the arrow down based on speed and delta time
        self.y = round(self.y)
        self.rect.centery = self.y


