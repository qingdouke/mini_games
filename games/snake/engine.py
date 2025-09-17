import pygame
import random
from .logic import init_game, snake_block, WIDTH, HEIGHT
from .ui import draw_snake, show_message


def game_loop():
    # 初始化
    pygame.init()
    print("pygame.init...")
    white, black, red, green, blue = (255, 255, 255), (0, 0, 0), (213, 50, 80), (0, 255, 0), (50, 153, 213)
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("贪吃蛇游戏")
    font_style = pygame.font.SysFont("SimHei", 25)
    #score_font = pygame.font.SysFont("SimHei", 35)

    clock = pygame.time.Clock()
    snake_speed = 10
    running = True
    while running:  # 无限游戏轮回
        x1, y1, x1_change, y1_change, snake_list, length_of_snake, x_food, y_food = init_game()
        game_over = False
        game_close = False

        while not game_over:
            while game_close:
                display.fill(blue)
                show_message(display, font_style, "你输了! 按 C 继续或按 Q 退出", red, WIDTH, HEIGHT)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("quit game")
                        pygame.quit()
                        return None
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            return "menu"
                        elif event.key == pygame.K_c:
                            game_close = False
                            game_over = False
                            x1, y1, x1_change, y1_change, snake_list, length_of_snake, x_food, y_food = init_game()
                            break  # 跳出 game_close，重新开始

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                game_close = True

            display.fill(blue)
            x1 += x1_change
            y1 += y1_change
            pygame.draw.rect(display, green, [x_food, y_food, snake_block, snake_block])
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(display, black, snake_block, snake_list)

            pygame.display.update()

            if x1 == x_food and y1 == y_food:
                length_of_snake += 1
                new_food_pos_valid = False
                while not new_food_pos_valid:
                    # Generate new random food coordinates
                    x_food = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
                    y_food = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
                    if [x_food, y_food] not in snake_list:
                        new_food_pos_valid = True

            clock.tick(snake_speed)


    pygame.quit()
    quit()

