import pygame
import sys

pygame.init()

# Основные настройки
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Начальное значение времени
total_time = 60
time_left = total_time

# Позиция игрока
playerpos = (100, 100)

# Шрифт для отображения оставшегося времени
font = pygame.font.Font(None, 36)

def draw_timer_bar(time_left, total_time, x, y, width, height):
    ratio = time_left / total_time
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width * ratio, height))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Изменяем позицию игрока (простой пример)
            if event.key == pygame.K_LEFT:
                playerpos = (playerpos[0] - 5, playerpos[1])
            elif event.key == pygame.K_RIGHT:
                playerpos = (playerpos[0] + 5, playerpos[1])
            elif event.key == pygame.K_UP:
                playerpos = (playerpos[0], playerpos[1] - 5)
            elif event.key == pygame.K_DOWN:
                playerpos = (playerpos[0], playerpos[1] + 5)
            
            # Уменьшаем время после каждого движения игрока
            time_left -= 1
            if time_left <= 0:
                print("Время вышло!")
                running = False
            
    # Обновление интерфейса
    screen.fill((0, 0, 0))
    
    # Отрисовка игрока
    pygame.draw.circle(screen, (0, 255, 0), playerpos, 10)
    
    # Отрисовка таймера
    draw_timer_bar(time_left, total_time, 10, 10, 200, 20)
    
    # Отображение числового значения времени
    timer_text = font.render(str(time_left), True, (255, 255, 255))
    screen.blit(timer_text, (220, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
