import random
import arrow


def spawn_tick(up_arrows, down_arrows, left_arrows, right_arrows, tickerIn):
    ticker = tickerIn
    ticker += 1
    if ticker % 20 == 0:  # Spawn an arrow every 20 ticks
        direction = random.choice(["up", "down", "left", "right"])
        match direction:
            case "up":
                up_arrows.append(arrow.Arrow(direction))
            case "down":
                down_arrows.append(arrow.Arrow(direction))
            case "left":
                left_arrows.append(arrow.Arrow(direction))
            case "right":
                right_arrows.append(arrow.Arrow(direction))
    return ticker

