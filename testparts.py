# import random
# listforrandom = [0,1,2,3,4,5,6,7,8,9]
# listfor4 = []
# numrandom = 0
# for i in range(4):
#     numrandom = random.choice(listforrandom)
#     listfor4.append(numrandom)
# print(listfor4)


x = True
y = True
z = True
while x == True:
    while y == True:
        try:
            v1 = int(input('Введите число 1: '))
            y = False
        except:
            print('Неверный формат данных')
            continue
    while z == True:
        try:
            v2 = int(input('Введите число 2: '))
            z = False
        except:
            print('Неверный формат данных')
            continue
    a=v1+v2
    y = True
    z = True
    if a>100:
        x = False
