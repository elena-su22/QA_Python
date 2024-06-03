import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hero vs Beast")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.Font(None, 36)


hero1 = {'hp': 3, 'int': 1, 'might': 5}
beast1 = {'hp': 3, 'damage': 1}


message = ""
displayed_message = ""


def fight(fightway, hero=hero1, beast=beast1):
    global message
    if fightway == '2':
        dice1 = random.randint(1, 6)
        if dice1 <= hero['int']:
            message = 'Вы сумели скрытно обойти зверя'
        else:
            message = 'Бой начинается!'
    elif fightway == '1':
        dice1 = random.randint(1, 6)
        if dice1 <= 3:
            message = 'Вы сбежали от зверя'
        else:
            message = 'Бой начинается!'
    elif fightway == '3':
        dice1 = random.randint(1, 6)
        if dice1 <= hero['might']:
            beast['hp'] -= 1
            message = 'Вы ранили зверя'
        message += '\nБой начинается!'

def display_message(surface, text, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, BLACK)
        surface.blit(text_surface, (x, y + i * 40))

def update_displayed_message():
    global message, displayed_message
    if displayed_message != message:
        displayed_message += message[len(displayed_message)]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hide_button.collidepoint(event.pos):
                fight('2')
            elif run_button.collidepoint(event.pos):
                fight('1')
            elif attack_button.collidepoint(event.pos):
                fight('3')

    screen.fill(WHITE)

    # Отображение кнопок
    hide_button = pygame.draw.rect(screen, BLACK, (50, 100, 200, 50))
    run_button = pygame.draw.rect(screen, BLACK, (50, 200, 200, 50))
    attack_button = pygame.draw.rect(screen, BLACK, (50, 300, 200, 50))

    # Текст на кнопках
    for button_text, button_rect in [("Скрытно обойти", hide_button), ("Бежать", run_button), ("Напасть", attack_button)]:
        text_surface = font.render(button_text, True, WHITE)
        screen.blit(text_surface, button_rect.topleft)

    # Обновление и отображение сообщения
    update_displayed_message()
    display_message(screen, displayed_message, 50, 400)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()