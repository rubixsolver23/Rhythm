import pygame
import sys
from pygame.locals import *

import constants
import colors
import arrow

import demo_arrow_spawn


mainClock = pygame.time.Clock()
pygame.init()

windowSurface = pygame.display.set_mode((constants.WINDOWWIDTH, constants.WINDOWHEIGHT), flags=pygame.SCALED, depth=32, vsync=1)
pygame.display.set_caption("Rhythm")


def main():
    ticker = 0

    up_arrows = []
    down_arrows = []
    left_arrows = []
    right_arrows = []


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        pass
                    case pygame.K_DOWN:
                        pass
                    case pygame.K_LEFT:
                        pass
                    case pygame.K_RIGHT:
                        pass
        
        # Spawn arrows at regular intervals
        ticker = demo_arrow_spawn.spawn_tick(up_arrows, down_arrows, left_arrows, right_arrows, ticker)
        
        for arrow_list in [up_arrows, down_arrows, left_arrows, right_arrows]:
            for arrow_instance in arrow_list:
                arrow_instance.tick(mainClock)
        
        # Garbage collection for arrows that have gone off the screen
        up_arrows = [arrow_instance for arrow_instance in up_arrows if arrow_instance.rect.top < constants.WINDOWHEIGHT]
        down_arrows = [arrow_instance for arrow_instance in down_arrows if arrow_instance.rect.top < constants.WINDOWHEIGHT]
        left_arrows = [arrow_instance for arrow_instance in left_arrows if arrow_instance.rect.top < constants.WINDOWHEIGHT]
        right_arrows = [arrow_instance for arrow_instance in right_arrows if arrow_instance.rect.top < constants.WINDOWHEIGHT]
                
        
        # Draw the screen
        windowSurface.fill(colors.WHITE)

        for arrow_list in [up_arrows, down_arrows, left_arrows, right_arrows]:
            for arrow_instance in arrow_list:
                windowSurface.blit(arrow_instance.img, arrow_instance.rect)
        
        pygame.display.update()  # Update the display
        mainClock.tick(60)  # Limit to 60 frames per second


main()