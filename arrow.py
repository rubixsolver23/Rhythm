import pygame
from pygame.locals import *
import constants

class Arrow:
    ARROW_HEIGHT = 64
    def __init__(self, direction="up"):
        self.direction = direction
        self.img = pygame.image.load(f"IMAGE/arrow_{direction}.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.rect = self.img.get_rect()

        self.height = self.rect.height

        self.y = -self.height/2
        self.speed = 200  # Speed of the arrow falling down (pixels per second)

        match direction:
            case "up":
                self.rect.centerx = constants.WINDOWWIDTH * (5/11)
            case "down":
                self.rect.centerx = constants.WINDOWWIDTH * (6/11)
            case "left":
                self.rect.centerx = constants.WINDOWWIDTH * (4/11)
            case "right":
                self.rect.centerx = constants.WINDOWWIDTH * (7/11)


    def tick(self, mainClock):
        self.y += self.speed * mainClock.get_time() / 1000.0  # Move the arrow down based on speed and delta time
        self.y = round(self.y)
        self.rect.centery = self.y


