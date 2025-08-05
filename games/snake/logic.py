import random

width = 600
height = 400
snake_block = 10

def init_game():
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    return x1, y1, x1_change, y1_change, snake_List, Length_of_snake, foodx, foody
