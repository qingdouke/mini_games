import pygame
import random
from .logic import init_game, snake_block, width, height
from .ui import draw_snake, show_message

def gameLoop():
    # 初始化
    pygame.init()
    print("pygame.init...")
    white, black, red, green, blue = (255, 255, 255), (0, 0, 0), (213, 50, 80), (0, 255, 0), (50, 153, 213)
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("贪吃蛇游戏")
    font_style = pygame.font.SysFont("SimHei", 25)
    score_font = pygame.font.SysFont("SimHei", 35)

    clock = pygame.time.Clock()
    snake_block = 10
    snake_speed = 10

    while True:  # 无限游戏轮回
        x1, y1, x1_change, y1_change, snake_List, Length_of_snake, foodx, foody = init_game()
        game_over = False
        game_close = False

        while not game_over:
            while game_close:
                display.fill(blue)
                show_message(display, font_style, "你输了! 按 C 继续或按 Q 退出", red, width, height)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("quit game")
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            return "menu"
                        elif event.key == pygame.K_c:
                            game_close = False
                            game_over = False
                            x1, y1, x1_change, y1_change, snake_List, Length_of_snake, foodx, foody = init_game()
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
            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True

            display.fill(blue)
            x1 += x1_change
            y1 += y1_change
            pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            draw_snake(display, black, snake_block, snake_List)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                Length_of_snake += 100

            clock.tick(snake_speed)


    pygame.quit()
    quit()

