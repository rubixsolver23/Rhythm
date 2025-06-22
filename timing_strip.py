import constants
import colors
import arrow
import pygame


class TimingStrip:
    def __init__(self, strip_location, perfect_buffer, good_buffer, ok_buffer, arrow_height):
        self.strip_location = strip_location
        self.perfect_buffer = perfect_buffer
        self.good_buffer = good_buffer
        self.ok_buffer = ok_buffer
        self.arrow_height = arrow_height

        self.perfect_strip = pygame.Rect(0, strip_location - perfect_buffer - arrow_height / 2, constants.WINDOWWIDTH, arrow_height)
        self.good_strip = pygame.Rect(0, strip_location - good_buffer - arrow_height / 2, constants.WINDOWWIDTH, arrow_height + 2 * good_buffer)
        self.ok_strip = pygame.Rect(0, strip_location - ok_buffer - arrow_height / 2, constants.WINDOWWIDTH, arrow_height + 2 * ok_buffer)
        

    def draw(self, surface):
        pygame.draw.rect(surface, colors.YELLOW, self.ok_strip)
        pygame.draw.rect(surface, colors.GREEN, self.good_strip)
        pygame.draw.rect(surface, colors.BLUE, self.perfect_strip)