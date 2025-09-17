import pygame
from .logic import random_mole_position, WIDTH, HEIGHT, MOLE_SIZE
from .ui import draw_mole, draw_score

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("打地鼠")
    font = pygame.font.SysFont("SimHei", 30)
    clock = pygame.time.Clock()

    score = 0
    mole_x, mole_y = random_mole_position()
    mole_timer = 0
    mole_interval = 1000  # 毫秒

    while True:
        screen.fill((0, 100, 0))
        draw_mole(screen, mole_x, mole_y)
        draw_score(screen, font, score)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return "menu"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mole_x < mx < mole_x + MOLE_SIZE and mole_y < my < mole_y + MOLE_SIZE:
                    score += 1
                    mole_x, mole_y = random_mole_position()

        mole_timer += clock.get_time()
        if mole_timer >= mole_interval:
            mole_x, mole_y = random_mole_position()
            mole_timer = 0

        clock.tick(60)
