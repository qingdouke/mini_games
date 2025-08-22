import random

WIDTH = 600
HEIGHT = 400
MOLE_SIZE = 60

def random_mole_position():
    x = random.randint(0, WIDTH - MOLE_SIZE)
    y = random.randint(0, HEIGHT - MOLE_SIZE)
    return x, y
