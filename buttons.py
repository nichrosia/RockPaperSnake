import time
import pygame
import random


def button(
        display,
        message,
        text_color,
        x,
        y,
        width,
        height,

        inactive_color=(205, 205, 205),
        active_color=(0, 255, 0),
        border_color=(0, 0, 0),

        function=None,
        function_parameter=None,
        return_function=None,

        return_value=None,

        seconds_between=0,
        text_font=None,
):

    if text_font is None:
        text_font = pygame.font.Font("freesansbold.ttf", 20)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:

        pygame.draw.rect(display, active_color, (x, y, width, height))
        pygame.draw.rect(display, border_color, (x, y, width, height), 5)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(seconds_between)
                if return_function is not None:
                    return function(function_parameter)
                if return_value is not None:
                    return return_value
                function(function_parameter)

    else:
        pygame.draw.rect(display, inactive_color, (x, y, width, height))
        pygame.draw.rect(display, border_color, (x, y, width, height), 5)

    text_surface = text_font.render(message, True, text_color)
    text_surf, text_rect = text_surface, text_surface.get_rect()
    text_rect.center = (x + (width / 2), y + (height / 2))

    display.blit(text_surf, text_rect)
