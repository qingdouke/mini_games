import pygame

def draw_snake(display, color, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, color, [x[0], x[1], snake_block, snake_block])

def show_message(display, font_style, msg, color, width, height):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])
