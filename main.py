import pygame
import sys
from pygame.locals import *

import constants
import colors
import arrow
import timing_strip

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

    timing_strip_obj = timing_strip.TimingStrip(
        strip_location=constants.STRIP_Y,
        perfect_buffer=constants.PERFECT_BUFFER,
        good_buffer=constants.GOOD_BUFFER,
        ok_buffer=constants.OK_BUFFER,
        arrow_height=arrow.Arrow.ARROW_HEIGHT
    )

    arrow_boxes = arrow.ArrowBoxes()

    # Input state variables
    up_pressed = 0
    down_pressed = 0
    left_pressed = 0
    right_pressed = 0

    # Score variables
    score = 0
    score_txt = pygame.font.Font(None, 36).render(f"Score: {score}", True, colors.BLACK)

    while True:

        # Reset inputs
        if up_pressed > 0:
            up_pressed -= 1
        if down_pressed > 0:
            down_pressed -= 1
        if left_pressed > 0:
            left_pressed -= 1
        if right_pressed > 0:
            right_pressed -= 1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        up_pressed = 3
                    case pygame.K_DOWN:
                        down_pressed = 3
                    case pygame.K_LEFT:
                        left_pressed = 3
                    case pygame.K_RIGHT:
                        right_pressed = 3
        
        # Spawn arrows at regular intervals
        ticker = demo_arrow_spawn.spawn_tick(up_arrows, down_arrows, left_arrows, right_arrows, ticker)
        
        # Update each arrow's position
        for arrow_list in [up_arrows, down_arrows, left_arrows, right_arrows]:
            for arrow_instance in arrow_list:
                arrow_instance.tick(mainClock)

        # Take arrow inputs
        if up_pressed > 0:
            if len(up_arrows) > 0:
                arrow_instance = up_arrows[0]
                if abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.PERFECT_BUFFER:
                    print("Up Perfect")
                    up_arrows.pop(0)
                    score += 10
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.GOOD_BUFFER:
                    print("Up Good")
                    up_arrows.pop(0)
                    score += 5
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.OK_BUFFER:
                    print("Up OK")
                    up_arrows.pop(0)
                    score += 2
                else:
                    print("Up Miss")
                    score -= 1
            else:
                print("Up Miss")
                score -= 1
            up_pressed = 0
        
        if down_pressed > 0:
            if len(down_arrows) > 0:
                arrow_instance = down_arrows[0]
                if abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.PERFECT_BUFFER:
                    print("Down Perfect")
                    down_arrows.pop(0)
                    score += 10
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.GOOD_BUFFER:
                    print("Down Good")
                    down_arrows.pop(0)
                    score += 5
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.OK_BUFFER:
                    print("Down OK")
                    down_arrows.pop(0)
                    score += 2
                else:
                    print("Down Miss")
                    score -= 1
            else:
                print("Down Miss")
                score -= 1
            down_pressed = 0

        if left_pressed > 0:
            if len(left_arrows) > 0:
                arrow_instance = left_arrows[0]
                if abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.PERFECT_BUFFER:
                    print("Left Perfect")
                    left_arrows.pop(0)
                    score += 10
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.GOOD_BUFFER:
                    print("Left Good")
                    left_arrows.pop(0)
                    score += 5
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.OK_BUFFER:
                    print("Left OK")
                    left_arrows.pop(0)
                    score += 2
                else:
                    print("Left Miss")
                    score -= 1
            else:
                print("Left Miss")
                score -= 1
            left_pressed = 0
        
        if right_pressed > 0:
            if len(right_arrows) > 0:
                arrow_instance = right_arrows[0]
                if abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.PERFECT_BUFFER:
                    print("Right Perfect")
                    right_arrows.pop(0)
                    score += 10
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.GOOD_BUFFER:
                    print("Right Good")
                    right_arrows.pop(0)
                    score += 5
                elif abs(arrow_instance.y - timing_strip_obj.strip_location) < constants.OK_BUFFER:
                    print("Right OK")
                    right_arrows.pop(0)
                    score += 2
                else:
                    print("Right Miss")
                    score -= 1
            else:
                print("Right Miss")
                score -= 1
            right_pressed = 0
        
        # Update score text
        score_txt = pygame.font.Font(None, 36).render(f"Score: {score}", True, colors.BLACK)
        
        # Garbage collection for arrows that have gone off the screen
        missed_arrows = [arrow_instance for arrow_instance in up_arrows + down_arrows + left_arrows + right_arrows if arrow_instance.rect.top > constants.STRIP_Y + constants.OK_BUFFER]
        score -= len(missed_arrows) # Deduct score for missed arrows

        up_arrows = [arrow_instance for arrow_instance in up_arrows if arrow_instance.rect.top < constants.STRIP_Y + constants.OK_BUFFER]
        down_arrows = [arrow_instance for arrow_instance in down_arrows if arrow_instance.rect.top < constants.STRIP_Y + constants.OK_BUFFER]
        left_arrows = [arrow_instance for arrow_instance in left_arrows if arrow_instance.rect.top < constants.STRIP_Y + constants.OK_BUFFER]
        right_arrows = [arrow_instance for arrow_instance in right_arrows if arrow_instance.rect.top < constants.STRIP_Y + constants.OK_BUFFER]

        


        # Draw the screen
        windowSurface.fill(colors.WHITE)

        # Draw the score text
        windowSurface.blit(score_txt, (10, 10))

        # Draw timing strips
        #timing_strip_obj.draw(windowSurface)

        # Draw the arrow boxes
        arrow_boxes.draw_boxes(windowSurface)

        # Draw each arrow
        for arrow_list in [up_arrows, down_arrows, left_arrows, right_arrows]:
            for arrow_instance in arrow_list:
                windowSurface.blit(arrow_instance.img, arrow_instance.rect)
        
        pygame.display.update()  # Update the display
        mainClock.tick(60)  # Limit to 60 frames per second


main()