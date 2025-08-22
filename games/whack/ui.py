import pygame
import os

# 加载地鼠图片（只加载一次）
mole_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "blackegg.png"))
mole_image = pygame.transform.scale(mole_image, (60, 60))  # 缩放为统一尺寸

#def draw_mole(screen, x, y, size):
 #   pygame.draw.circle(screen, (139, 69, 19), (x + size // 2, y + size // 2), size // 2)
def draw_mole(screen, x, y):
    screen.blit(mole_image, (x, y))
def draw_score(screen, font, score):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
