import pygame
from pygame.locals import *
import constants

class Arrow:
    ARROW_HEIGHT = 64
    def __init__(self, direction="up"):
        self.direction = direction
        self.img = pygame.image.load(f"IMAGE/{direction}_arrow_with_box_up_and_no_background_so_cool_woah.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (64, 64))
        self.rect = self.img.get_rect()

        self.height = self.rect.height

        self.y = -self.height/2
        self.speed = 5  # Speed of the arrow falling down (pixels per frame)

        match direction:
            case "up":
                self.rect.centerx = constants.WINDOWWIDTH * (3/7)
            case "down":
                self.rect.centerx = constants.WINDOWWIDTH * (4/7)
            case "left":
                self.rect.centerx = constants.WINDOWWIDTH * (2/7)
            case "right":
                self.rect.centerx = constants.WINDOWWIDTH * (5/7)


    def tick(self, mainClock):
        self.y += self.speed
        self.y = round(self.y)
        self.rect.centery = self.y

class ArrowBoxes:
    def __init__(self):
        self.up_box = pygame.image.load("IMAGE/arrow_box_with_thinner_boarder_drawn_line_for_tyler.png").convert_alpha()
        self.up_box = pygame.transform.scale(self.up_box, (64, 64))
        self.down_box = pygame.image.load("IMAGE/arrow_box_with_thinner_boarder_drawn_line_for_tyler.png").convert_alpha()
        self.down_box = pygame.transform.scale(self.down_box, (64, 64))
        self.left_box = pygame.image.load("IMAGE/arrow_box_with_thinner_boarder_drawn_line_for_tyler.png").convert_alpha()
        self.left_box = pygame.transform.scale(self.left_box, (64, 64))
        self.right_box = pygame.image.load("IMAGE/arrow_box_with_thinner_boarder_drawn_line_for_tyler.png").convert_alpha()
        self.right_box = pygame.transform.scale(self.right_box, (64, 64))
    
    def draw_boxes(self, windowSurface):
        # Draw the boxes for each arrow direction
        windowSurface.blit(self.up_box, (constants.WINDOWWIDTH * (3/7) - 32, constants.STRIP_Y - 34))
        windowSurface.blit(self.down_box, (constants.WINDOWWIDTH * (4/7) - 32, constants.STRIP_Y - 34))
        windowSurface.blit(self.left_box, (constants.WINDOWWIDTH * (2/7) - 32, constants.STRIP_Y - 34))
        windowSurface.blit(self.right_box, (constants.WINDOWWIDTH * (5/7) - 32, constants.STRIP_Y - 34))

    
