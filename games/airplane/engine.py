import pygame
import random
from .ui import draw_score
from .logic import WIDTH, HEIGHT, WHITE,BLACK, Player, Enemy, init_game
from ..snake.ui import show_message

def game_loop():
    # Initialize Pygame
    pygame.init()
    font = pygame.font.SysFont("SimHei", 30)
    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Airplane War")
    # Game clock to control frame rate
    clock = pygame.time.Clock()
    blue = (50, 153, 213)
    all_sprites, enemies, bullets,player,enemy = init_game()
    # --- Game Loop ---
    score = 0
    running = True
    game_over = False
    while running:
        # Keep the loop running at a set speed
        clock.tick(60)
        # Process events
        for event in pygame.event.get():
            # Check for closing the window
            if event.type == pygame.QUIT:
                running = False
        while not game_over:
            for event in pygame.event.get():
                # Check for closing the window
                if event.type == pygame.QUIT:
                    running = False
                # Check for player shooting
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet_middle, bullet_left, bullet_right = player.shoot()
                        all_sprites.add(bullet_middle, bullet_left, bullet_right)
                        bullets.add(bullet_middle, bullet_left, bullet_right)
            # Update all sprites
            all_sprites.update()
            clock.tick(60)
            # --- Collision Detection ---
            # Check for bullet hitting an enemy
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
           # score = hits
            for hit in hits:
                # Respawn a new enemy
                new_enemy = Enemy()
                all_sprites.add(new_enemy)
                enemies.add(new_enemy)
                score += 1
            # Check for enemy hitting the player
            hits = pygame.sprite.spritecollide(player, enemies, False)  # 'False' means the enemy is not killed on collision
            if hits:
                game_over = True

            # --- Drawing ---
            screen.fill(BLACK)  # Fill the background with black
            all_sprites.draw(screen)  # Draw all sprites on the screen
            draw_score(screen, font, score)
            # Update the display
            pygame.display.flip()

        while game_over:
            clock.tick(60)
            screen.fill(blue)
            show_message(screen, font, "你输了! 按 C 继续或按 Q 退出", WHITE, WIDTH, HEIGHT)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    print("some key down")
                    if event.key == pygame.K_c:
                        all_sprites, enemies, bullets,player,enemy = init_game()
                        game_over = False
                        #break
                    elif event.key == pygame.K_q:
                        return "menu"

    # Quit the game
    pygame.quit()
    #return "menu"

