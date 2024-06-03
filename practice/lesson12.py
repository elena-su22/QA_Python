import string
import re
import random

# #1
# numlist = [1,2,3,4,5,6,7,8,9]
# def num3(numlistx = numlist):
#     num3list = []
#     for i in numlistx:
#         if i %3 == 0:
#             num3list.append(i)
#     return num3list
# print(num3())

# #2
# phonbooklist = []
# x = True
# while x == True:
#     choicex = input('Введите действие: добавить контакт, вывести книгу, выход')
#     if choicex == 'выход':
#         print('Работа программы остановленна')
#         x = False
#         break
#     elif choicex == 'вывести книгу':
#         print(phonbooklist)
#         continue
#     elif choicex == 'добавить контакт':
#         namex = input('Введите имя контакта')
#         numx = int(input('Введите номер контакта'))
#         phonbooklist.append({'имя':namex,'номер':numx})
#         continue
#     else:
#         print('Введено неверное действие')
#         continue

# #3
# x = True
# while x == True:
#     try:
#         v1 = int(input('Введите число 1: '))
#         v2 = int(input('Введите число 2: '))
#     except:
#         print('Неверный формат данных')
#         continue

#     v3 = str(input('Введите действие(+-/* или другой символ для прекращения работы): '))
#     def plus():
#         return v1+v2
#     def minus():
#         return v1-v2
#     def proizv():
#         return v1*v2
#     def delit():
#         if v2 == 0:
#             return 'На 0 делить нельзя'
#         else:
#             return v1/v2
#     if v3 == '+':
#         result = plus()
#         print(f'Сумма чисел 1 и 2: {result}')
#     elif v3 == '-':
#         result = minus()
#         print(f'Разность чисел 1 и 2: {result}')
#     elif v3 == '*':
#         result = proizv()
#         print(f'Произведение чисел 1 и 2: {result}')
#     elif v3 == '/':
#         result = delit()
#         print(f'Результат деления числа 1 на число 2: {result}')
#     else:
#         print('Действие введено неверно, работа завершена')
#         x = False

# #4
# text1 = 'Hello, world! You are so wonderful! I love this world!'
# word1 = 'world'
# def foundworld(textx=text1,wordx = word1):
#     textwithoutpunct = re.sub(r'[^\w\s]', '', textx)
#     textwithoutpunct = textwithoutpunct.lower()
#     textwithoutpunct = textwithoutpunct.split()
#     print(textwithoutpunct)
#     scoreword = 0
#     for i in textwithoutpunct:
#         if wordx == i:
#             scoreword += 1
#     print(f'слово {wordx} встречается в строке {scoreword} раз')
# foundworld()
            
#5
dataforvic = [{'Кто самое большое животное?':'синий кит'}, {'Кто самый быстрый зверь?':'гепард'},{'Кто самая быстрая птица?':'сапсан'}, {'Кто самое умное животное?':'шимпанзе'}]
def victorina(dataforvicx = dataforvic):
    vinscore = 0
    for i in range(3):
        choice1 = random.choice(dataforvicx)
        for q1, answ1 in choice1.items():
            print(q1)
            answ = input('Введите ответ!')
            if answ == answ1:
                print('Правильно!')
                vinscore += 1
            else:
                print('Неправильно')
                vinscore = vinscore
        dataforvicx.remove(choice1)
    return vinscore
n = victorina()
print(f'Вы набрали {n} очков в викторине!')
