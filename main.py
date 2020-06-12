import pygame
import random
import time
from buttons import button

condition = True

pygame.init()

display_width = 900
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Rock, Paper, Scissors')

black = (0, 0, 0)
gray = (50, 50, 50)
light_gray = (205, 205, 205)
white = (255, 255, 255)

red = (255, 20, 20)
green = (20, 255, 20)

display.fill(white)

clock = pygame.time.Clock()

stop = None

p1_win_num = 0
p2_win_num = 0


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def result_msg(msg, x, y, w, h, color):
    pygame.draw.rect(display, color, (x, y, w, h))
    pygame.draw.rect(display, black, (x, y, w, h), 5)
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (x + (w / 2), y + (h / 2))
    display.blit(text_surf, text_rect)


def menu_button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
        pygame.draw.rect(display, black, (x, y, w, h), 5)
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(display, ic, (x, y, w, h))
        pygame.draw.rect(display, black, (x, y, w, h), 5)
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = (x + (w / 2), y + (h / 2))
    display.blit(text_surf, text_rect)


def scissors(choice):
    if choice is 'Rock':
        return 'Loss'
    elif choice is 'Scissors':
        return 'Draw'
    elif choice is 'Paper':
        return 'Success'


def rock(choice):
    if choice is 'Paper':
        return 'Loss'
    elif choice is 'Rock':
        return 'Draw'
    elif choice is 'Scissors':
        return 'Success'


def paper(choice):
    if choice is 'Scissors':
        return 'Loss'
    elif choice is 'Paper':
        return 'Draw'
    elif choice is 'Rock':
        return 'Success'


def choice_handling(choice1, choice2):
    if choice1 == 'Scissors':
        if choice2 == 'Rock':
            return 2
        if choice2 == 'Paper':
            return 1
        if choice2 == 'Scissors':
            return 'Draw'
    if choice1 == 'Rock':
        if choice2 == 'Rock':
            return 'Draw'
        if choice2 == 'Paper':
            return 2
        if choice2 == 'Scissors':
            return 1
    if choice1 == 'Paper':
        if choice2 == 'Rock':
            return 1
        if choice2 == 'Paper':
            return 'Draw'
        if choice2 == 'Scissors':
            return 2


def menu():
    display.fill(white)
    pygame.display.update()
    while True:
        menu_button("A. I.", 50, 250, 300, 100, light_gray, green, ai_main)
        menu_button("PvP (Unfinished)", 550, 250, 300, 100, light_gray, green, pvp_main)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(80)


def ai_main():
    x = 300
    w = 300
    y = 0
    h = 100
    success_num = 0
    fail_num = 0
    display.fill(white)
    while True:
        pygame.draw.rect(display, white, (750, 0, 150, 50))
        choice_num = random.randint(0, 2)
        if choice_num == 0:
            choice = 'Rock'
        elif choice_num == 1:
            choice = 'Scissors'
        elif choice_num == 2:
            choice = 'Paper'

        result_s = button(
            display, "Scissors", black,
            0, 500, 300, 100,
            light_gray, green, black, scissors, choice, True, None, 0.15
        )
        result_r = button(
            display,
            "Rock",
            black,
            300, 500, 300, 100,
            light_gray,
            green,
            black,
            rock,
            choice,
            True,
            None,
            0.15
        )
        result_p = button(
            display,
            "Paper",
            black,
            600, 500, 300, 100,
            light_gray,
            green,
            black,
            paper,
            choice,
            True,
            None,
            0.15
        )

        if result_p is not None or result_r is not None or result_s is not None:

            if result_p is not None:
                result_msg(f"{choice}", x, y, w, h, light_gray)
                result_msg(f"{result_p}", 400, 200, 100, 100, light_gray)

                if result_p is 'Success':
                    success_num += 1
                elif result_p is 'Loss':
                    fail_num += 1

            elif result_r is not None:
                result_msg(f"{choice}", x, y, w, h, light_gray)
                result_msg(f"{result_r}", 400, 200, 100, 100, light_gray)

                if result_r is 'Success':
                    success_num += 1
                elif result_r is 'Loss':
                    fail_num += 1

            elif result_s is not None:
                result_msg(f"{choice}", x, y, w, h, light_gray)
                result_msg(f"{result_s}", 400, 200, 100, 100, light_gray)

                if result_s is 'Success':
                    success_num += 1
                elif result_s is 'Loss':
                    fail_num += 1

        result_msg(f"S: {success_num} : F: {fail_num}", 700, 0, 200, 50, light_gray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(80)


def pvp_main():
    display.fill(white)
    p1_result = None
    p2_result = None

    global p1_win_num
    global p2_win_num

    result_msg("Player 1", 200, 250, 500, 100, light_gray)

    while p1_result is None:
        display.fill(white)
        result_s = button(display, "Scissors", black, 0, 500, 300, 100, light_gray, green, black, None, None, None,
                          'Scissors')
        result_r = button(display, "Rock", black, 300, 500, 300, 100, light_gray, green, black, None, None, None,
                          'Rock')
        result_p = button(display, "Paper", black, 600, 500, 300, 100, light_gray, green, black, None, None, None,
                          'Paper')
        result_msg(f"P1: {p1_win_num} : P2: {p2_win_num}", 700, 0, 200, 50, light_gray)

        if result_s is not None:
            p1_result = result_s
            break
        if result_r is not None:
            p1_result = result_r
            break
        if result_p is not None:
            p1_result = result_p
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(80)

    display.fill(white)
    result_msg("Player 2", 200, 250, 500, 100, light_gray)
    pygame.display.update()
    time.sleep(1)
    del result_s, result_r, result_p
    time.sleep(0.1)
    while p2_result is None:
        display.fill(white)
        result_s = button(
            display, "Scissors", black, 0, 500, 300, 100, light_gray, green, black, None, None, None, 'Scissors'
        )
        result_r = button(
            display, "Rock", black, 300, 500, 300, 100, light_gray, green, black, None, None, None, 'Rock'
        )
        result_p = button(
            display, "Paper", black, 600, 500, 300, 100, light_gray, green, black, None, None, None, 'Paper'
        )
        result_msg(f"P1: {p1_win_num} : P2: {p2_win_num}", 700, 0, 200, 50, light_gray)

        if result_s == 'Scissors':
            p2_result = result_s
            break
        if result_r is not None:
            p2_result = result_r
            break
        if result_p is not None:
            p2_result = result_p
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(80)

    display.fill(white)
    result = choice_handling(p1_result, p2_result)
    if result == 1:
        result_msg("Player 1 won!", 345, 250, 210, 100, light_gray)
        p1_win_num += 1
    if result == 2:
        result_msg("Player 2 won!", 345, 250, 210, 100, light_gray)
        p2_win_num += 1
    if result == 'Draw':
        result_msg("Draw!", 345, 250, 210, 100, light_gray)


# if condition:
menu()
# condition = False
