import pygame
from games.snake.engine import game_loop as snake_game
from games.whack.engine import game_loop as whack_game
from games.airplane.engine import game_loop as airplane_game
def show_menu():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("小游戏合集启动器")
    font = pygame.font.SysFont("SimHei", 30)
    clock = pygame.time.Clock()

    while True:
        screen.fill((50, 150, 200))
        title = font.render("请选择游戏：", True, (255, 255, 255))
        option1 = font.render("1 - 贪吃蛇", True, (255, 255, 0))
        quit_option = font.render("Q - 退出游戏合集", True, (255, 100, 100))
        option2 = font.render("2 - 打地鼠", True, (255, 255, 0))
        option3 = font.render("3 - 飞机大战", True, (255, 255, 0))

        screen.blit(title, (180, 80))
        screen.blit(option1, (200, 140))
        screen.blit(option2, (200, 180))
        screen.blit(option3, (200, 220))
        screen.blit(quit_option, (180, 280))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return
                elif event.key == pygame.K_1:
                    result = snake_game()
                elif event.key == pygame.K_2:
                    result = whack_game()
                elif event.key == pygame.K_3:
                    result = airplane_game()
                    if result == "menu":
                        continue  # 回到菜单

        clock.tick(30)

if __name__ == "__main__":
    show_menu()
