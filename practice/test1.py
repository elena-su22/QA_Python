import random
import PySimpleGUI as sg


layout = [
    [sg. B('Button 1')],
    [sg. B('Button 2')],
]

window = sg.Window('Button app', layout)
event, values = window.read()
print(event)

colors = ['красный', 'синий', 'зеленый','серый']

# рандомайзер
def choose_color(previous_color):
    remaining_colors = [color for color in colors  if color != previous_color]
    return random.choice(remaining_colors)

# угадываем
def check_guess(guess, actual):
    if guess == actual:
        print("Правильно!")
        return True
    else:
        print("Неправильно.")
        return False


def play():
    print("Старт")
    previous_color = None
    for _ in range(3):
        # Выбор уникального случайного цвета
        color = choose_color(previous_color)
        print("выберите цвет: красный, синий, серый или зеленый")
        guess = input()

        while guess not in colors:
            print("корректный цвет: красный, синий, серый или зеленый")
            guess = input()

        if check_guess(guess, color):
            previous_color = color
            continue
        else:
            guess = input("Попробуйте еще раз: ")
            check_guess(guess, color)
        
    print("Вы угадали все уникальные цвета")


play()