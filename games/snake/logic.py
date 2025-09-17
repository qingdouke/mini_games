import random

WIDTH = 600
HEIGHT = 400
snake_block = 10

def init_game():
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    x_food = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    y_food = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
    return x1, y1, x1_change, y1_change, snake_list, length_of_snake, x_food, y_food
