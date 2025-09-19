import pygame
import random


# Screen dimensions
WIDTH = 600
HEIGHT = 400
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Placeholder for the player's image and position
        self.image = pygame.Surface((30, 30),pygame.SRCALPHA)
        #define the color for the shape
        self.color = WHITE
        #define the coordinates for the lines
        line_points_1 = [(15,0), (15, 20)]   # vertical line
        line_points_2 = [(0,20), (30, 20)]  # horizontal line
        #draw the lines onto the surface
        pygame.draw.line(self.image, self.color, line_points_1[0], line_points_1[1], 10)
        pygame.draw.line(self.image, self.color, line_points_2[0], line_points_2[1], 10)

        #get the rect from the new image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        # Create a bullet for the middle shot
        #bullet_middle = Bullet(self.rect.centerx, self.rect.top)
        bullet_middle: Bullet = Bullet(self.rect.centerx, self.rect.top)
        # Create a bullet for the left shot
        # Starting position is slightly to the left of the player's center
        # The velocity will be adjusted in the Bullet class
        bullet_left = Bullet(self.rect.centerx - 15, self.rect.top)

        # Create a bullet for the right shot
        # Starting position is slightly to the right
        bullet_right = Bullet(self.rect.centerx + 15, self.rect.top)

        # Add all three bullets to the sprite groups

        return bullet_middle, bullet_left, bullet_right

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Placeholder for the enemy's image and position
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red color for enemies
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 8)

    def update(self):
        # Move the enemy downwards
        self.rect.y += self.speed
        # Reset enemy position if it moves off-screen
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 8)


# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x=0, vel_y=-10):  # Add optional parameters for velocity
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.vel_x = vel_x  # Store the horizontal velocity
        self.vel_y = vel_y  # Store the vertical velocity

    def update(self):
        # Update the position using both velocities
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Kill the bullet if it goes off-screen
        if self.rect.bottom < 0 or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()
 # --- Sprite Groups ---
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def init_game():
    all_sprites.empty()
    enemies.empty()
    bullets.empty()
    # Create game objects
    player = Player()
    all_sprites.add(player)
    # Create some enemies
    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
    return all_sprites, enemies, bullets,player,enemy