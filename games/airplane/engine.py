import pygame
import random
from .ui import draw_score
from .logic import WIDTH, HEIGHT, BLACK, all_sprites, enemies, bullets, Player, Enemy


def game_loop():
    # --- Sprite Groups ---
    # Initialize Pygame
    pygame.init()
    font = pygame.font.SysFont("SimHei", 30)
    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Airplane War")
    # Game clock to control frame rate
    clock = pygame.time.Clock()
    # Create game objects
    player = Player()
    all_sprites.add(player)
    score = 0
    # Create some enemies
    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # --- Game Loop ---
    running = True
    while running:
        # Keep the loop running at a set speed
        clock.tick(60)

        # Process events
        for event in pygame.event.get():
            # Check for closing the window
            if event.type == pygame.QUIT:
                running = False
            # Check for player shooting
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Update all sprites
        all_sprites.update()

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
            print("Game Over!")
            running = False


        # --- Drawing ---
        screen.fill(BLACK)  # Fill the background with black
        all_sprites.draw(screen)  # Draw all sprites on the screen
        draw_score(screen, font, score)
        # Update the display
        pygame.display.flip()


    # Quit the game
    #pygame.quit()
    return "menu"

