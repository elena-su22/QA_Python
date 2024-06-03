# list1 = [1,2,3,4,5,6]
# def dlist1(list = list1):
#     v1 = max(list)
#     return v1
# print(dlist1())

# maxnum = dlist1()
# print(maxnum)
# print(type(maxnum))


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

# dist = int(input('Введите количество км: '))
# kmcost = int(input('Введите стоимость 1 км: '))
# startcost = int(input('Введите стартовую цену: '))
# def taxicost(dist=dist,kmcost=kmcost,startcost=startcost):
#     price = dist*kmcost
#     price = price + startcost
#     return price
# print(taxicost())

# def taxicost():
#     dist = int(input('Введите количество км: '))
#     kmcost = int(input('Введите стоимость 1 км: '))
#     startcost = int(input('Введите стартовую цену: '))
#     price = dist*kmcost
#     price = price + startcost
#     return price
# print(taxicost())


# проверка пароля

def checkpass(pass1="12Trgggg"):
    if len(pass1) < 8:
        return False
    elif pass1.islower() == True:
        return False
    elif pass1.isupper() == True:
        return False
    elif any(i.isdigit() for i in pass1) == True:
        return True
    else:
        return False
print(checkpass('Abcd1234'))
print(checkpass('qwerty'))
print(checkpass('abcD'))
print(checkpass('ABCD1234'))
