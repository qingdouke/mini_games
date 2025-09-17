import pygame
import random


# --- Classes for Game Objects ---

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Placeholder for the player's image and position
        self.image = pygame.Surface((50, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self):
        # Handle player movement with keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep the player within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def shoot(self):
        # Create a new bullet and add it to a sprite group
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Placeholder for the enemy's image and position
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red color for enemies
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 8)

    def update(self):
        # Move the enemy downwards
        self.rect.y += self.speed
        # Reset enemy position if it moves off-screen
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 8)


# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Placeholder for the bullet's image and position
        self.image = pygame.Surface((5, 15))
        self.image.fill((0, 255, 0))  # Green color for bullets
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10  # Negative speed to move up

    def update(self):
        # Move the bullet upwards
        self.rect.y += self.speed
        # Kill the bullet if it goes off-screen
        if self.rect.bottom < 0:
            self.kill()

