import pygame
import sys
from pygame.locals import *
import colors


mainClock = pygame.time.Clock()
pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), flags=pygame.SCALED, depth=32, vsync=1)
pygame.display.set_caption("Rhythm")


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        windowSurface.fill(colors.WHITE)  # Clear the screen with black
        pygame.display.update()  # Update the display
        mainClock.tick(60)  # Limit to 60 frames per second